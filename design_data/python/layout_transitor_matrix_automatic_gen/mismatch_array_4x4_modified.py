#!/usr/bin/env python3
"""
SCALABLE MISMATCH ARRAY GENERATOR - NMOS ONLY
Modified version with configurable dimensions and PMOS disabled
"""

import pya
import klayout.db as db
import sys
import json

# ========== SCALABLE CONFIGURATION ==========
# These values should match what's configured in the GUI

# Default transistor dimensions (will be overridden if pattern file contains them)
TRANSISTOR_W = 1.03      # µm - Width (configurable)
TRANSISTOR_L = 0.35      # µm - Length (configurable)
TRANSISTOR_NG = 1        # Number of fingers

# Spacing parameters (µm)
GUARDRING_WIDTH = 0.5       # Guardring width
GUARDRING_SPACING = 2.0     # Distance from transistor to guardring (configurable, default 2µm)

# Array size (will be read from pattern file)
ARRAY_SIZE = 4              # Default 4x4 array

# Design rules IHP SG13G2
METAL1_WIDTH = 0.28
METAL2_WIDTH = 0.36
METAL3_WIDTH = 0.20
POLY_WIDTH = 0.13
VIA1_SIZE = 0.26
VIA2_SIZE = 0.26
CONT_SIZE = 0.22
CONT_SPACING = 0.28
PAD_SIZE = 50.0

# PDK
LIB_NAME = 'SG13_dev'

# Layers
LAYER_MAP = {
    'Activ':    (1, 0),
    'GatPoly':  (5, 0),
    'Cont':     (6, 0),
    'nSD':      (7, 0),
    'Metal1':   (8, 0),
    'Metal2':   (10, 0),
    'Metal3':   (30, 0),
    'pSD':      (14, 0),
    'Via1':     (19, 0),
    'Via2':     (29, 0),
    'NWell':    (31, 0),
    'Ptap':     (32, 0),
    'Ntap':     (33, 0),  
    'TEXT':     (63, 0),
}

def load_pattern_and_config():
    """Load pattern and extract configuration if available"""
    global TRANSISTOR_W, TRANSISTOR_L, GUARDRING_SPACING, ARRAY_SIZE
    
    # Try to load pattern file
    pattern_data = None
    config = {}
    
    # Check for pattern file
    if 'pattern_file' in globals():
        try:
            with open(pattern_file, 'r') as f:
                data = json.load(f)
                pattern_data = data.get('pattern_data', {})
                config = data.get('metadata', {})
        except Exception as e:
            print(f"⚠ Error loading pattern file: {e}")
    else:
        # Try temp_pattern.json
        try:
            with open('temp_pattern.json', 'r') as f:
                data = json.load(f)
                pattern_data = data.get('pattern_data', {})
                config = data.get('metadata', {})
        except:
            pass
    
    # Apply configuration if available
    if config:
        if 'transistor_W' in config:
            TRANSISTOR_W = config['transistor_W']
            print(f"✓ Loaded W={TRANSISTOR_W}µm from pattern file")
        
        if 'transistor_L' in config:
            TRANSISTOR_L = config['transistor_L']
            print(f"✓ Loaded L={TRANSISTOR_L}µm from pattern file")
        
        if 'guardring_spacing' in config:
            GUARDRING_SPACING = config['guardring_spacing']
            print(f"✓ Loaded guardring_spacing={GUARDRING_SPACING}µm from pattern file")
        
        if 'array_rows' in config:
            ARRAY_SIZE = config['array_rows']
            print(f"✓ Loaded array_size={ARRAY_SIZE}x{ARRAY_SIZE} from pattern file")
    
    # Convert pattern keys from strings to tuples
    if pattern_data:
        pattern = {}
        for str_key, value in pattern_data.items():
            if isinstance(str_key, str) and ',' in str_key:
                row, col = map(int, str_key.split(','))
                pattern[(row, col)] = value
            else:
                pattern[str_key] = value
        return pattern
    
    # Return default pattern if nothing loaded
    return get_default_pattern()

class ScalableMismatchArray:
    """Scalable mismatch array generator - NMOS only"""
    
    def __init__(self):
        print("\n" + "="*60)
        print("SCALABLE MISMATCH ARRAY GENERATOR")
        print("="*60)
        
        # Load configuration and pattern
        self.pattern_data = load_pattern_and_config()
        
        # Display current configuration
        print(f"\nConfiguration:")
        print(f"  Transistor W: {TRANSISTOR_W} µm")
        print(f"  Transistor L: {TRANSISTOR_L} µm")
        print(f"  Guardring spacing: {GUARDRING_SPACING} µm")
        print(f"  Guardring width: {GUARDRING_WIDTH} µm")
        print(f"  Array size: {ARRAY_SIZE}x{ARRAY_SIZE}")
        
        # Calculate pitches
        self.calculate_pitches()
        
        # Load library
        self.lib = pya.Library.library_by_name(LIB_NAME)
        if not self.lib:
            raise Exception(f"Library {LIB_NAME} not found")
        
        # Create layout
        self.layout = db.Layout(True)
        self.layout.dbu = 0.001  # 1nm
        self.top_cell = self.layout.create_cell(f'MismatchArray_{ARRAY_SIZE}x{ARRAY_SIZE}_NMOS')
        
        # Create layer indices
        self.layers = {}
        for name, (layer, datatype) in LAYER_MAP.items():
            self.layers[name] = self.layout.layer(layer, datatype)
        
        print(f"✓ Layout initialized")
        
        # Debug tracking
        self.debug_info = {
            'transistor_count': 0,
            'dummy_count': 0,
            'gate_routes': [],
            'pattern_verification': []
        }
    
    def calculate_pitches(self):
        """Calculate pitches based on transistor dimensions and spacing"""
        # Get actual transistor bbox size (this is approximate)
        # The actual size will be determined when we create the PCell
        estimated_t_width = TRANSISTOR_W
        estimated_t_height = TRANSISTOR_L * 4  # Approximate height
        
        # Calculate pitches
        # Pitch = transistor_dimension + 2*spacing + guardring_width
        self.pitch_x = estimated_t_width + 2 * GUARDRING_SPACING + GUARDRING_WIDTH
        self.pitch_y = estimated_t_height + 2 * GUARDRING_SPACING + GUARDRING_WIDTH
        
        print(f"  Calculated pitch X: {self.pitch_x:.3f} µm")
        print(f"  Calculated pitch Y: {self.pitch_y:.3f} µm")
    
    def dbu(self, value_um):
        """Convert µm to database units"""
        return int(value_um / self.layout.dbu)
    
    def create_transistor_pcell(self):
        """Create NMOS transistor PCell"""
        pcell_name = 'nmos'
        
        # Find PCell declaration
        pcell_decl = self.lib.layout().pcell_declaration(pcell_name)
        if not pcell_decl:
            print(f"\n⚠ PCell '{pcell_name}' not found")
            raise Exception(f"PCell {pcell_name} not found in library {LIB_NAME}")
        
        # Parameters for PCell
        params = {
            'w': f'{TRANSISTOR_W}u',
            'l': f'{TRANSISTOR_L}u',
            'ng': str(TRANSISTOR_NG)
        }
        
        # Create PCell instance
        return self.layout.add_pcell_variant(self.lib, pcell_decl.id(), params)
    
    def calculate_shared_guardring_array(self, transistor_bbox, rows, cols):
        """Calculate dimensions for array with shared guardrings"""
        
        # Get actual transistor dimensions
        actual_t_width = transistor_bbox.width() * self.layout.dbu
        actual_t_height = transistor_bbox.height() * self.layout.dbu
        
        print(f"\nActual transistor dimensions:")
        print(f"  Width: {actual_t_width:.3f} µm")
        print(f"  Height: {actual_t_height:.3f} µm")
        
        # Recalculate pitches with actual dimensions
        pitch_x = self.dbu(actual_t_width + 2 * GUARDRING_SPACING + GUARDRING_WIDTH)
        pitch_y = self.dbu(actual_t_height + 2 * GUARDRING_SPACING + GUARDRING_WIDTH)
        
        print(f"  Final pitch X: {pitch_x * self.layout.dbu:.3f} µm")
        print(f"  Final pitch Y: {pitch_y * self.layout.dbu:.3f} µm")
        
        gr_width = self.dbu(GUARDRING_WIDTH)
        gr_spacing = self.dbu(GUARDRING_SPACING)
        
        total_width = cols * pitch_x + gr_width
        total_height = rows * pitch_y + gr_width
        
        cell_inner_width = pitch_x - gr_width
        cell_inner_height = pitch_y - gr_width
        
        return {
            'pitch_x': pitch_x,
            'pitch_y': pitch_y,
            'gr_width': gr_width,
            'gr_spacing': gr_spacing,
            'total_width': total_width,
            'total_height': total_height,
            'cell_inner_width': cell_inner_width,
            'cell_inner_height': cell_inner_height,
            't_width': transistor_bbox.width(),
            't_height': transistor_bbox.height()
        }
    
    def create_shared_guardring_structure(self, array_cell, geom, rows, cols):
        """Create shared guardring structure for NMOS array"""
        print("\nCreating shared guardring structure...")
        
        gr_width = geom['gr_width']
        
        # Create vertical guardring stripes
        for col in range(cols + 1):
            x = col * geom['pitch_x']
            stripe = db.Box(
                x, 0,
                x + gr_width, geom['total_height']
            )
            array_cell.shapes(self.layers['Activ']).insert(stripe)
            array_cell.shapes(self.layers['pSD']).insert(stripe)
            array_cell.shapes(self.layers['Ptap']).insert(stripe)
        
        # Create horizontal guardring stripes
        for row in range(rows + 1):
            y = row * geom['pitch_y']
            stripe = db.Box(
                0, y,
                geom['total_width'], y + gr_width
            )
            array_cell.shapes(self.layers['Activ']).insert(stripe)
            array_cell.shapes(self.layers['pSD']).insert(stripe)
            array_cell.shapes(self.layers['Ptap']).insert(stripe)
        
        # Add contacts to guardring intersections
        cont_size = self.dbu(CONT_SIZE)
        for row in range(rows + 1):
            for col in range(cols + 1):
                x = col * geom['pitch_x'] + gr_width // 2
                y = row * geom['pitch_y'] + gr_width // 2
                
                cont_box = db.Box(
                    x - cont_size//2, y - cont_size//2,
                    x + cont_size//2, y + cont_size//2
                )
                array_cell.shapes(self.layers['Cont']).insert(cont_box)
                
                m1_box = cont_box.enlarged(self.dbu(0.05))
                array_cell.shapes(self.layers['Metal1']).insert(m1_box)
        
        print(f"✓ Created shared guardring grid: {cols+1} x {rows+1} stripes")
    
    def create_nmos_array(self):
        """Create NMOS array with proper centering"""
        print(f"\n{'='*60}")
        print(f"Creating NMOS array {ARRAY_SIZE}x{ARRAY_SIZE}")
        print(f"{'='*60}")
        
        array_cell = self.layout.create_cell(f'nmos_array_{ARRAY_SIZE}x{ARRAY_SIZE}')
        
        # Create transistor PCell
        transistor_pcell = self.create_transistor_pcell()
        transistor_cell = self.layout.cell(transistor_pcell)
        t_bbox = transistor_cell.bbox()
        
        total_cols = ARRAY_SIZE + 2  # Add dummy columns
        total_rows = ARRAY_SIZE
        geom = self.calculate_shared_guardring_array(t_bbox, total_rows, total_cols)
        
        # Create guardring structure
        self.create_shared_guardring_structure(array_cell, geom, total_rows, total_cols)
        
        # Place transistors
        transistor_info = []
        active_count = 0
        dummy_count = 0
        
        for row in range(total_rows):
            for col in range(total_cols):
                # Calculate center of available space within guardring
                # The transistor should be centered with GUARDRING_SPACING on all sides
                cell_center_x = col * geom['pitch_x'] + geom['gr_width'] + geom['cell_inner_width'] // 2
                cell_center_y = row * geom['pitch_y'] + geom['gr_width'] + geom['cell_inner_height'] // 2
                
                # Position transistor centered in the cell
                bbox_center_x = t_bbox.center().x
                bbox_center_y = t_bbox.center().y
                
                trans_x = cell_center_x - bbox_center_x
                trans_y = cell_center_y - bbox_center_y
                
                trans = db.Trans(db.Point(trans_x, trans_y))
                array_cell.insert(db.CellInstArray(transistor_pcell, trans))
                
                is_dummy = (col == 0 or col == total_cols - 1)
                
                info = {
                    'row': row,
                    'col': col,
                    'active_row': row,
                    'active_col': col - 1 if not is_dummy else -1,
                    'x': cell_center_x,
                    'y': cell_center_y,
                    'is_dummy': is_dummy,
                    'gate_x': cell_center_x * self.layout.dbu,
                    'gate_y': cell_center_y * self.layout.dbu
                }
                
                transistor_info.append(info)
                
                if is_dummy:
                    dummy_count += 1
                    self.debug_info['dummy_count'] += 1
                else:
                    active_count += 1
                    self.debug_info['transistor_count'] += 1
        
        print(f"✓ Placed {active_count} active + {dummy_count} dummy transistors")
        
        # Verify spacing
        if len(transistor_info) > 1:
            t0 = transistor_info[0]
            t1 = transistor_info[1]
            
            # Calculate actual spacing from transistor edge to guardring
            t_half_width = geom['t_width'] * self.layout.dbu / 2
            t_half_height = geom['t_height'] * self.layout.dbu / 2
            
            left_spacing = (t0['x'] * self.layout.dbu) - t_half_width - GUARDRING_WIDTH
            right_spacing = geom['pitch_x'] * self.layout.dbu - GUARDRING_WIDTH - (t0['x'] * self.layout.dbu - t_half_width)
            
            print(f"\nSpacing verification:")
            print(f"  Transistor to left guardring: {left_spacing:.3f} µm (target: {GUARDRING_SPACING} µm)")
            print(f"  Transistor to right guardring: {right_spacing:.3f} µm (target: {GUARDRING_SPACING} µm)")
        
        return array_cell, transistor_info, geom
    
    def route_gate_connections(self, array_cell, transistor_info):
        """Route gate connections using loaded pattern"""
        print(f"\nRouting gate connections...")
        
        m3_width = self.dbu(METAL3_WIDTH)
        
        active_transistors = [t for t in transistor_info if not t['is_dummy']]
        routed_count = 0
        
        for t in active_transistors:
            row = t['active_row']
            col = t['active_col']
            
            pattern_key = (row, col)
            if pattern_key not in self.pattern_data:
                print(f"⚠ No pattern for transistor [{row},{col}]")
                continue
            
            pattern = self.pattern_data[pattern_key]
            
            # Gate position
            gate_x = t['x']
            gate_y = t['y']
            
            # Create via stack at gate
            self.create_gate_via_stack(array_cell, gate_x, gate_y)
            
            # Apply pattern
            offset_y_dbu = self.dbu(pattern['offset_y'])
            start_x = gate_x
            start_y = gate_y + offset_y_dbu
            
            h_length_dbu = self.dbu(pattern['h_length'])
            
            # Horizontal direction based on column
            if col >= ARRAY_SIZE//2:
                b_end_x = start_x + h_length_dbu
            else:
                b_end_x = start_x - h_length_dbu
            
            # Draw horizontal segment
            if h_length_dbu > 0:
                h_box = db.Box(
                    min(start_x, b_end_x) - m3_width//2, start_y - m3_width//2,
                    max(start_x, b_end_x) + m3_width//2, start_y + m3_width//2
                )
                array_cell.shapes(self.layers['Metal3']).insert(h_box)
            
            # Vertical segment
            v_length_dbu = self.dbu(pattern['v_length'])
            
            if pattern['goes_up']:
                exit_y = start_y + v_length_dbu
            else:
                exit_y = start_y - v_length_dbu
            
            v_box = db.Box(
                b_end_x - m3_width // 2, min(start_y, exit_y),
                b_end_x + m3_width // 2, max(start_y, exit_y)
            )
            array_cell.shapes(self.layers['Metal3']).insert(v_box)
            
            # Add label
            label = f"G{row}_{col}"
            self.add_text(array_cell, b_end_x, exit_y, label)
            self.debug_info['gate_routes'].append(label)
            
            routed_count += 1
        
        print(f"✓ Routed {routed_count} gates")
    
    def create_gate_via_stack(self, cell, x, y):
        """Create via stack from Poly to Metal3"""
        cont_size = self.dbu(CONT_SIZE)
        via1_size = self.dbu(VIA1_SIZE)
        via2_size = self.dbu(VIA2_SIZE)
        
        # Contact
        cont_box = db.Box(
            x - cont_size//2, y - cont_size//2,
            x + cont_size//2, y + cont_size//2
        )
        cell.shapes(self.layers['Cont']).insert(cont_box)
        
        # M1
        m1_pad = cont_box.enlarged(self.dbu(0.05))
        cell.shapes(self.layers['Metal1']).insert(m1_pad)
        
        # Via1
        via1_box = db.Box(
            x - via1_size//2, y - via1_size//2,
            x + via1_size//2, y + via1_size//2
        )
        cell.shapes(self.layers['Via1']).insert(via1_box)
        
        # M2
        m2_pad = via1_box.enlarged(self.dbu(0.05))
        cell.shapes(self.layers['Metal2']).insert(m2_pad)
        
        # Via2
        via2_box = db.Box(
            x - via2_size//2, y - via2_size//2,
            x + via2_size//2, y + via2_size//2
        )
        cell.shapes(self.layers['Via2']).insert(via2_box)
    
    def add_text(self, cell, x, y, text):
        """Add text label"""
        text_obj = db.Text(text, db.Trans(db.Point(x, y)))
        cell.shapes(self.layers['TEXT']).insert(text_obj)
    
    def generate_structure(self, output_file):
        """Generate complete NMOS-only structure"""
        print("\n" + "="*60)
        print("GENERATING NMOS MISMATCH TEST STRUCTURE")
        print("="*60)
        
        # Create NMOS array
        nmos_array, nmos_info, nmos_geom = self.create_nmos_array()
        self.route_gate_connections(nmos_array, nmos_info)
        
        # Place in top cell
        nmos_trans = db.Trans(db.Point(0, 0))
        self.top_cell.insert(db.CellInstArray(nmos_array.cell_index(), nmos_trans))
        
        # PMOS GENERATION DISABLED
        print("\n⚠ PMOS generation disabled - NMOS only structure")
        
        # Add title
        bbox = self.top_cell.bbox()
        title_y = bbox.top + self.dbu(10)
        title = f"NMOS Mismatch Array {ARRAY_SIZE}x{ARRAY_SIZE} - W={TRANSISTOR_W}µm L={TRANSISTOR_L}µm"
        self.add_text(self.top_cell, bbox.center().x, title_y, title)
        
        # Save
        print(f"\nSaving to: {output_file}")
        self.layout.write(output_file)
        
        # Final report
        self.print_final_report()
    
    def print_final_report(self):
        """Print final summary"""
        bbox = self.top_cell.bbox()
        total_area = bbox.width() * bbox.height() / 1e6
        
        print("\n" + "="*60)
        print("FINAL REPORT - NMOS STRUCTURE GENERATED")
        print("="*60)
        print(f"\nConfiguration:")
        print(f"  Transistor W: {TRANSISTOR_W} µm")
        print(f"  Transistor L: {TRANSISTOR_L} µm")
        print(f"  Guardring spacing: {GUARDRING_SPACING} µm")
        print(f"  Array: {ARRAY_SIZE}x{ARRAY_SIZE}")
        
        print(f"\nDimensions:")
        print(f"  Total area: {total_area:.0f} µm²")
        print(f"  Chip size: {bbox.width()/1000:.1f} x {bbox.height()/1000:.1f} µm")
        
        print(f"\nTransistor count:")
        print(f"  Active: {self.debug_info['transistor_count']}")
        print(f"  Dummy: {self.debug_info['dummy_count']}")
        print(f"  Total: {self.debug_info['transistor_count'] + self.debug_info['dummy_count']}")
        
        print(f"\nFeatures:")
        print(f"  ✓ Scalable dimensions (W, L configurable)")
        print(f"  ✓ Configurable guardring spacing ({GUARDRING_SPACING}µm)")
        print(f"  ✓ Shared guardring borders")
        print(f"  ✓ NMOS only (PMOS disabled)")
        print(f"  ✓ Pattern-based routing")
        print("="*60)

def main():
    """Main function"""
    
    # Output file
    try:
        output
    except NameError:
        output = f"mismatch_array_{ARRAY_SIZE}x{ARRAY_SIZE}_nmos_only.gds"
    
    print(f"Output file: {output}")
    
    # Generate structure
    generator = ScalableMismatchArray()
    generator.generate_structure(output)
    
    print(f"\nTo view the result:")
    print(f"  klayout {output}")

if __name__ == "__main__":
    main()
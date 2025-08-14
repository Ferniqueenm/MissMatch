#!/usr/bin/env python3
"""
SCALABLE MISMATCH ARRAY GENERATOR - NMOS AND PMOS SUPPORT
Modified version with configurable dimensions and full PMOS support
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
    'Activ':    (1, 0),   # Active area
    'GatPoly':  (5, 0),   # Gate poly
    'Cont':     (6, 0),   # Contact (not "locint" as in IHP script)
    'nSD':      (7, 0),   # N+ implant
    'Metal1':   (8, 0),   # Metal 1
    'Metal2':   (10, 0),  # Metal 2
    'Metal3':   (30, 0),  # Metal 3
    'pSD':      (14, 0),  # P+ implant
    'Via1':     (19, 0),  # Via 1
    'Via2':     (29, 0),  # Via 2
    'NWell':    (31, 0),  # N-well
    # Ptap and Ntap are NOT used by IHP for guard rings!
    # 'Ptap':     (32, 0),  # Not used
    # 'Ntap':     (33, 0),  # Not used
    'TEXT':     (63, 0),  # Text layer
}

def get_default_pattern():
    """Return default pattern if no pattern file is found"""
    return {}

def load_pattern_and_config():
    """Load pattern and extract configuration if available - Phase 2 & 3 version"""
    global TRANSISTOR_W, TRANSISTOR_L, GUARDRING_SPACING, ARRAY_SIZE
    
    # Initialize return data
    full_data = {
        'pattern_data': {},
        'metadata': {}
    }
    
    # Try to load pattern file
    try:
        with open('temp_pattern.json', 'r') as f:
            data = json.load(f)
            full_data = data
            print(f"✓ Loaded temp_pattern.json")
    except Exception as e:
        print(f"⚠ Could not load temp_pattern.json: {e}")
    
    # Extract config from metadata
    config = full_data.get('metadata', {})
    
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
        
        # Phase 2: Handle dummy mode
        if 'dummy_mode' in config:
            print(f"✓ Dummy mode: {config['dummy_mode']}")
        elif 'has_dummies' in config:
            # Backward compatibility
            dummy_mode = 'sides' if config['has_dummies'] else 'none'
            config['dummy_mode'] = dummy_mode
            print(f"✓ Converted has_dummies to dummy_mode: {dummy_mode}")
        
        if 'device_type' in config:
            print(f"✓ Device type: {config['device_type']}")
    
    # Convert pattern keys from strings to tuples
    pattern_data = full_data.get('pattern_data', {})
    if pattern_data:
        pattern = {}
        for str_key, value in pattern_data.items():
            if isinstance(str_key, str) and ',' in str_key:
                row, col = map(int, str_key.split(','))
                pattern[(row, col)] = value
            else:
                pattern[str_key] = value
        full_data['pattern_data'] = pattern
    
    return full_data

class ScalableMismatchArray:
    """Scalable mismatch array generator - NMOS and PMOS support"""
    
    def __init__(self):
        print("\n" + "="*60)
        print("SCALABLE MISMATCH ARRAY GENERATOR")
        print("="*60)
        
        # Load configuration and pattern
        self.full_data = load_pattern_and_config()
        self.pattern_data = self.full_data.get('pattern_data', {})
        self.metadata = self.full_data.get('metadata', {})
        self.device_type = self.metadata.get('device_type', 'nmos')
        self.dummy_mode = self.metadata.get('dummy_mode', 'sides')
        
        # Display current configuration
        print(f"\nConfiguration:")
        print(f"  Device Type: {self.device_type}")
        print(f"  Dummy Mode: {self.dummy_mode}")
        print(f"  Transistor W: {TRANSISTOR_W} µm")
        print(f"  Transistor L: {TRANSISTOR_L} µm")
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
        
        # Create top cell with appropriate name
        if self.device_type == 'both':
            cell_name = f'MismatchArray_{ARRAY_SIZE}x{ARRAY_SIZE}_BOTH'
        elif self.device_type == 'pmos':
            cell_name = f'MismatchArray_{ARRAY_SIZE}x{ARRAY_SIZE}_PMOS'
        else:
            cell_name = f'MismatchArray_{ARRAY_SIZE}x{ARRAY_SIZE}_NMOS'
        
        self.top_cell = self.layout.create_cell(cell_name)
        
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
    
    def create_transistor_pcell(self, transistor_type='nmos'):
        """Create transistor PCell - FIXED to accept type parameter"""
        pcell_name = transistor_type
        
        # Find PCell declaration
        pcell_decl = self.lib.layout().pcell_declaration(pcell_name)
        if not pcell_decl:
            print(f"\n⚠ PCell '{pcell_name}' not found")
            print("Available PCells in library:")
            for i in range(self.lib.layout().pcells()):
                pd = self.lib.layout().pcell_declaration(i)
                if pd:
                    print(f"  - {pd.name()}")
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
        """
        Create shared guardring structure for NMOS array
        CORRECTED based on official IHP implementation:
        - Uses pSD (NO Ptap)
        - Uses Activ
        - Uses Cont
        - Uses Metal1
        - NO NWell for substrate contact
        """
        print("\nCreating shared guardring structure for NMOS (IHP-compliant)...")
        
        gr_width = geom['gr_width']
        
        # For NMOS array: p-type substrate contact
        # Based on IHP script: uses pSD + Activ (NO Ptap!)
        
        # Create vertical guardring stripes
        for col in range(cols + 1):
            x = col * geom['pitch_x']
            stripe_box = db.Box(
                x, 0,
                x + gr_width, geom['total_height']
            )
            
            # Active area (required for guard ring)
            array_cell.shapes(self.layers['Activ']).insert(stripe_box)
            
            # P+ implant for substrate contact (pSD layer)
            array_cell.shapes(self.layers['pSD']).insert(stripe_box)
            
            # NO Ptap layer - IHP doesn't use it!
            # NO NWell - substrate contacts don't need it
        
        # Create horizontal guardring stripes
        for row in range(rows + 1):
            y = row * geom['pitch_y']
            stripe_box = db.Box(
                0, y,
                geom['total_width'], y + gr_width
            )
            
            # Active area
            array_cell.shapes(self.layers['Activ']).insert(stripe_box)
            
            # P+ implant for substrate contact
            array_cell.shapes(self.layers['pSD']).insert(stripe_box)
            
            # NO Ptap layer - IHP doesn't use it!
        
        # Add contacts to guardring intersections
        cont_size = self.dbu(CONT_SIZE)
        m1_enc = self.dbu(0.05)  # Metal1 enclosure of contact
        
        for row in range(rows + 1):
            for col in range(cols + 1):
                # Center of guardring intersection
                x_center = col * geom['pitch_x'] + gr_width // 2
                y_center = row * geom['pitch_y'] + gr_width // 2
                
                # Contact (Cont layer)
                cont_box = db.Box(
                    x_center - cont_size//2, 
                    y_center - cont_size//2,
                    x_center + cont_size//2, 
                    y_center + cont_size//2
                )
                array_cell.shapes(self.layers['Cont']).insert(cont_box)
                
                # Metal1 over contact (with enclosure)
                m1_box = db.Box(
                    x_center - cont_size//2 - m1_enc,
                    y_center - cont_size//2 - m1_enc,
                    x_center + cont_size//2 + m1_enc,
                    y_center + cont_size//2 + m1_enc
                )
                array_cell.shapes(self.layers['Metal1']).insert(m1_box)
        
        print(f"✓ Created substrate contact guardring: {cols+1} x {rows+1} stripes")
        print(f"  Layers used: Activ, pSD, Cont, Metal1")


    def create_shared_guardring_structure_pmos(self, array_cell, geom, rows, cols):
        """
        Create N-well guardring for PMOS - CORRECT IHP IMPLEMENTATION
        Uses: NWell + Activ + nSD + Cont + Metal1 (NO Ntap!)
        """
        print("\nCreating N-well guardring structure for PMOS (IHP-compliant)...")
        
        gr_width = geom['gr_width']
        
        # First create N-well for entire PMOS array
        nwell_margin = self.dbu(0.5)
        nwell_box = db.Box(
            -nwell_margin, 
            -nwell_margin,
            geom['total_width'] + nwell_margin,
            geom['total_height'] + nwell_margin
        )
        array_cell.shapes(self.layers['NWell']).insert(nwell_box)
        
        # Create guardring stripes (N-well contact)
        for col in range(cols + 1):
            x = col * geom['pitch_x']
            stripe_box = db.Box(
                x, 0,
                x + gr_width, geom['total_height']
            )
            
            # Active area
            array_cell.shapes(self.layers['Activ']).insert(stripe_box)
            
            # N+ implant for N-well contact (nSD layer)
            array_cell.shapes(self.layers['nSD']).insert(stripe_box)
            
            # NO Ntap layer - IHP doesn't use it!
        
        # Horizontal stripes
        for row in range(rows + 1):
            y = row * geom['pitch_y']
            stripe_box = db.Box(
                0, y,
                geom['total_width'], y + gr_width
            )
            
            array_cell.shapes(self.layers['Activ']).insert(stripe_box)
            array_cell.shapes(self.layers['nSD']).insert(stripe_box)
        
        # Add contacts (same as NMOS)
        cont_size = self.dbu(CONT_SIZE)
        m1_enc = self.dbu(0.05)
        
        for row in range(rows + 1):
            for col in range(cols + 1):
                x_center = col * geom['pitch_x'] + gr_width // 2
                y_center = row * geom['pitch_y'] + gr_width // 2
                
                cont_box = db.Box(
                    x_center - cont_size//2, 
                    y_center - cont_size//2,
                    x_center + cont_size//2, 
                    y_center + cont_size//2
                )
                array_cell.shapes(self.layers['Cont']).insert(cont_box)
                
                m1_box = db.Box(
                    x_center - cont_size//2 - m1_enc,
                    y_center - cont_size//2 - m1_enc,
                    x_center + cont_size//2 + m1_enc,
                    y_center + cont_size//2 + m1_enc
                )
                array_cell.shapes(self.layers['Metal1']).insert(m1_box)
        
        print(f"✓ Created N-well contact guardring: {cols+1} x {rows+1} stripes")
        print(f"  Layers used: NWell, Activ, nSD, Cont, Metal1")


    def create_nmos_array(self):
        """Create NMOS array with configurable dummy arrangement - Phase 2"""
        print(f"\n{'='*60}")
        print(f"Creating NMOS array {ARRAY_SIZE}x{ARRAY_SIZE}")
        print(f"{'='*60}")
        
        array_cell = self.layout.create_cell(f'nmos_array_{ARRAY_SIZE}x{ARRAY_SIZE}')
        
        # Get dummy mode from metadata
        dummy_mode = self.metadata.get('dummy_mode', 'sides')
        print(f"  Dummy mode: {dummy_mode}")
        
        # Calculate total dimensions based on dummy mode
        if dummy_mode == 'none':
            total_rows = ARRAY_SIZE
            total_cols = ARRAY_SIZE
        elif dummy_mode == 'sides':
            total_rows = ARRAY_SIZE
            total_cols = ARRAY_SIZE + 2
        else:  # full ring
            total_rows = ARRAY_SIZE + 2
            total_cols = ARRAY_SIZE + 2
        
        print(f"  Total array dimensions: {total_rows}x{total_cols}")
        print(f"  Active array: {ARRAY_SIZE}x{ARRAY_SIZE}")
        
        # Create transistor PCell
        transistor_pcell = self.create_transistor_pcell('nmos')
        transistor_cell = self.layout.cell(transistor_pcell)
        t_bbox = transistor_cell.bbox()
        
        geom = self.calculate_shared_guardring_array(t_bbox, total_rows, total_cols)
        
        # Create guardring structure
        self.create_shared_guardring_structure(array_cell, geom, total_rows, total_cols)
        
        # Place transistors
        transistor_info = []
        active_count = 0
        dummy_count = 0
        
        for row in range(total_rows):
            for col in range(total_cols):
                # Determine if dummy based on mode
                is_dummy = False
                
                if dummy_mode == 'sides':
                    is_dummy = (col == 0 or col == total_cols-1)
                elif dummy_mode == 'full':
                    is_dummy = (row == 0 or row == total_rows-1 or 
                            col == 0 or col == total_cols-1)
                
                # Calculate center position
                cell_center_x = col * geom['pitch_x'] + geom['gr_width'] + geom['cell_inner_width'] // 2
                cell_center_y = row * geom['pitch_y'] + geom['gr_width'] + geom['cell_inner_height'] // 2
                
                # Position transistor
                bbox_center_x = t_bbox.center().x
                bbox_center_y = t_bbox.center().y
                
                trans_x = cell_center_x - bbox_center_x
                trans_y = cell_center_y - bbox_center_y
                
                trans = db.Trans(db.Point(trans_x, trans_y))
                array_cell.insert(db.CellInstArray(transistor_pcell, trans))
                
                # Calculate active indices
                if is_dummy:
                    active_row = -1
                    active_col = -1
                else:
                    if dummy_mode == 'none':
                        active_row = row
                        active_col = col
                    elif dummy_mode == 'sides':
                        active_row = row
                        active_col = col - 1
                    else:  # full ring
                        active_row = row - 1
                        active_col = col - 1
                
                info = {
                    'row': row,
                    'col': col,
                    'active_row': active_row,
                    'active_col': active_col,
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
        
        if dummy_mode == 'full':
            print(f"Full dummy ring: top/bottom/left/right borders")
        elif dummy_mode == 'sides':
            print(f"Side dummies only: left/right columns")
        else:
            print(f"No dummy transistors")
        
        return array_cell, transistor_info, geom

    def create_pmos_array(self):
        """Create PMOS array with configurable dummy arrangement - Phase 2"""
        print(f"\n{'='*60}")
        print(f"Creating PMOS array {ARRAY_SIZE}x{ARRAY_SIZE}")
        print(f"{'='*60}")
        
        array_cell = self.layout.create_cell(f'pmos_array_{ARRAY_SIZE}x{ARRAY_SIZE}')
        
        # Get dummy mode from metadata
        dummy_mode = self.metadata.get('dummy_mode', 'sides')
        print(f"  Dummy mode: {dummy_mode}")
        
        # Calculate total dimensions based on dummy mode
        if dummy_mode == 'none':
            total_rows = ARRAY_SIZE
            total_cols = ARRAY_SIZE
        elif dummy_mode == 'sides':
            total_rows = ARRAY_SIZE
            total_cols = ARRAY_SIZE + 2
        else:  # full ring
            total_rows = ARRAY_SIZE + 2
            total_cols = ARRAY_SIZE + 2
        
        # Create PMOS transistor PCell
        transistor_pcell = self.create_transistor_pcell('pmos')
        transistor_cell = self.layout.cell(transistor_pcell)
        t_bbox = transistor_cell.bbox()
        
        geom = self.calculate_shared_guardring_array(t_bbox, total_rows, total_cols)
        
        # Create N-well guardring structure for PMOS
        self.create_shared_guardring_structure_pmos(array_cell, geom, total_rows, total_cols)
        
        # Place transistors (same logic as NMOS)
        transistor_info = []
        active_count = 0
        dummy_count = 0
        
        for row in range(total_rows):
            for col in range(total_cols):
                # Determine if dummy based on mode
                is_dummy = False
                
                if dummy_mode == 'sides':
                    is_dummy = (col == 0 or col == total_cols-1)
                elif dummy_mode == 'full':
                    is_dummy = (row == 0 or row == total_rows-1 or 
                            col == 0 or col == total_cols-1)
                
                # Calculate center position
                cell_center_x = col * geom['pitch_x'] + geom['gr_width'] + geom['cell_inner_width'] // 2
                cell_center_y = row * geom['pitch_y'] + geom['gr_width'] + geom['cell_inner_height'] // 2
                
                # Position transistor
                bbox_center_x = t_bbox.center().x
                bbox_center_y = t_bbox.center().y
                
                trans_x = cell_center_x - bbox_center_x
                trans_y = cell_center_y - bbox_center_y
                
                trans = db.Trans(db.Point(trans_x, trans_y))
                array_cell.insert(db.CellInstArray(transistor_pcell, trans))
                
                # Calculate active indices
                if is_dummy:
                    active_row = -1
                    active_col = -1
                else:
                    if dummy_mode == 'none':
                        active_row = row
                        active_col = col
                    elif dummy_mode == 'sides':
                        active_row = row
                        active_col = col - 1
                    else:  # full ring
                        active_row = row - 1
                        active_col = col - 1
                
                info = {
                    'row': row,
                    'col': col,
                    'active_row': active_row,
                    'active_col': active_col,
                    'x': cell_center_x,
                    'y': cell_center_y,
                    'is_dummy': is_dummy,
                    'gate_x': cell_center_x * self.layout.dbu,
                    'gate_y': cell_center_y * self.layout.dbu
                }
                
                transistor_info.append(info)
                
                if is_dummy:
                    dummy_count += 1
                else:
                    active_count += 1
        
        print(f"✓ Placed {active_count} active + {dummy_count} dummy PMOS transistors")
        
        return array_cell, transistor_info, geom

    def create_route_from_points(self, array_cell, gate_x, gate_y, route_points, m3_width):
        """
        Create route from points - Y-INVERSION ONLY
        """
        segments = []
        
        if len(route_points) < 2:
            return segments
        
        for i in range(len(route_points) - 1):
            current_point = route_points[i]
            next_point = route_points[i + 1]
            
            # Only invert Y coordinate
            curr_x = gate_x + self.dbu(current_point['x'])  # Keep X as is
            curr_y = gate_y - self.dbu(current_point['y'])  # Invert Y
            next_x = gate_x + self.dbu(next_point['x'])     # Keep X as is
            next_y = gate_y - self.dbu(next_point['y'])     # Invert Y
            
            # Rest of the code remains the same...
            dx = abs(next_x - curr_x)
            dy = abs(next_y - curr_y)
            
            if dx > 1 and dy < 1:  # Horizontal
                box = db.Box(
                    min(curr_x, next_x) - m3_width//2,
                    curr_y - m3_width//2,
                    max(curr_x, next_x) + m3_width//2,
                    curr_y + m3_width//2
                )
                array_cell.shapes(self.layers['Metal3']).insert(box)
                
            elif dy > 1 and dx < 1:  # Vertical
                box = db.Box(
                    curr_x - m3_width//2,
                    min(curr_y, next_y) - m3_width//2,
                    curr_x + m3_width//2,
                    max(curr_y, next_y) + m3_width//2
                )
                array_cell.shapes(self.layers['Metal3']).insert(box)
            
            elif dx > 1 and dy > 1:
                # L-shape
                h_box = db.Box(
                    min(curr_x, next_x) - m3_width//2,
                    curr_y - m3_width//2,
                    max(curr_x, next_x) + m3_width//2,
                    curr_y + m3_width//2
                )
                array_cell.shapes(self.layers['Metal3']).insert(h_box)
                
                v_box = db.Box(
                    next_x - m3_width//2,
                    min(curr_y, next_y) - m3_width//2,
                    next_x + m3_width//2,
                    max(curr_y, next_y) + m3_width//2
                )
                array_cell.shapes(self.layers['Metal3']).insert(v_box)
        
        return segments
    
    def create_legacy_route(self, array_cell, gate_x, gate_y, pattern, active_col, m3_width):
        """Create route from legacy pattern format (backward compatibility)"""
        segments = []
        
        # Apply pattern WITHOUT direction logic
        offset_y_dbu = self.dbu(pattern.get('offset_y', 0))
        h_length_dbu = self.dbu(pattern.get('h_length', 0))
        v_length_dbu = self.dbu(pattern.get('v_length', 0))
        
        start_x = gate_x
        start_y = gate_y + offset_y_dbu
        
        # NO AUTOMATIC DIRECTION - respect pattern exactly
        # NO MIRROR EFFECT - all columns use same pattern
        end_x = start_x + h_length_dbu
        
        # Horizontal segment
        if h_length_dbu > 0:
            h_box = db.Box(
                min(start_x, end_x) - m3_width//2, start_y - m3_width//2,
                max(start_x, end_x) + m3_width//2, start_y + m3_width//2
            )
            array_cell.shapes(self.layers['Metal3']).insert(h_box)
            segments.append({'type': 'H', 'start': (start_x, start_y), 'end': (end_x, start_y)})
        
        # Vertical segment - respect pattern direction
        if pattern.get('goes_up', False):
            exit_y = start_y + v_length_dbu
        else:
            exit_y = start_y - v_length_dbu
        
        v_box = db.Box(
            end_x - m3_width//2, min(start_y, exit_y),
            end_x + m3_width//2, max(start_y, exit_y)
        )
        array_cell.shapes(self.layers['Metal3']).insert(v_box)
        segments.append({'type': 'V', 'start': (end_x, start_y), 'end': (end_x, exit_y)})
        
        return segments


    def route_gate_connections(self, array_cell, transistor_info):
        """Route gate connections - wrapper for enhanced version"""
        # Usar la versión enhanced si existe
        if hasattr(self, 'route_gate_connections_enhanced'):
            return self.route_gate_connections_enhanced(array_cell, transistor_info)
        else:
            print("WARNING: No enhanced routing method found, skipping gate routing")
            return None

    def route_gate_connections_enhanced(self, array_cell, transistor_info):
        """
        Route with FIXED transistor mapping
        """
        print(f"\nRouting gate connections...")
        print(f"  Array size: {ARRAY_SIZE}x{ARRAY_SIZE}")
        print(f"  Dummy mode: {self.dummy_mode}")
        
        m3_width = self.dbu(METAL3_WIDTH)
        active_transistors = [t for t in transistor_info if not t['is_dummy']]
        routes_created = 0
        
        for t in active_transistors:
            # Get ACTIVE coordinates from KLayout's perspective
            active_row = t['active_row']  
            active_col = t['active_col']
            
            if active_row < 0 or active_col < 0:
                continue
            
            # CRITICAL FIX: Map KLayout coordinates to GUI coordinates
            # GUI row 0 = top, KLayout row 0 = bottom
            # So we need to flip the row for lookup
            gui_row = (ARRAY_SIZE - 1) - active_row
            gui_col = active_col  # Columns don't change
            
            # Look up pattern with GUI coordinates
            pattern_key_str = f"{gui_row},{gui_col}"
            pattern_key = (gui_row, gui_col)
            
            # Try both formats
            pattern = self.pattern_data.get(pattern_key)
            if not pattern:
                pattern = self.pattern_data.get(pattern_key_str)
            
            if not pattern:
                print(f"  KL[{active_row},{active_col}] -> GUI[{gui_row},{gui_col}] - No pattern")
                continue
            
            print(f"  KL[{active_row},{active_col}] -> GUI[{gui_row},{gui_col}] - Found pattern")
            
            # Gate position
            gate_x = t['x']
            gate_y = t['y']
            
            # Create via stack at gate
            self.create_gate_via_stack(array_cell, gate_x, gate_y)
            
            # Draw route from pattern
            if 'route_points' in pattern:
                self.create_route_from_points(
                    array_cell, gate_x, gate_y, 
                    pattern['route_points'], m3_width
                )
                
                # Add label
                if pattern['route_points']:
                    last_point = pattern['route_points'][-1]
                    label_x = gate_x + self.dbu(last_point['x'])
                    label_y = gate_y - self.dbu(last_point['y'])  # Y-inverted
                    
                    # Use GUI coordinates for label
                    label = f"G{gui_row}_{gui_col}"
                    self.add_text(array_cell, label_x, label_y, label)
                
                routes_created += 1
        
        print(f"  Created {routes_created} routes")
        return routes_created



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
        """Generate complete structure with NMOS and/or PMOS - FIXED VERSION"""
        print("\n" + "="*60)
        print("GENERATING MISMATCH TEST STRUCTURE")
        print("="*60)
        
        print(f"Device type requested: {self.device_type}")
        
        if self.device_type == 'both':
            # Create both NMOS and PMOS arrays
            nmos_array, nmos_info, nmos_geom = self.create_nmos_array()
            self.route_gate_connections(nmos_array, nmos_info)
            
            pmos_array, pmos_info, pmos_geom = self.create_pmos_array()
            self.route_gate_connections(pmos_array, pmos_info)
            
            # Place side by side
            nmos_trans = db.Trans(db.Point(0, 0))
            self.top_cell.insert(db.CellInstArray(nmos_array.cell_index(), nmos_trans))
            
            separation = self.dbu(30)
            pmos_x = nmos_array.bbox().width() + separation
            pmos_trans = db.Trans(db.Point(pmos_x, 0))
            self.top_cell.insert(db.CellInstArray(pmos_array.cell_index(), pmos_trans))
            
            print("✓ Generated both NMOS and PMOS arrays")
        
        elif self.device_type == 'pmos':
            # PMOS only
            pmos_array, pmos_info, pmos_geom = self.create_pmos_array()
            self.route_gate_connections(pmos_array, pmos_info)
            pmos_trans = db.Trans(db.Point(0, 0))
            self.top_cell.insert(db.CellInstArray(pmos_array.cell_index(), pmos_trans))
            
            print("✓ Generated PMOS array only")
        
        else:
            # NMOS only (default)
            nmos_array, nmos_info, nmos_geom = self.create_nmos_array()
            self.route_gate_connections(nmos_array, nmos_info)
            nmos_trans = db.Trans(db.Point(0, 0))
            self.top_cell.insert(db.CellInstArray(nmos_array.cell_index(), nmos_trans))
            
            print("✓ Generated NMOS array only")
        
        # Add title
        bbox = self.top_cell.bbox()
        title_y = bbox.top + self.dbu(10)
        title = f"{self.device_type.upper()} Mismatch Array {ARRAY_SIZE}x{ARRAY_SIZE} - W={TRANSISTOR_W}µm L={TRANSISTOR_L}µm"
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
        print(f"FINAL REPORT - {self.device_type.upper()} STRUCTURE GENERATED")
        print("="*60)
        print(f"\nConfiguration:")
        print(f"  Device Type: {self.device_type}")
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
        print(f"  ✓ {self.device_type.upper()} support enabled")
        print(f"  ✓ Pattern-based routing")
        print("="*60)

def main():
    """Main function"""
    
    # Load data to get device type
    full_data = load_pattern_and_config()
    device_type = full_data.get('metadata', {}).get('device_type', 'nmos')
    
    # Output file with appropriate name
    try:
        output
    except NameError:
        if device_type == 'both':
            output = f"mismatch_array_{ARRAY_SIZE}x{ARRAY_SIZE}_both.gds"
        elif device_type == 'pmos':
            output = f"mismatch_array_{ARRAY_SIZE}x{ARRAY_SIZE}_pmos.gds"
        else:
            output = f"mismatch_array_{ARRAY_SIZE}x{ARRAY_SIZE}_nmos.gds"
    
    print(f"Output file: {output}")
    
    # Generate structure
    generator = ScalableMismatchArray()
    generator.generate_structure(output)
    
    print(f"\nTo view the result:")
    print(f"  klayout {output}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Simple test to verify coordinate mapping
Creates a minimal pattern for a 2x2 array with side dummies
"""

import json

def create_test_pattern():
    """
    Create a simple test pattern for 2x2 array with side dummies
    Each transistor gets a unique simple route for identification
    """
    
    # Configuration
    array_rows = 2
    array_cols = 2
    dummy_mode = 'sides'
    
    # This will create physical array of 2x4 (2 rows, 4 cols with dummies)
    # Active transistors at physical positions:
    # [0,1] = active[0,0] -> klayout[1,0]
    # [0,2] = active[0,1] -> klayout[1,1]
    # [1,1] = active[1,0] -> klayout[0,0]
    # [1,2] = active[1,1] -> klayout[0,1]
    
    pattern_data = {
        'metadata': {
            'array_rows': array_rows,
            'array_cols': array_cols,
            'dummy_mode': dummy_mode,
            'device_type': 'nmos',
            'transistor_W': 1.03,
            'transistor_L': 0.35,
            'guardring_spacing': 2.0,
            'description': 'Test pattern for coordinate mapping debug'
        },
        'pattern_data': {}
    }
    
    # Create distinct patterns for each transistor
    # Using KLayout coordinates as keys
    
    # Top-left (GUI[0,0] -> KL[1,0])
    pattern_data['pattern_data']['1,0'] = {
        'route_points': [
            {'x': 0, 'y': 0},      # Start at gate
            {'x': -1, 'y': 0},     # Go left 1µm
            {'x': -1, 'y': -2}     # Go up 2µm
        ],
        'gui_coords': (0, 0),
        'description': 'Top-left: Left then Up'
    }
    
    # Top-right (GUI[0,1] -> KL[1,1])
    pattern_data['pattern_data']['1,1'] = {
        'route_points': [
            {'x': 0, 'y': 0},      # Start at gate
            {'x': 1, 'y': 0},      # Go right 1µm
            {'x': 1, 'y': -2}      # Go up 2µm
        ],
        'gui_coords': (0, 1),
        'description': 'Top-right: Right then Up'
    }
    
    # Bottom-left (GUI[1,0] -> KL[0,0])
    pattern_data['pattern_data']['0,0'] = {
        'route_points': [
            {'x': 0, 'y': 0},      # Start at gate
            {'x': -1, 'y': 0},     # Go left 1µm
            {'x': -1, 'y': 2}      # Go down 2µm
        ],
        'gui_coords': (1, 0),
        'description': 'Bottom-left: Left then Down'
    }
    
    # Bottom-right (GUI[1,1] -> KL[0,1])
    pattern_data['pattern_data']['0,1'] = {
        'route_points': [
            {'x': 0, 'y': 0},      # Start at gate
            {'x': 1, 'y': 0},      # Go right 1µm
            {'x': 1, 'y': 2}       # Go down 2µm
        ],
        'gui_coords': (1, 1),
        'description': 'Bottom-right: Right then Down'
    }
    
    # Save the test pattern
    with open('test_pattern_2x2.json', 'w') as f:
        json.dump(pattern_data, f, indent=2)
    
    print("Test pattern created: test_pattern_2x2.json")
    print("\nExpected routing:")
    print("="*50)
    print("GUI Position | KLayout Key | Route Direction")
    print("-"*50)
    print("[0,0] top-left  | '1,0' | Left then Up")
    print("[0,1] top-right | '1,1' | Right then Up")
    print("[1,0] bot-left  | '0,0' | Left then Down")
    print("[1,1] bot-right | '0,1' | Right then Down")
    print("="*50)
    print("\nTo test:")
    print("1. Copy test_pattern_2x2.json to temp_pattern.json")
    print("2. Run the KLayout script")
    print("3. Check if routes appear in correct positions")

def verify_klayout_lookup():
    """
    Show what KLayout will look for given its active coordinates
    """
    print("\n" + "="*60)
    print("KLAYOUT LOOKUP VERIFICATION")
    print("="*60)
    
    # Simulate KLayout's perspective
    array_rows = 2
    array_cols = 2
    dummy_mode = 'sides'
    
    # Physical array: 2x4
    total_rows = 2
    total_cols = 4
    
    print("\nKLayout will process transistors in this order:")
    print("-"*60)
    
    for row in range(total_rows):
        for col in range(total_cols):
            # Check if dummy
            is_dummy = (col == 0 or col == 3)
            
            if not is_dummy:
                # Calculate active indices (KLayout's calculation)
                active_row = row
                active_col = col - 1  # Subtract 1 for left dummy column
                
                print(f"Physical[{row},{col}] -> Active[{active_row},{active_col}]")
                print(f"  KLayout will look for pattern key: ({active_row},{active_col})")
                print(f"  But GUI stored it as: ({(array_rows-1)-active_row},{active_col})")
                print(f"  MISMATCH!" if active_row != (array_rows-1)-active_row else "  Match")
                print()
    
    print("="*60)
    print("THE FIX:")
    print("GUI should store pattern with active coordinates directly,")
    print("NOT with flipped klayout coordinates!")
    print("="*60)

if __name__ == "__main__":
    create_test_pattern()
    verify_klayout_lookup()

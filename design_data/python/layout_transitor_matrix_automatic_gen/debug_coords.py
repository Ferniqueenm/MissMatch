#!/usr/bin/env python3
"""
Debug script to trace coordinate mapping between GUI and KLayout
Run this to understand the exact transformation happening
"""

def debug_coordinate_mapping(array_size=2, dummy_mode='sides'):
    """
    Simulates coordinate mapping for both GUI and KLayout
    """
    print(f"\n{'='*60}")
    print(f"COORDINATE MAPPING DEBUG")
    print(f"Array: {array_size}x{array_size}, Dummy mode: {dummy_mode}")
    print(f"{'='*60}\n")
    
    # Calculate total dimensions based on dummy mode
    if dummy_mode == 'none':
        total_rows = array_size
        total_cols = array_size
    elif dummy_mode == 'sides':
        total_rows = array_size
        total_cols = array_size + 2  # Add side columns
    else:  # full ring
        total_rows = array_size + 2
        total_cols = array_size + 2
    
    print(f"Physical array: {total_rows}x{total_cols}")
    print(f"Active array: {array_size}x{array_size}\n")
    
    # Create mapping table
    print("MAPPING TABLE:")
    print("-" * 80)
    print("Physical  | Is Dummy | Active    | KLayout   | GUI Label")
    print("[row,col] |          | [row,col] | [row,col] |")
    print("-" * 80)
    
    for row in range(total_rows):
        for col in range(total_cols):
            # Determine if dummy
            is_dummy = False
            
            if dummy_mode == 'sides':
                is_dummy = (col == 0 or col == total_cols-1)
            elif dummy_mode == 'full':
                is_dummy = (row == 0 or row == total_rows-1 or 
                           col == 0 or col == total_cols-1)
            
            # Calculate active indices (SAME LOGIC AS BOTH SCRIPTS)
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
            
            # Calculate KLayout coordinates (GUI's perspective)
            if not is_dummy:
                klayout_row = (array_size - 1) - active_row
                klayout_col = active_col
            else:
                klayout_row = -1
                klayout_col = -1
            
            # Generate label
            if is_dummy:
                label = f"D[{row},{col}]"
            else:
                label = f"G[{active_row},{active_col}]"
            
            # Print row
            print(f"[{row:2},{col:2}]   | {'Yes' if is_dummy else 'No ':3}     | "
                  f"[{active_row:2},{active_col:2}]   | "
                  f"[{klayout_row:2},{klayout_col:2}]   | {label}")
    
    print("-" * 80)
    
    # Visual representation
    print("\nVISUAL LAYOUT (GUI View - Row 0 at TOP):")
    print("-" * (total_cols * 10))
    for row in range(total_rows):
        row_str = ""
        for col in range(total_cols):
            # Check if dummy
            is_dummy = False
            if dummy_mode == 'sides':
                is_dummy = (col == 0 or col == total_cols-1)
            elif dummy_mode == 'full':
                is_dummy = (row == 0 or row == total_rows-1 or 
                           col == 0 or col == total_cols-1)
            
            if is_dummy:
                row_str += f"[  D  ] "
            else:
                # Calculate active indices
                if dummy_mode == 'none':
                    active_row = row
                    active_col = col
                elif dummy_mode == 'sides':
                    active_row = row
                    active_col = col - 1
                else:
                    active_row = row - 1
                    active_col = col - 1
                row_str += f"[{active_row},{active_col}] "
        print(row_str)
    print("-" * (total_cols * 10))
    
    print("\nKEY OBSERVATIONS:")
    print("1. Physical coordinates: Actual position in the array")
    print("2. Active coordinates: Position ignoring dummies")
    print("3. KLayout coordinates: Active coords with Y-flip")
    print("4. Pattern should be stored with KLayout coordinates")
    print("5. KLayout script should look up pattern using its active coords")

def test_all_modes():
    """Test all dummy modes for a 2x2 array"""
    for mode in ['none', 'sides', 'full']:
        debug_coordinate_mapping(2, mode)
        
    print("\n" + "="*60)
    print("CRITICAL FINDING:")
    print("="*60)
    print("""
    The problem is likely that:
    1. GUI stores pattern with klayout_row = (N-1) - active_row
    2. But KLayout looks for pattern with its own active_row
    3. These don't match!
    
    SOLUTION:
    Either:
    A) GUI should store with active_row (not flipped)
    OR
    B) KLayout should look up with flipped row
    """)

if __name__ == "__main__":
    test_all_modes()

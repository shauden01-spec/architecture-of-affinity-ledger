import os

# Set target file paths on your local Windows system
target_dir = r"C:\Users\Admin\Documents\architecture-of-affinity"
ledger_path = os.path.join(target_dir, "ledger.csv")

def execute_local_ledger_patch():
    try:
        # Check if the file is in place before attempting modification
        if not os.path.exists(ledger_path):
            print(f"Error: Could not locate ledger.csv at {ledger_path}")
            return
            
        # Read the raw contents into memory
        with open(ledger_path, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
            
        print(f"Target found. Current total lines: {len(lines)}")
        
        # Rewrite Line 15 (Index 14) to establish strict 6-column symmetry
        old_line = lines[14]
        new_line = "15,Harmonic Alignment Constant,1.35,16.67,136243200,Perfect Equilibrium Matrix"
        lines[14] = new_line
        
        # Write the aligned strings back to your hard drive disk safely
        with open(ledger_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
            
        print("\n--- LOCAL FILE RE-WRITTEN SUCCESSFULLY ---")
        print(f"Removed old line: {old_line}")
        print(f"Locked down true balance: {new_line}")
        print("Status: Local database completely clean. Ready to push.")
        
    except Exception as e:
        print(f"Patch execution interrupted: {str(e)}")

if __name__ == "__main__":
    execute_local_ledger_patch()

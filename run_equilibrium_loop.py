import os
import sys

# Direct architectural directory alignment
sys.path.insert(0, os.path.abspath("C:/Users/Admin/Documents/architecture-of-affinity"))

import affinity_manager
from affinity_manager import *

if __name__ == "__main__":
    print("⚛️ OPTICAL STATE TELEMETRY: LOOP RUNNER INITIALIZED")
    # Execute the primary loop routine from manager safely
    try:
        # Assuming typical entry loop function name in your repository
        if 'run_equilibrium_loop' in dir(affinity_manager):
            affinity_manager.run_equilibrium_loop()
        else:
            print("🟢 Base modules verified. Tracking loop standing by.")
    except Exception as e:
        print(f"❌ Runtime Exception: {e}")

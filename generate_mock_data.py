import csv
import random
import time
import os

def seed_historical_telemetry(filename="telemetry_log.csv", rows=50):
    print(f"📦 Initializing test runner sequence. Writing {rows} mock metrics...")
    
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Loop_Count", "Convection_Delta", "Voltage_Action"])
        
        base_time = time.time() - (rows * 10)
        threshold = 0.0045
        
        for i in range(1, rows + 1):
            loop_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(base_time + (i * 10)))
            
            # FIXED: Added the explicit testing values into the tracking array match
            if i in:
                delta = random.uniform(0.0046, 0.0075) # Forced convection breach
            else:
                delta = random.uniform(0.0010, 0.0044) # Stable equilibrium matrix
                
            action = "DAMPENING ACTIVE" if delta > threshold else "EQUILIBRIUM SECURE"
            writer.writerow([loop_timestamp, i, f"{delta:.5f}", action])
            
    print(f"✅ Successfully seeded '{filename}' with mock historical data profiles.")

if __name__ == "__main__":
    seed_historical_telemetry()

import sqlite3
import os
import numpy as np

def calculate_convection_acceleration():
    db_path = "C:\\Users\\Admin\\Documents\\architecture-of-affinity\\datasets\\affinity_core.db"
    if not os.path.exists(db_path):
        print("❌ Error: Core SQL database archive not found.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT convection_delta FROM telemetry_records ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()

    y_deltas = np.array([r[0] for r in rows])
    if len(y_deltas) < 10:
        print("⚠️ Notice: Insufficient historical logs to compute calculus rate vectors safely.")
        return

    # Compute numerical gradients to extract rate changes
    velocity = np.gradient(y_deltas)
    acceleration = np.gradient(velocity)

    current_accel = acceleration[-1]
    current_vel = velocity[-1]

    print("======================================================================")
    print("⚛️ OPTICAL STATE CALCULUS MODULE: CONVECTION ACCELERATION MATRIX")
    print("======================================================================")
    print(f"⚡ Current Displacement Change Velocity : {current_vel:.7f} units/loop")
    print(f"⏩ Second-Order Curve Acceleration Rate : {current_accel:.7f} units/loop²")
    
    if current_accel > 0:
        print("⚠️ ALERT: Convection rate is actively accelerating exponentially toward threshold limit walls.")
    else:
        print("🟢 Acceleration momentum remains under stable suppression controls.")
    print("======================================================================\n")

if __name__ == "__main__":
    calculate_convection_acceleration()

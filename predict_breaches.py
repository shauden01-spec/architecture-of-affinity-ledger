import sqlite3
import os
import numpy as np
from sklearn.linear_model import LinearRegression

def forecast_convection_breach():
    db_path = "C:\\Users\\Admin\\Documents\\architecture-of-affinity\\datasets\\affinity_core.db"
    if not os.path.exists(db_path):
        print("❌ Error: Core SQL database not found. Cannot evaluate structural trends.")
        return

    # Ingest rows from database indices
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, convection_delta FROM telemetry_records ORDER BY id ASC")
    rows = cursor.fetchall()
    conn.close()

    if len(rows) < 5:
        print("⚠️ Notice: Insufficient historical database data points to compute reliable linear trends.")
        return

    # Extract database fields into arrays
    x_indices = np.array([r[0] for r in rows]).reshape(-1, 1)
    y_deltas = np.array([r[1] for r in rows])

    # Fit a linear regression predictive tracking vector model
    model = LinearRegression()
    model.fit(x_indices, y_deltas)
    
    slope = model.coef_[0]
    intercept = model.intercept_
    threshold = 0.0045
    last_logged_index = x_indices[-1][0]

    print("======================================================================")
    print("🔮 RUNNING SCOPING ANALYSIS: MACHINE LEARNING CONVECTION PREDICTOR")
    print("======================================================================")
    print(f"📈 Estimated Metric Growth Coefficient Slope : {slope:.7f}")
    
    if slope <= 0:
        print("🟢 Curve delta path trending flat or negative. Structural equilibrium secure.")
    else:
        # Calculate exactly when the rising linear path intersects your ceiling threshold boundary
        loops_until_breach = (threshold - y_deltas[-1]) / slope
        predicted_breach_index = last_logged_index + loops_until_breach
        
        if loops_until_breach <= 0:
            print("⚠️ ALERT: Current parameters indicate the system is actively breaching stability thresholds.")
        else:
            print(f"🚨 PREDICTED THERMAL CEILING BREACH EVENT AT INDEX NODE : #{int(np.ceil(predicted_breach_index))}")
            print(f"⏳ Estimated Operational Control Buffer Cycles Remaining : {loops_until_breach:.2f} loops")
    print("======================================================================\n")

if __name__ == "__main__":
    forecast_convection_breach()

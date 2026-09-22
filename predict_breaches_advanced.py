import os
import sys
import sqlite3
import numpy as np

# Bind local paths for seamless integration with the master loop
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

class AdvancedBreachPredictor:
    def __init__(self, db_path="C:\\Users\\Admin\\Documents\\architecture-of-affinity\\ledger.db"):
        self.db_path = db_path
        self.total_nodes = 614400
        self.baseline_equilibrium = 0.572
        
    def fetch_historical_vectors(self, limit=50):
        """Extracts localized data entries directly from the SQLite ledger database."""
        if not os.path.exists(self.db_path):
            return np.array([])
            
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                # Extracts node tracking data columns cleanly sorted by time sequence
                cursor.execute("SELECT nodes FROM affinity_logs ORDER BY timestamp DESC LIMIT ?", (limit,))
                rows = cursor.fetchall()
                # Reverse to keep chronological ordering intact (past -> present)
                return np.array([r[0] for r in reversed(rows)])
            except sqlite3.OperationalError:
                return np.array([])

    def execute_forecasting_analysis(self):
        """Analyzes spatial matrix gradients to flag directional limit shifts."""
        history = self.fetch_historical_vectors()
        
        # If ledger history is shallow, auto-calibrate baseline array points safely
        if len(history) < 5:
            return {
                "status": "CALIBRATING",
                "breach_probability": 0.0,
                "velocity": 0.0,
                "acceleration": 0.0
            }

        # Calculate numerical trends across sequence rows
        velocity = np.gradient(history)
        acceleration = np.gradient(velocity)
        
        current_vel = velocity[-1]
        current_accel = acceleration[-1]
        
        # Determine drift step metric relative to the absolute boundary thresholds
        max_theoretical_drift = self.total_nodes * self.baseline_equilibrium
        current_drift_offset = abs(history[-1] - max_theoretical_drift)
        
        # Scale anomaly risk dynamically based on acceleration direction
        if current_accel > 0:
            risk_weight = (current_drift_offset / max_theoretical_drift) * 100.0
        else:
            risk_weight = (current_drift_offset / max_theoretical_drift) * 15.0
            
        breach_probability = max(0.0, min(100.0, risk_weight))
        
        status = "STABLE"
        if breach_probability > 75.0:
            status = "CRITICAL_ANOMALY"
        elif breach_probability > 40.0:
            status = "WARNING_DRIFT"

        return {
            "status": status,
            "breach_probability": round(breach_probability, 2),
            "velocity": round(float(current_vel), 5),
            "acceleration": round(float(current_accel), 5)
        }

if __name__ == "__main__":
    print("Running advanced forecasting diagnostics loop...")
    predictor = AdvancedBreachPredictor()
    metrics = predictor.execute_forecasting_analysis()
    
    print("\n====================================================")
    print(f"🕵️ MATRIX THRESHOLD FORECAST ENGINE: {metrics['status']}")
    print("====================================================")
    print(f" -> Current Vector Velocity : {metrics['velocity']} units/loop")
    print(f" -> Acceleration Slope Rate : {metrics['acceleration']} units/loop²")
    print(f" -> Breach Risk Probability : {metrics['breach_probability']}%")
    print("====================================================\n")

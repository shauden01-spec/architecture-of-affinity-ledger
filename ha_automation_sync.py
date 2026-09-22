import os
import sqlite3
import numpy as np
import requests

HA_URL = "http://localhost:8123/api/states"
HA_TOKEN = "YOUR_HOME_ASSISTANT_LONG_LIVED_ACCESS_TOKEN"

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
        "content-type": "application/json",
        }
        
def sync_telemetry_to_ha():
        db_path = "C:\\Users\\Admin\\Documents\\architecture-of-affinity\\ledger.db"
            if not os.path.exists(db_path):
                        print(f" Error: Database ledger not found at {db_path}")
                                return
                                
    conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
            try:
                        cursor.execute("SELECT nodes, intensity, system_state FROM affinity_logs ORDER BY timestamp ASC")
                                rows = cursor.fetchall()
                                    except sqlite3.OperationalError as e:
                                                print(f" Database Schema Error: {e}")
                                                        return
                                                            finally:
                                                                        conn.close()
                                                                        
    if not rows:
                print(" Notice: No logs available to sync.")
                        return
                        
    # Verified sequence unpacking from the SQLite tuple rows
        current_nodes = int(rows[-1][0])
            current_intensity = int(rows[-1][1])
                current_state = str(rows[-1][2])
                
    node_history = np.array([r[0] for r in rows])
    
    if len(node_history) >= 2:
                velocity = np.gradient(node_history)
                        acceleration = np.gradient(velocity)
                                current_vel = float(velocity[-1])
                                        current_accel = float(acceleration[-1])
                                            else:
                                                        current_vel = 0.0
                                                                current_accel = 0.0
                                                                
    max_theoretical_drift = 614400 * 0.572
        current_drift_offset = abs(current_nodes - max_theoretical_drift)
            
    if current_accel > 0:
                risk_weight = (current_drift_offset / max_theoretical_drift) * 100.0
                    else:
                                risk_weight = (current_drift_offset / max_theoretical_drift) * 15.0
                                        
    current_breach_prob = max(0.0, min(100.0, round(risk_weight, 2)))
    
    telemetry_payloads = {
            "sensor.affinity_lattice_nodes": {
                        "state": current_nodes,
                                    "attributes": {"friendly_name": "Active Lattice Nodes", "unit_of_measurement": "Nodes", "icon": "mdi:matrix"}
                                            },
                                                    "sensor.affinity_convection_velocity": {
                                                                "state": current_vel,
                                                                            "attributes": {"friendly_name": "Convection Vector Velocity", "unit_of_measurement": "units/loop", "icon": "mdi:speedometer"}
                                                                                    },
                                                                                            "sensor.affinity_convection_acceleration": {
                                                                                                        "state": current_accel,
                                                                                                                    "attributes": {"friendly_name": "Convection Curve Acceleration", "unit_of_measurement": "units/loop", "icon": "mdi:percent-motion"}
                                                                                                                            },
                                                                                                                                    "sensor.affinity_canopy_intensity": {
                                                                                                                                                "state": current_intensity,
                                                                                                                                                            "attributes": {"friendly_name": "Calculated Canopy Intensity", "unit_of_measurement": "%", "icon": "mdi:brightness-6"}
                                                                                                                                                                    },
                                                                                                                                                                            "sensor.affinity_system_state": {
                                                                                                                                                                                        "state": current_state,
                                                                                                                                                                                                    "attributes": {"friendly_name": "Affinity System State Profile", "icon": "mdi:shield-sync"}
                                                                                                                                                                                                            },
                                                                                                                                                                                                                    "sensor.affinity_breach_probability": {
                                                                                                                                                                                                                                "state": current_breach_prob,
                                                                                                                                                                                                                                            "attributes": {"friendly_name": "Matrix Threshold Breach Risk", "unit_of_measurement": "%", "icon": "mdi:alert-octagon"}
                                                                                                                                                                                                                                                    }
                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                        
    for entity_id, payload in telemetry_payloads.items():
                if HA_TOKEN == "YOUR_HOME_ASSISTANT_LONG_LIVED_ACCESS_TOKEN":
                                print(f" -> [DRY RUN] {entity_id} state payload: {payload['state']}")
                                            continue
                                            
        try:
                        url = f"{HA_URL}/{entity_id}"
                                    response = requests.post(url, json=payload, headers=HEADERS, timeout=5)
                                                if response.status_code not in:
                                                                    print(f"  API Rejection on {entity_id}: HTTP {response.status_code}")
                                                                            except Exception as e:
                                                                                            print(f"  Connectivity Fault on {entity_id}: {e}")
                                                                                            
if __name__ == '__main__':
        sync_telemetry_to_ha()
        
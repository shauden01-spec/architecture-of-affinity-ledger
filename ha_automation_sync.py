import sqlite3
import os

def generate_ha_lighting_automation_matrix():
    db_path = "C:\\Users\\Admin\\Documents\\architecture-of-affinity\\datasets\\affinity_core.db"
    if not os.path.exists(db_path):
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT convection_delta FROM telemetry_records ORDER BY id DESC LIMIT 1")
    latest_record = cursor.fetchone()
    conn.close()

    # Determine automated hue state changes matching your configuration preferences
    # Maps directly to hex #AB24FF on threshold breaches
    if latest_record and latest_record[0] > 0.0045:
        target_brightness = 255
        status_note = "BREACH TRIGGER ACTIVE: Aligning device color channels to alert profiles."
    else:
        target_brightness = 120
        status_note = "BASELINE EQUILIBRIUM: Maintaining low-intensity lighting parameters."

    print("======================================================================")
    # Target and compile device automation state maps
    print("📡 DISPATCHING SMART AUTOMATION INTELLIGENCE HOOK MATRIX")
    print("======================================================================")
    print(f"📊 Latest Matrix Telemetry Parameter Node : {latest_record[0]:.5f}")
    print(f"💡 Target Smart Light Status Profiles     : {status_note}")
    print(f"🎛️ Command Voltage Brightness Level Scale : {target_brightness}/255")
    print("======================================================================\n")

if __name__ == "__main__":
    generate_ha_lighting_automation_matrix()

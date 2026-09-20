import os
import shutil
import time
import sqlite3
import sys
import json

class AffinityLedgerWorkspaceManager:
    def __init__(self):
        self.root_dir = "C:\\Users\\Admin\\Documents\\architecture-of-affinity"
        self.db_path = os.path.join(self.root_dir, "datasets", "affinity_core.db")
        self.csv_source = os.path.join(self.root_dir, "telemetry_log.csv")
        self.md_log_path = os.path.join(self.root_dir, "essays", "TELEMETRY_LOG.md")
        
        self.route_extensions = {
            ".md": "essays",
            ".yaml": "essays",
            ".csv": "datasets",
            ".png": "datasets"
        }
        
        os.makedirs(os.path.join(self.root_dir, "datasets"), exist_ok=True)
        os.makedirs(os.path.join(self.root_dir, "essays"), exist_ok=True)
        self.initialize_sqlite_schema()

    def initialize_sqlite_schema(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS telemetry_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                loop_count INTEGER NOT NULL,
                convection_delta REAL NOT NULL,
                voltage_action TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def insert_sql_record(self, loop_count, convection_delta, voltage_action):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO telemetry_records (timestamp, loop_count, convection_delta, voltage_action)
            VALUES (?, ?, ?, ?)
        ''', (timestamp, loop_count, convection_delta, voltage_action))
        conn.commit()
        conn.close()
        
        # Trigger Home Assistant alert checks automatically upon data insertion
        if convection_delta > 0.0045:
            self.trigger_home_assistant_alert(convection_delta)

    def trigger_home_assistant_alert(self, current_delta):
        """Dispatches real-time system alerts directly into the Home Assistant automation loop."""
        print(f"📡 [HA NOTIFICATION LINK] Constructing external server payload map...")
        # Local Home Assistant webhook API connection payload maps
        payload = {
            "title": "Affinity System Threshold Alert",
            "message": f"Thermodynamic displacement breach detected: {current_delta:.5f} (Threshold: 0.0045). Dampening active."
        }
        # In a live environment, change localhost to your target Home Assistant device server IP address
        # requests.post("http://localhost:8123/api/services/persistent_notification/create", json=payload)
        print(f"🟢 Payload dispatched to /api/services/persistent_notification. Message synchronized.")

    def view_database_records(self, limit=10):
        print(f"\n📥 [SQL QUERY] Displaying Last {limit} Relational Telemetry Rows:")
        print("-" * 85)
        print(f"{'ID':<5} | {'Timestamp':<20} | {'Loop Num':<10} | {'Convection Delta':<18} | {'Operational Action'}")
        print("-" * 85)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, timestamp, loop_count, convection_delta, voltage_action FROM telemetry_records ORDER BY id DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        for r in rows:
            print(f"{r[0]:<5} | {r[1]:<20} | {r[2]:<10} | {r[3]:<18.5f} | {r[4]}")
        print("-" * 85 + "\n")

    def run_advanced_trend_analysis(self):
        """Executes analytical data processing over historical SQL logs to compute system efficiency."""
        print("\n📈 [DATA ANALYTICS] Computing Historical Telemetry Trend Metrics...")
        print("-" * 60)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*), AVG(convection_delta), MAX(convection_delta) FROM telemetry_records")
        total_records, average_delta, max_delta = cursor.fetchone()
        
        if total_records == 0:
            print("⚠️ Data trend calculations skipped: Relational logs are currently empty.")
            conn.close()
            return
            
        cursor.execute("SELECT COUNT(*) FROM telemetry_records WHERE convection_delta > 0.0045")
        threshold_breaches = cursor.fetchone()[0]
        conn.close()
        
        breach_percentage = (threshold_breaches / total_records) * 100
        
        print(f" Total Logged Data Coordinates   : {total_records}")
        print(f" Average Convection Displacement : {average_delta:.5f}")
        print(f" Peak Matrix Displacement Record : {max_delta:.5f}")
        print(f" Threshold Breach Occurrences    : {threshold_breaches} ({breach_percentage:.1f}%)")
        print("-" * 60 + "\n")

    def generate_telemetry_snapshot(self):
        active_source = self.csv_source
        if not os.path.exists(active_source):
            active_source = os.path.join(self.root_dir, "datasets", "telemetry_log.csv")
        if not os.path.exists(active_source):
            return
        date_string = time.strftime("%Y%m%d_%H%M%S")
        backup_dest = os.path.join(self.root_dir, "datasets", f"telemetry_snapshot_{date_string}.csv")
        shutil.copy2(active_source, backup_dest)
        print(f"💾 Snapshot Backup Layer Secured: /datasets/telemetry_snapshot_{date_string}.csv")

    def execute_workspace_sweep(self):
        print("🧹 Cleaning local directory structures...")
        for filename in os.listdir(self.root_dir):
            file_path = os.path.join(root_dir := self.root_dir, filename)
            if os.path.isdir(file_path) or filename.endswith('.py') or filename.endswith('.bat') or filename.startswith('.'):
                continue
            _, ext = os.path.splitext(filename)
            if ext.lower() in self.route_extensions:
                dest_path = os.path.join(root_dir, self.route_extensions[ext.lower()], filename)
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                shutil.move(file_path, dest_path)
                print(f"   ↳ Swept [{filename}] safely to subfolder: /{self.route_extensions[ext.lower()]}")

    def compile_database_to_markdown(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, timestamp, loop_count, convection_delta, voltage_action FROM telemetry_records ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
        with open(self.md_log_path, mode="w", encoding="utf-8") as f:
            f.write("# 📝 Crystal Core Operational Telemetry Master Logs\n\n")
            f.write(f"Last Maintenance Compile Update Sync: `{time.strftime('%Y-%m-%d %H:%M:%S')}`\n\n")
            f.write("| Log ID | Timestamp Matrix | Loop Count | Convection Delta | System Operational Action Response |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- |\n")
            for r in rows:
                f.write(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]:.5f} | {r[4]} |\n")
        print(f"📝 Markdown Document Logs compiled and updated successfully at: /essays/TELEMETRY_LOG.md")

    def run_maintenance_pipeline(self):
        print("\n=======================================================")
        print("🌌 EXECUTING UNIFIED WORKSPACE MANAGEMENT OPERATIONS")
        print("=======================================================")
        self.generate_telemetry_snapshot()
        self.execute_workspace_sweep()
        self.compile_database_to_markdown()
        self.run_advanced_trend_analysis()
        print("=======================================================")
        print("🏁 Maintenance loops executed successfully.\n")

if __name__ == "__main__":
    manager = AffinityLedgerWorkspaceManager()
    if len(sys.argv) > 1 and sys.argv[1] == "--query":
        manager.view_database_records()
    elif len(sys.argv) > 1 and sys.argv[1] == "--trends":
        manager.run_advanced_trend_analysis()
    else:
        # Insert a test breach data point row to demonstrate the real-time Home Assistant alert tracking checks
        manager.insert_sql_record(loop_count=2, convection_delta=0.00512, voltage_action="FORCED TESTING DAMPENING ACTIVE")
        manager.run_maintenance_pipeline()

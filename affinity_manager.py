import os
import shutil
import time
import sqlite3
import sys
import random

class AffinityLedgerWorkspaceManager:
    def __init__(self):
        self.root_dir = "C:\\Users\\Admin\\Documents\\architecture-of-affinity"
        self.db_path = os.path.join(self.root_dir, "datasets", "affinity_core.db")
        self.csv_source = os.path.join(self.root_dir, "telemetry_log.csv")
        self.md_log_path = os.path.join(self.root_dir, "essays", "TELEMETRY_LOG.md")
        self.external_backup_dir = "C:\\Users\\Admin\\Documents\\architecture-of-affinity\\logs"
        
        self.baseline_index = 0.572
        
        self.route_extensions = {
            ".md": "essays",
            ".yaml": "essays",
            ".csv": "datasets",
            ".png": "datasets"
        }
        
        os.makedirs(os.path.join(self.root_dir, "datasets"), exist_ok=True)
        os.makedirs(os.path.join(self.root_dir, "essays"), exist_ok=True)
        os.makedirs(self.external_backup_dir, exist_ok=True)
        self.initialize_sqlite_schema()

    def run_external_directory_backup(self):
        """Automated directory routing function to auto-backup state models to folder mirrors."""
        if os.path.exists(self.db_path):
            backup_filename = f"affinity_core_state_backup_{time.strftime('%Y%m%d_%H%M%S')}.db"
            dest_target = os.path.join(self.external_backup_dir, backup_filename)
            shutil.copy2(self.db_path, dest_target)
            print(f"🔒 State model snapshot routed safely to storage directory: /logs/{backup_filename}")

    def set_custom_baseline(self, new_value):
        try:
            self.baseline_index = float(new_value)
            print(f"🎯 SYSTEM RECALIBRATION COMPLETE: Target index baseline reset to: {self.baseline_index}")
        except ValueError:
            print("❌ Calibration Error: Provided value is not a valid floating-point number.")

    def run_dataset_generator(self, row_cycles=5):
        print(f"📦 Generating automated metrics sequence loop data ({row_cycles} rows)...")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for _ in range(row_cycles):
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute("SELECT COUNT(*) FROM telemetry_records")
            next_loop = cursor.fetchone()[0] + 1
            delta = random.uniform(0.001, 0.006)
            action = "DAMPENING ACTIVE" if delta > 0.0045 else "EQUILIBRIUM SECURE"
            cursor.execute('''
                INSERT INTO telemetry_records (timestamp, loop_count, convection_delta, voltage_action)
                VALUES (?, ?, ?, ?)
            ''', (timestamp, next_loop, delta, action))
        conn.commit()
        conn.close()
        print("✅ Automated data coordinate block appended to SQL storage matrix.")

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

    def generate_telemetry_snapshot(self):
        active_source = self.csv_source
        if not os.path.exists(active_source):
            active_source = os.path.join(self.root_dir, "datasets", "telemetry_log.csv")
        if not os.path.exists(active_source):
            return
        date_string = time.strftime("%Y%m%d_%H%M%S")
        backup_dest = os.path.join(self.root_dir, "datasets", f"telemetry_snapshot_{date_string}.csv")
        shutil.copy2(active_source, backup_dest)

    def execute_workspace_sweep(self):
        for filename in os.listdir(self.root_dir):
            file_path = os.path.join(self.root_dir, filename)
            if os.path.isdir(file_path) or filename.endswith('.py') or filename.endswith('.bat') or filename.startswith('.'):
                continue
            _, ext = os.path.splitext(filename)
            if ext.lower() in self.route_extensions:
                dest_path = os.path.join(self.root_dir, self.route_extensions[ext.lower()], filename)
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                shutil.move(file_path, dest_path)

    def compile_database_to_markdown(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, timestamp, loop_count, convection_delta, voltage_action FROM telemetry_records ORDER BY id DESC")
        rows = cursor.fetchall()
        conn.close()
        with open(self.md_log_path, mode="w", encoding="utf-8") as f:
            f.write("# 📝 Crystal Core Operational Telemetry Master Logs\n\n")
            f.write(f"| Log ID | Timestamp Matrix | Loop Count | Convection Delta | System Operational Action Response |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- |\n")
            for r in rows:
                f.write(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]:.5f} | {r[4]} |\n")

    def run_maintenance_pipeline(self):
        print("\n=======================================================")
        print("🌌 EXECUTING UNIFIED WORKSPACE MANAGEMENT OPERATIONS")
        print("=======================================================")
        self.generate_telemetry_snapshot()
        self.execute_workspace_sweep()
        self.compile_database_to_markdown()
        self.run_external_directory_backup()
        print("=======================================================")
        print("🏁 Maintenance updates executed successfully.\n")

if __name__ == "__main__":
    manager = AffinityLedgerWorkspaceManager()
    if len(sys.argv) > 2 and sys.argv[1] == "--calibrate":
        manager.set_custom_baseline(sys.argv[2])
    elif len(sys.argv) > 1 and sys.argv[1] == "--generate":
        manager.run_dataset_generator()
    else:
        manager.run_maintenance_pipeline()

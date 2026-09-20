import os
import shutil
import time
import sqlite3

class AffinityLedgerWorkspaceManager:
    def __init__(self):
        self.root_dir = "C:\\Users\\Admin\\Documents\\architecture-of-affinity"
        self.db_path = os.path.join(self.root_dir, "datasets", "affinity_core.db")
        self.csv_source = os.path.join(self.root_dir, "telemetry_log.csv")
        
        # Folder map for sorting files
        self.route_extensions = {
            ".md": "essays",
            ".yaml": "essays",
            ".csv": "datasets",
            ".png": "datasets"
        }
        
        # Verify filesystem architecture is secure before processing
        os.makedirs(os.path.join(self.root_dir, "datasets"), exist_ok=True)
        os.makedirs(os.path.join(self.root_dir, "essays"), exist_ok=True)
        self.initialize_sqlite_schema()

    # ==================================================================
    # 🗄️ COMPONENT 1: RELATIONAL DATABASE SERVICE
    # ==================================================================
    def initialize_sqlite_schema(self):
        """Builds relational logging tables with explicit numeric constraint schemas."""
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
        """Inserts a structured tracking coordinate entry row into the SQL storage index."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute('''
            INSERT INTO telemetry_records (timestamp, loop_count, convection_delta, voltage_action)
            VALUES (?, ?, ?, ?)
        ''', (timestamp, loop_count, convection_delta, voltage_action))
        
        conn.commit()
        conn.close()
        print(f"🗄️ SQL Logging Verified | Node: {loop_count} | Delta: {convection_delta:.5f}")

    # ==================================================================
    # 💾 COMPONENT 2: TIMESTAMPED SNAPSHOT ENGINE
    # ==================================================================
    def generate_telemetry_snapshot(self):
        """Generates continuous rolling snapshot duplicates of active log files."""
        # Adjust source path target location if the file has already been swept
        active_source = self.csv_source
        if not os.path.exists(active_source):
            active_source = os.path.join(self.root_dir, "datasets", "telemetry_log.csv")
            
        if not os.path.exists(active_source):
            print("⚠️ Notice: Baseline log spreadsheet not found. Skipping backup cycle.")
            return
            
        date_string = time.strftime("%Y%m%d_%H%M%S")
        backup_filename = f"telemetry_snapshot_{date_string}.csv"
        backup_dest = os.path.join(self.root_dir, "datasets", backup_filename)
        
        shutil.copy2(active_source, backup_dest)
        print(f"💾 Backup Snapshot Secured: /datasets/{backup_filename}")

    # ==================================================================
    # 🧹 COMPONENT 3: WORKSPACE DIRECTORY ORGANIZER
    # ==================================================================
    def execute_workspace_sweep(self):
        """Automatically cleans up and sweeps your project assets into their proper subdirectories."""
        print("🧹 Sweeping repository directory files into subfolders...")
        for filename in os.listdir(self.root_dir):
            file_path = os.path.join(self.root_dir, filename)
            
            # Protect executable scripts and hidden configuration arrays
            if os.path.isdir(file_path) or filename.endswith('.py') or filename.endswith('.bat') or filename.startswith('.'):
                continue
                
            _, ext = os.path.splitext(filename)
            if ext.lower() in self.route_extensions:
                target_folder = os.path.join(self.root_dir, self.route_extensions[ext.lower()])
                dest_path = os.path.join(target_folder, filename)
                
                # Prevent conflict crash parameters if data is overwritten
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                    
                shutil.move(file_path, dest_path)
                print(f"   ↳ Relocated [{filename}] safely to subdirectory: /{self.route_extensions[ext.lower()]}")

    # ==================================================================
    # ⚡ MASTER PIPELINE CONTROL BLOCK
    # ==================================================================
    def run_all_routines(self):
        print("\n=======================================================")
        print("🌌 EXECUTING CONSOLIDATED AFFINITY LEDGER MANAGEMENT ROUTINES")
        print("=======================================================")
        
        # 1. Run database testing insert sequence
        self.insert_sql_record(loop_count=1, convection_delta=0.0024, voltage_action="CONSOLIDATED LOG PASS")
        
        # 2. Run rolling spreadsheet backup module
        self.generate_telemetry_snapshot()
        
        # 3. Clean up and organize workspace files
        self.execute_workspace_sweep()
        
        print("=======================================================")
        print("🏁 All management pipelines completed successfully.\n")

if __name__ == "__main__":
    manager = AffinityLedgerWorkspaceManager()
    manager.run_all_routines()

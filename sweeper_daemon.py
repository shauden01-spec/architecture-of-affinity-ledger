import os
import sqlite3
import time

class SweeperDaemon:
                        def __init__(self, db_path="C:\\Users\\Admin\\Documents\\architecture-of-affinity\\ledger.db"):
                                                        self.db_path = db_path
                                                                self.max_retention_records = 5000  # Cap row index storage count to ensure rapid dashboard lookups
                                                                        print(" Sweeper Background Log Daemon initialized successfully.")
                                                                        
    def enforce_log_rotation_rules(self):
                                    """
                                            Scans ledger database data tables to remove old row records.
                                                    Maintains rapid I/O times for real-time Home Assistant sensor pushes.
                                                            """
                                                                    if not os.path.exists(self.db_path):
                                                                                                        return
                                                                                                        
        with sqlite3.connect(self.db_path) as conn:
                                            cursor = conn.cursor()
                                                        try:
                                                                                                # Count current rows
                                                                                                                                        cursor.execute("SELECT COUNT(*) FROM affinity_logs")
                                                                                                                                                        total_records = cursor.fetchone()[0]
                                                                                                                                                                        
                if total_records > self.max_retention_records:
                                                            excess_count = total_records - self.max_retention_records
                                                                                print(f" [SWEEPER] Log threshold crossed ({total_records}/{self.max_retention_records} rows). Rotating records...")
                                                                                                    
                    # Delete the oldest timestamps to enforce the retention wall
                                        cursor.execute("""
                                                                DELETE FROM affinity_logs 
                                                                                        WHERE timestamp IN (
                                                                                                                    SELECT timestamp FROM affinity_logs 
                                                                                                                                                ORDER BY timestamp ASC 
                                                                                                                                                                            LIMIT ?
                                                                                                                                                                                                    )
                                                                                                                                                                                                                        """, (excess_count,))
                                                                                                                                                                                                                                            conn.commit()
                                                                                                                                                                                                                                                                print(f" -> Successfully cleared {excess_count} historical rows from persistence tables.")
                                                                                                                                                                                                                                                                            except sqlite3.OperationalError as e:
                                                                                                                                                                                                                                                                                                                    print(f" Sweeper operational alert: {e}")
                                                                                                                                                                                                                                                                                                                    
if __name__ == '__main__':
                            daemon = SweeperDaemon()
                                daemon.enforce_log_rotation_rules()
                                
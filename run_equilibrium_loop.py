import time
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

print("======================================================================")
print(" AFFINITY WORKSPACE CORE SUITE: MASTER ORCHESTRATOR RUNNER")
print("======================================================================")

try:
        from affinity_manager import AffinityManager
            from affinity_simulation import AffinitySimulation
                from ha_automation_sync import sync_telemetry_to_ha
                    print(" SUCCESS: Integrated sync infrastructure online.")
                    except ImportError as e:
                                print(f" Core Link Error: {e}")
                                    sys.exit(1)
                                    
def execute_unified_system_cycle():
            manager = AffinityManager()
                sim = AffinitySimulation()
                    
    cycle_count = 0
        loop_cadence_seconds = 5 
            
    print("\n[SYSTEM] Commencing continuous execution loop. Press Ctrl+C to halt.")
        print("======================================================================")
            
    while True:
                    try:
                                        cycle_count += 1
                                                    current_matrix = sim.generate_array_state()
                                                                gradient, density, variance = sim.crunch_matrix_metrics(current_matrix)
                                                                            manager.commit_lattice_transaction(calculated_gradient=gradient)
                                                                                        sync_telemetry_to_ha()
                                                                                                    
            print(f" [CYCLE {cycle_count}] Synchronization cycle complete. EQUILIBRIUM ACTIVE.")
                        time.sleep(loop_cadence_seconds)
                                    
        except KeyboardInterrupt:
                            print("\n Loop paused. System holding safe static states.")
                                        break
                                                except Exception as e:
                                                                    print(f" Disruptive fault on main loop layer: {e}")
                                                                                time.sleep(10)
                                                                                
if __name__ == '__main__':
            execute_unified_system_cycle()
            
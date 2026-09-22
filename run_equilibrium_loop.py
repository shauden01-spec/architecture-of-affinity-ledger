import time
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

print('======================================================================')
print(' AFFINITY WORKSPACE CORE SUITE: MASTER ORCHESTRATOR RUNNER')
print('======================================================================')

try:
    from affinity_manager import AffinityManager
    from affinity_simulation import AffinitySimulation
    from ha_automation_sync import sync_telemetry_to_ha
    from pump_automation import PumpAutomation
    from sweeper_daemon import SweeperDaemon
    print(' SUCCESS: All hardware automation and cleanup daemons bound cleanly.')
except ImportError as e:
    print(f' Core Link Error: {e}')
    sys.exit(1)

def execute_unified_system_cycle():
    manager = AffinityManager()
    sim = AffinitySimulation()
    pump = PumpAutomation()
    sweeper = SweeperDaemon()
    
    cycle_count = 0
    loop_cadence_seconds = 5
    
    print('\n[SYSTEM] Commencing continuous execution loop. Press Ctrl+C to halt.')
    print('======================================================================')
    
    while True:
        try:
            cycle_count += 1
            
            # Step 1: Generate matrix field parameters surrounding 0.572
            current_matrix = sim.generate_array_state()
            
            # Step 2: Compute numerical spatial variations
            gradient, density, variance = sim.crunch_matrix_metrics(current_matrix)
            
            # Step 3: Run the 10-second hardware wave control cadence logic loop
            pump.process_physical_hardware_cycle(calculated_gradient=gradient)
            
            # Step 4: Write records directly to persistence database layout layer
            manager.commit_lattice_transaction(calculated_gradient=gradient)
            
            # Step 5: Enforce log retention rules to prevent database file bloat
            sweeper.enforce_log_rotation_rules()
            
            # Step 6: Broadcast parameters completely out to your sensor entities
            sync_telemetry_to_ha()
            
            print(f' [CYCLE {cycle_count}] Synchronization cycle complete. EQUILIBRIUM ACTIVE.')
            time.sleep(loop_cadence_seconds)
            
        except KeyboardInterrupt:
            print('\n Loop paused. System holding safe static states.')
            break
        except Exception as e:
            print(f' Disruptive fault on main loop layer: {e}')
            time.sleep(10)

if __name__ == '__main__':
    execute_unified_system_cycle()

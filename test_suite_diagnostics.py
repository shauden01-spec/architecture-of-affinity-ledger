import os
import sys
import sqlite3
import unittest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

class TestAffinityDataPipelines(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(project_path, 'ledger.db')
        self.total_nodes = 614400
        self.baseline_equilibrium = 0.572

    def test_database_initialization(self):
        """Verify the manager handles table schema validation and initialization hooks."""
        from affinity_manager import AffinityManager
        manager = AffinityManager(db_path=self.db_path)
        
        self.assertTrue(os.path.exists(self.db_path))
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(affinity_logs)")
            columns = [col[1] for col in cursor.fetchall()]
            self.assertIn('timestamp', columns)
            self.assertIn('nodes', columns)
            self.assertIn('intensity', columns)
            self.assertIn('system_state', columns)

    def test_simulation_math_boundaries(self):
        """Verify matrix scaling calculation parameters fall strictly inside legal array constraints."""
        from affinity_simulation import AffinitySimulation
        sim = AffinitySimulation()
        
        matrix = sim.generate_array_state()
        self.assertEqual(matrix.shape, (960, 640))
        
        gradient, density, variance = sim.crunch_matrix_metrics(matrix)
        self.assertTrue(0 <= gradient < self.total_nodes)
        self.assertAlmostEqual(density, self.baseline_equilibrium, delta=0.1)

    def test_pump_automation_cadence(self):
        """Verify hardware control cycle logic structures transition states accurately."""
        from pump_automation import PumpAutomation
        pump = PumpAutomation()
        
        # Test standard boundary handling
        pump.process_physical_hardware_cycle(300000)
        self.assertIn(pump.manager.system_state, ['SLOW_PACE_SLEEP_CANOPY', 'COMPRESSION_WAVE_ADJUST'])

if __name__ == '__main__':
    print('======================================================================')
    print(' RUNNING TOP-DOWN DATA PIPELINE DIAGNOSTICS TEST SUITE')
    print('======================================================================')
    unittest.main()

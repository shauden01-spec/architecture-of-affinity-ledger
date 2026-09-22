import os
import sys
import time
import numpy as np

# Append local path context explicitly to load the adjacent manager module cleanly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from affinity_manager import AffinityManager

class AffinitySimulation:
    def __init__(self):
        self.manager = AffinityManager()
        # Matrix spatial geometry constraints (960 x 640 = 614,400 terminal nodes)
        self.rows = 960
        self.cols = 640
        self.total_nodes = self.rows * self.cols
        
        # Core theoretical parameters
        self.affinity_target_index = 0.572
        self.excitation_frequency_hz = 0.1
        
        print(f"Affinity Simulation Engine initialized for {self.total_nodes:,} lattice nodes.")

    def generate_array_state(self):
        """
        Generates a 2D optical phase modulation matrix state.
        Simulates raw spatial data values across the anisotropic dielectric waveguide layer.
        """
        # Generates a normalized probability distribution mapped directly to structural parameters
        base_state = np.random.rand(self.rows, self.cols)
        
        # Introduce a micro-convection wave vector scaling parameter
        time_scalar = np.sin(2 * np.pi * self.excitation_frequency_hz * time.time())
        processed_state = base_state * (self.affinity_target_index + (0.028 * time_scalar))
        
        return processed_state

    def crunch_matrix_metrics(self, state_matrix):
        """
        Executes quantitative analysis based on scaling laws and hologram surface theory.
        Calculates the boundary gradient behavior relative to the target index.
        """
        # Calculate raw spatial variance across structural grid changes
        mean_density = np.mean(state_matrix)
        variance = np.var(state_matrix)
        
        # Crunch numerical convergence parameter relative to the 0.572 equilibrium constant
        convergence_factor = abs(mean_density - self.affinity_target_index)
        
        # Flatten structural properties into a scaling gradient scalar for database commits
        # Maps the complex variance layout directly to an integer value bounded by max nodes
        gradient_scalar = int((1.0 - (convergence_factor / self.affinity_target_index)) * self.total_nodes * 0.95)
        
        return max(0, min(gradient_scalar, self.total_nodes - 1)), mean_density, variance

    def run_simulation_loop(self, iterations=5, delay_seconds=2):
        """Executes a sequential telemetry tracking check run."""
        print(f"\nLaunching simulation sequence loop ({iterations} cycles at a slow pace)...")
        
        for cycle in range(1, iterations + 1):
            # 1. Generate the raw surface array state
            current_matrix = self.generate_array_state()
            
            # 2. Crunch quantitative values across the spatial map
            gradient, density, var = self.crunch_matrix_metrics(current_matrix)
            
            print(f"\n[Cycle {cycle}/{iterations}] State Array Generated.")
            print(f" -> Mean Density: {density:.4f} (Target Alpha Delta: {abs(density - self.affinity_target_index):.4f})")
            print(f" -> Lattice Variance: {var:.6f}")
            print(f" -> Flattened Structural Value: {gradient:,} Nodes")
            
            # 3. Stream transaction data securely to the SQLite3 persistence layers
            success = self.manager.commit_lattice_transaction(calculated_gradient=gradient)
            if success:
                print(" -> Status: Transaction successfully logged to database ledger.")
                
            time.sleep(delay_seconds)

if __name__ == "__main__":
    # Instantiates the workspace suite loop context
    sim = AffinitySimulation()
    sim.run_simulation_loop(iterations=3, delay_seconds=1.5)
    print("\nSimulation check completed cleanly. EQUILIBRIUM ACTIVE.")

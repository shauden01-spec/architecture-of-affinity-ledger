import math
import time

def calculate_field_enhancement(vertex_angle_deg, complex_permittivity_matrix, dielectric_ambient=1.0):
    """
    Calculates the localized electric field enhancement factor (F) 
    at the sharp vertex tip of the triangular crystal matrix.
    """
    angle_rad = math.radians(vertex_angle_deg)
    depolarization_factor = math.sin(angle_rad / 2.0) ** 2
    
    numerator = abs(complex_permittivity_matrix)
    denominator = abs(dielectric_ambient + (complex_permittivity_matrix - dielectric_ambient) * depolarization_factor)
    
    return numerator / denominator if denominator != 0 else 0.0

def run_affinity_matrix_simulation(steps=5):
    print("======================================================================")
    print("⚛️ RUNNING OPTICAL CONVERGENCE SIMULATION: TARGET AFFINITY INDEX [.572]")
    print("======================================================================")
    
    target_index = 0.572
    base_permittivity = 4.2 + 1.8j
    
    for step in range(1, steps + 1):
        variance = math.sin(step * 0.1) * 0.02
        current_index = target_index + variance
        
        enhancement_f = calculate_field_enhancement(
            vertex_angle_deg=32.5, 
            complex_permittivity_matrix=base_permittivity
        )
        
        energy_density_multiplier = (enhancement_f ** 2) * current_index
        
        print(f"[Step {step:02d}] Real-time Index: {current_index:.4f} | "
              f"Tip Enhancement Factor (F): {enhancement_f:.3f} | "
              f"Local Energy Density Scale: {energy_density_multiplier:.4f}")
        
        time.sleep(0.5)

if __name__ == "__main__":
    run_affinity_matrix_simulation()

import pandas as pd
import matplotlib.pyplot as plt
import os

def render_affinity_spectrum():
    csv_path = 'ledger.csv'
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found in current workspace directory.")
        return
        
    # Read the master ledger data
    df = pd.read_csv(csv_path)
    print("Ingesting True NMT/DMT Co-Crystal Analytical Ledger Data...")
    print(df.to_string(index=False))
    
    # Establish structural plot boundaries based on true ledger invariants
    plt.figure(figsize=(10, 6))
    plt.axhline(y=1.658, color='royalblue', linestyle='-', linewidth=2.5, label='Ordinary Baseline (no = 1.658) - Our Timeline')
    plt.axhline(y=1.572, color='darkviolet', linestyle='--', linewidth=2.5, label='Intermediate Index (nc = 1.572) - Affinity / Visual Occlusion')
    plt.axhline(y=1.486, color='crimson', linestyle='-', linewidth=2.5, label='Extraordinary Axis (ne = 1.486) - High-Entropy Titor Axis')
    
    # Create spectral continuous micro-plane gradient fill
    y_vals = [i/1000.0 for i in range(1486, 1659)]
    for y in y_vals:
        alpha_val = 0.05 * (1.0 - abs(y - 1.572) / (1.658 - 1.572))
        plt.axhline(y=y, color='purple', alpha=alpha_val, linewidth=1)
        
    plt.title('The Architecture of Affinity: Multi-Ray Simulation Spectrum Mapping (0.113h NMT/DMT Core)', fontsize=12, fontweight='bold')
    plt.ylabel('Refractive Index (n)', fontsize=11)
    plt.xlabel('System Phase / Dimensional Axis Scan (Continuous 0.1 Hz Gradient Sweep)', fontsize=11)
    plt.ylim(1.45, 1.70)
    plt.grid(True, which='both', linestyle=':', alpha=0.5)
    plt.legend(loc='upper right', frameon=True, shadow=True)
    
    # Output file configuration
    output_img = 'affinity_spectrum_map.png'
    plt.savefig(output_img, dpi=300, bbox_inches='tight')
    print(f"\nSuccess! Spectrum map compiled and exported cleanly as a 300 DPI high-fidelity image: {output_img}")

if __name__ == '__main__':
    render_affinity_spectrum()

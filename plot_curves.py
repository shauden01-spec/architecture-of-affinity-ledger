import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_dashboard(i):
    csv_filename = "telemetry_log.csv"
    if not os.path.exists(csv_filename):
        return

    try:
        # Ingest incremental row matrices from spreadsheet logs
        df = pd.read_csv(csv_filename)
        if df.empty or len(df) < 2:
            return

        df['Convection_Delta'] = pd.to_numeric(df['Convection_Delta'])
        
        # Pull only the most recent 30 entries to keep the window readable
        df_display = df.tail(30)

        plt.cla() # Wipe prior frame assets to redraw cleanly
        
        # Plot your target parameters using your preferred spectrum profile
        plt.plot(df_display['Loop_Count'], df_display['Convection_Delta'], 
                 marker='o', color='#AB24FF', linestyle='-', linewidth=2, label='Convection Delta')
        
        # Redraw the static boundary parameter limit line
        plt.axhline(y=0.0045, color='r', linestyle='--', alpha=0.7, label='Dampening Threshold (0.0045)')
        
        # Apply clean presentation geometry properties
        plt.title("Real-Time Crystal Matrix Telemetry Dashboard", fontsize=12, fontweight='bold', pad=10)
        plt.xlabel("Automated Loop Count Sequence (Last 30 Records)", fontsize=10)
        plt.ylabel("Thermodynamic Velocity Delta", fontsize=10)
        plt.grid(True, linestyle=':', alpha=0.5)
        plt.legend(loc='upper left')
        plt.tight_layout()
        
    except Exception as e:
        # Prevent data lock collisions if the pump script writes mid-refresh cycle
        pass

if __name__ == "__main__":
    fig = plt.figure(figsize=(10, 5))
    
    # Establish a dynamic monitoring loop that auto-refreshes the layout every 1000ms
    ani = FuncAnimation(fig, animate_dashboard, cache_frame_data=False, interval=1000)
    plt.show()

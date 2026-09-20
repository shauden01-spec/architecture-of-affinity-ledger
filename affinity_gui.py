import tkinter as tk
from tkinter import messagebox
import subprocess
import os

class AffinityControlPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Affinity Core Orchestration Dashboard")
        self.root.geometry("450x320")
        self.root.configure(bg="#121212")
        self.script_dir = "C:\\Users\\Admin\\Documents\\architecture-of-affinity"
        self.build_ui_elements()

    def build_ui_elements(self):
        # Decorative Title Plate Header
        title = tk.Label(self.root, text="🌌 AFFINITY LEDGER CORE SYSTEM", font=("Helvetica", 14, "bold"), fg="#AB24FF", bg="#121212")
        title.pack(pady=15)

        # Component 1: Baseline Parameter Input Override Fields
        lbl_frame = tk.Frame(self.root, bg="#121212")
        lbl_frame.pack(pady=10)
        
        tk.Label(lbl_frame, text="Target Calibration Baseline:", fg="#FFFFFF", bg="#121212", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
        self.entry_baseline = tk.Entry(lbl_frame, width=10, bg="#222222", fg="#AB24FF", insertbackground="#AB24FF", font=("Helvetica", 10, "bold"))
        self.entry_baseline.insert(0, "0.572")
        self.entry_baseline.pack(side=tk.LEFT, padx=5)

        # Action Execution Buttons Array Mapping
        btn_config = {"font": ("Helvetica", 10, "bold"), "bg": "#222222", "fg": "#FFFFFF", "activebackground": "#AB24FF", "activeforeground": "#FFFFFF", "width": 35, "pady": 5}
        
        tk.Button(self.root, text="🎯 Execute Target Recalibration Override", command=self.trigger_calibration, **btn_config).pack(pady=5)
        tk.Button(self.root, text="📦 Append Automated Telemetry Data Block", command=self.trigger_generation, **btn_config).pack(pady=5)
        tk.Button(self.root, text="📊 Launch Real-Time Visual Curves Analytics", command=self.trigger_dashboard, **btn_config).pack(pady=5)

    def trigger_calibration(self):
        val = self.entry_baseline.get()
        os.chdir(self.script_dir)
        subprocess.Popen(f"python affinity_manager.py --calibrate {val}", shell=True)
        messagebox.showinfo("System Calibration Update", f"Dispatched baseline override command parameters targeting values: {val}")

    def trigger_generation(self):
        os.chdir(self.script_dir)
        subprocess.Popen("python affinity_manager.py --generate", shell=True)
        messagebox.showinfo("Data Stream Update", "Automated tracking coordinates generated and logged straight into database indices.")

    def trigger_dashboard(self):
        os.chdir(self.script_dir)
        subprocess.Popen("python plot_curves.py", shell=True)

if __name__ == "__main__":
    window = tk.Tk()
    app = AffinityControlPanel(window)
    window.mainloop()

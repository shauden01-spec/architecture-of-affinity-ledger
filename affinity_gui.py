import tkinter as tk
from tkinter import scrolledtext, messagebox
import subprocess
import os
import sys

class AffinityControlPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Affinity Core Orchestration Dashboard")
        self.root.geometry("500x500")
        self.root.configure(bg="#121212")
        self.script_dir = "C:\\Users\\Admin\\Documents\\architecture-of-affinity"
        self.build_ui_elements()

    def build_ui_elements(self):
        title = tk.Label(self.root, text="🌌 AFFINITY LEDGER CORE SYSTEM", font=("Helvetica", 14, "bold"), fg="#AB24FF", bg="#121212")
        title.pack(pady=15)

        lbl_frame = tk.Frame(self.root, bg="#121212")
        lbl_frame.pack(pady=10)
        
        tk.Label(lbl_frame, text="Target Calibration Baseline:", fg="#FFFFFF", bg="#121212", font=("Helvetica", 10)).pack(side=tk.LEFT, padx=5)
        self.entry_baseline = tk.Entry(lbl_frame, width=10, bg="#222222", fg="#AB24FF", insertbackground="#AB24FF", font=("Helvetica", 10, "bold"))
        self.entry_baseline.insert(0, "0.572")
        self.entry_baseline.pack(side=tk.LEFT, padx=5)

        btn_config = {"font": ("Helvetica", 10, "bold"), "bg": "#222222", "fg": "#FFFFFF", "activebackground": "#AB24FF", "activeforeground": "#FFFFFF", "width": 35, "pady": 5}
        
        tk.Button(self.root, text="🎯 Execute Target Recalibration Override", command=self.trigger_calibration, **btn_config).pack(pady=5)
        tk.Button(self.root, text="📦 Append Automated Telemetry Data Block", command=self.trigger_generation, **btn_config).pack(pady=5)
        tk.Button(self.root, text="📊 Launch Real-Time Visual Curves Analytics", command=self.trigger_dashboard, **btn_config).pack(pady=5)

        # INTERACTIVE TERMINAL LOG BOX
        tk.Label(self.root, text="💻 Real-Time Log Execution Summaries:", fg="#AB24FF", bg="#121212", font=("Helvetica", 10, "bold")).pack(pady=(15, 2))
        self.terminal_log = scrolledtext.ScrolledText(self.root, width=55, height=8, bg="#050505", fg="#00FF00", insertbackground="#00FF00", font=("Consolas", 9))
        self.terminal_log.pack(pady=5, padx=10)
        self.log_message("📡 Operational control console initialized. Ready for command updates...")

    def log_message(self, message):
        self.terminal_log.insert(tk.END, f"[{time.strftime('%H:%M:%S')}] {message}\n")
        self.terminal_log.see(tk.END)

    def trigger_calibration(self):
        val = self.entry_baseline.get()
        os.chdir(self.script_dir)
        self.log_message(f"Dispatched calibration shift targeting baseline: {val}")
        # Capture process logs and write them back into our terminal view frame
        res = subprocess.run(f"python affinity_manager.py --calibrate {val}", shell=True, capture_output=True, text=True)
        if res.stdout: self.log_message(res.stdout.strip())

    def trigger_generation(self):
        os.chdir(self.script_dir)
        self.log_message("Requesting incremental dataset row generation...")
        res = subprocess.run("python affinity_manager.py --generate", shell=True, capture_output=True, text=True)
        if res.stdout: self.log_message(res.stdout.strip())

    def trigger_dashboard(self):
        os.chdir(self.script_dir)
        self.log_message("Initializing real-time dynamic curve graphing window...")
        subprocess.Popen("python plot_curves.py", shell=True)

if __name__ == "__main__":
    import time
    window = tk.Tk()
    app = AffinityControlPanel(window)
    window.mainloop()

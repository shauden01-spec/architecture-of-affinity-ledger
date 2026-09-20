@echo off
title Affinity Ledger Core Management Suite Launcher
color 0B

echo ========================================================
echo 🌌 INITIALIZING THE ARCHITECTURE OF AFFINITY WORKSPACE
echo ========================================================
echo.

cd /d "C:\Users\Admin\Documents\architecture-of-affinity"

echo [1/3] Spinning up background file Sweeper Daemon service...
start "Affinity Sweeper Daemon" /min cmd /k "python sweeper_daemon.py"

echo [2/3] Launching real-time 0.1 Hz Pump Controller loop daemon...
start "Affinity Pump Automation Controller" cmd /k "python pump_automation.py"

echo [3/3] Booting Real-Time Telemetry Tracking Dashboard interface...
start "Affinity Real-Time Analytics Dashboard" cmd /k "python plot_curves.py"

echo.
echo ⚙️ Running workspace data manager maintenance cycles...
python affinity_manager.py

timeout /t 3 >nul
exit

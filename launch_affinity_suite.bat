@echo off
title Affinity Ledger Core Management Suite Launcher
color 0B

echo ========================================================
echo 🌌 INITIALIZING THE ARCHITECTURE OF AFFINITY WORKSPACE
echo ========================================================
echo.

:: Jump cleanly into your explicit project workspace path
cd /d "C:\Users\Admin\Documents\architecture-of-affinity"

echo [1/2] Launching real-time 0.1 Hz Pump Controller loop daemon...
start "Affinity Pump Automation Controller" cmd /k "python pump_automation.py"

echo [2/2] Booting Real-Time Telemetry Tracking Dashboard interface...
start "Affinity Real-Time Analytics Dashboard" cmd /k "python plot_curves.py"

echo.
echo ========================================================
echo 🎉 Core modules initialized in separate console clusters!
echo ========================================================
timeout /t 3 >nul
exit

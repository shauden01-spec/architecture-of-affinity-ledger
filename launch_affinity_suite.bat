@echo off
title Affinity Ledger Core Management Suite Launcher
color 0B

echo ========================================================
echo 🌌 INITIALIZING THE ARCHITECTURE OF AFFINITY WORKSPACE
echo ========================================================
echo.

cd /d "C:\Users\Admin\Documents\architecture-of-affinity"

:: COMPONENT 3: BOOT UP DATABASE PROTECTION TRIGGER LOCK
echo 🗄️ Executing system boot backup routine...
if exist "datasets\affinity_core.db" (
    echo    ↳ Mirroring core relational database file to fallback directory...
    copy /y "datasets\affinity_core.db" "datasets\affinity_core_boot_backup.db" >nul
    echo    🔒 Secure boot backup synchronized.
) else (
    echo    ⚠️ Notice: Database core index not found. Bypassing fallback duplication lock.
)
echo.

echo [1/3] Spinning up background file Sweeper Daemon service...
start "Affinity Sweeper Daemon" /min cmd /k "python sweeper_daemon.py"

echo [2/3] Launching real-time 0.1 Hz Pump Controller loop daemon...
start "Affinity Pump Automation Controller" cmd /k "python pump_automation.py"

echo [3/3] Booting Real-Time Telemetry Tracking Dashboard interface...
start "Affinity Real-Time Analytics Dashboard" cmd /k "python plot_curves.py"

echo.
echo ⚙️ Running workspace data manager maintenance cycles...
python affinity_manager.py
python affinity_manager.py --generate

timeout /t 3 >nul
exit

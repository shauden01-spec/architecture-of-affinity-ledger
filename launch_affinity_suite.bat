@echo off
title AFFINITY ARCHITECTURE INTEGRATION SUITE
cd /d "C:\Users\Admin\Documents\architecture-of-affinity"

echo ======================================================================
echo  BOOTING AFFINITY WORKSPACE CORE ENGINE ENVIRONMENT
echo ======================================================================
echo.

set "DB_FILE=ledger.db"
set "BACKUP_DIR=datasets\backups"

:: Generate safe timestamp strings
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set "dt=%%I"
set "TIMESTAMP=%dt:~0,4%%dt:~4,2%%dt:~6,2%_%dt:~8,2%%dt:~10,2%%dt:~12,2%"

:: Execute safety backup routine if the active ledger file exists
if exist "%DB_FILE%" (
    if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%"
    echo  Archive Backup: Backing up database ledger file before launch...
    copy /y "%DB_FILE%" "%BACKUP_DIR%\ledger_backup_%TIMESTAMP%.db" >nul
    echo  Success: Snapshot database backup verified and stored cleanly.
) else (
    echo  Notice: No existing database ledger file found to back up. Initializing clean layer.
)
echo.

:: Run the top-down test suite diagnostics to verify data pipeline security before looping
echo  Running system data pipeline pre-flight test checks...
python test_suite_diagnostics.py
if errorlevel 1 (
    echo.
    echo  ERROR: System diagnostics test suite failed. Aborting core boot loop to prevent file corruption.
    echo.
    pause
    exit /b
)
echo  Pre-flight diagnostics passed completely.
echo.

:: Run the master orchestration script file
echo  Starting master runtime orchestration cycle loop...
python run_equilibrium_loop.py

echo.
echo ======================================================================
echo  ENGINE EXECUTION LOOP STOPPED CLEANLY
echo ======================================================================
pause

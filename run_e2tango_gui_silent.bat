@echo off
cd /d "%~dp0"

:: Launch application silently without console window
start "" /b py -3.11 dual_modbus_gui_prod.py 2>nul
if %errorLevel% neq 0 (
    start "" /b python dual_modbus_gui_prod.py 2>nul
    if %errorLevel% neq 0 (
        start "" /b py dual_modbus_gui_prod.py 2>nul
        if %errorLevel% neq 0 (
            echo ERROR: Cannot launch application. Python not found.
            pause
            exit /b 1
        )
    )
)

:: Exit immediately after launching
exit /b 0
@echo off
cd /d "%~dp0"

:: Try different Python commands to launch the application
py -3.11 dual_modbus_gui_prod.py
if %errorLevel% neq 0 (
    python dual_modbus_gui_prod.py
    if %errorLevel% neq 0 (
        py dual_modbus_gui_prod.py
        if %errorLevel% neq 0 (
            echo ERROR: Cannot launch application. Python not found.
            pause
            exit /b 1
        )
    )
)
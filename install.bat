@echo off
echo ========================================
echo  e2tango Modbus GUI Installer v1.0
echo ========================================
echo.

:: Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running with Administrator privileges...
) else (
    echo WARNING: Not running as Administrator. Some operations may fail.
    echo It's recommended to run this installer as Administrator.
    echo.
    pause
)

:: Set installation directory
set INSTALL_DIR=%~dp0
set PYTHON_URL=https://www.python.org/ftp/python/3.11.10/python-3.11.10-amd64.exe
set PYTHON_INSTALLER=%TEMP%\python-3.11.10-amd64.exe

echo Installation directory: %INSTALL_DIR%
echo.

:: Check if Python 3.11 is already installed
echo [1/5] Checking Python installation...
python --version 2>nul | findstr "3.11" >nul
if %errorLevel% == 0 (
    echo Python 3.11 is already installed.
    goto :install_dependencies
)

py -3.11 --version 2>nul | findstr "3.11" >nul
if %errorLevel% == 0 (
    echo Python 3.11 is available via py launcher.
    goto :install_dependencies
)

echo Python 3.11 not found. Installing Python 3.11...

:: Download Python 3.11 installer
echo [2/5] Downloading Python 3.11 installer...
powershell -Command "& {[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%'}"

if not exist "%PYTHON_INSTALLER%" (
    echo ERROR: Failed to download Python installer.
    echo Please download and install Python 3.11 manually from https://python.org
    pause
    exit /b 1
)

:: Install Python 3.11
echo [3/5] Installing Python 3.11...
"%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 Include_doc=0

:: Wait for installation to complete
timeout /t 10 /nobreak >nul

:: Clean up installer
del "%PYTHON_INSTALLER%" >nul 2>&1

:: Refresh environment variables
echo Refreshing environment variables...
call refreshenv >nul 2>&1

:install_dependencies
echo [4/5] Installing Python dependencies...

:: Try different Python commands to install dependencies
py -3.11 -m pip install --upgrade pip >nul 2>&1
py -3.11 -m pip install -r "%INSTALL_DIR%requirements.txt"
if %errorLevel% == 0 (
    echo Dependencies installed successfully with py -3.11
    goto :create_launcher
)

python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r "%INSTALL_DIR%requirements.txt"
if %errorLevel% == 0 (
    echo Dependencies installed successfully with python
    goto :create_launcher
)

py -m pip install --upgrade pip >nul 2>&1
py -m pip install -r "%INSTALL_DIR%requirements.txt"
if %errorLevel% == 0 (
    echo Dependencies installed successfully with py
    goto :create_launcher
)

echo ERROR: Failed to install dependencies. Please run manually:
echo   py -3.11 -m pip install -r requirements.txt
pause
exit /b 1

:create_launcher
echo [5/5] Creating launcher script...

:: Create launcher script
(
echo @echo off
echo cd /d "%INSTALL_DIR%"
echo.
echo :: Try different Python commands to launch the application
echo py -3.11 dual_modbus_gui_prod.py
echo if %%errorLevel%% neq 0 ^(
echo     python dual_modbus_gui_prod.py
echo     if %%errorLevel%% neq 0 ^(
echo         py dual_modbus_gui_prod.py
echo         if %%errorLevel%% neq 0 ^(
echo             echo ERROR: Cannot launch application. Python not found.
echo             pause
echo             exit /b 1
echo         ^)
echo     ^)
echo ^)
) > "%INSTALL_DIR%run_e2tango_gui.bat"

:: Create desktop shortcut (if possible)
set DESKTOP=%USERPROFILE%\Desktop
if exist "%DESKTOP%" (
    echo Creating desktop shortcut...
    (
    echo @echo off
    echo cd /d "%INSTALL_DIR%"
    echo call run_e2tango_gui.bat
    ) > "%DESKTOP%\e2tango Modbus GUI.bat"
)

echo.
echo ========================================
echo  Installation Complete!
echo ========================================
echo.
echo Application installed in: %INSTALL_DIR%
echo.
echo To run the application:
echo 1. Double-click: run_e2tango_gui.bat
echo 2. Or use desktop shortcut: e2tango Modbus GUI.bat
echo.
echo The application will run without showing console window.
echo.
pause
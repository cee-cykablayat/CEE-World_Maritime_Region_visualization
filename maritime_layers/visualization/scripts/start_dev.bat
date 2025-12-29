@echo off
REM Combined Developer Launcher - Windows
REM Starts backend server and opens frontend in browser

cls
color 0A

echo.
echo ╔════════════════════════════════════════════════════╗
echo ║    🗺️  MARITIME BOUNDARIES - DEVELOPER SETUP      ║
echo ║         Crimson Energy Experts Pvt. Ltd.          ║
echo ╚════════════════════════════════════════════════════╝
echo.

REM Get the directory
cd /d "%~dp0"
cd ..\..

echo 📁 Working directory: %CD%
echo.

REM Check if Python is available
where python3 >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=python3
    goto :check_port
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=python
    goto :check_port
)

echo ❌ Python not found on your system.
echo.
echo Please install Python from: https://www.python.org/downloads/
echo.
pause
exit /b 1

:check_port
echo ✓ Python found: %PYTHON_CMD%
echo.

set PORT=8000

echo 🚀 Starting backend server on port %PORT%...
echo.

REM Start the server in a new window
start "Maritime Boundaries Server" /min %PYTHON_CMD% -m http.server %PORT%

REM Wait for server to start
timeout /t 2 /nobreak > nul

echo ✓ Server started successfully
echo.
echo ════════════════════════════════════════════════════
echo 📊 SERVER INFORMATION
echo ════════════════════════════════════════════════════
echo.
echo 🌐 Frontend:
echo    http://localhost:%PORT%/visualization/frontend/maritime_interactive_map.html
echo.
echo 📁 Data Directory:
echo    %CD%\processed_data
echo.
echo ════════════════════════════════════════════════════
echo.

REM Open in default browser
echo 🌐 Opening browser...
timeout /t 1 /nobreak > nul
start http://localhost:%PORT%/frontend/maritime_interactive_map.html

echo.
echo ════════════════════════════════════════════════════
echo ⏸️  Server is running in background
echo.
echo To stop the server, find "Maritime Boundaries Server"
echo in your taskbar and close the window.
echo ════════════════════════════════════════════════════
echo.
pause

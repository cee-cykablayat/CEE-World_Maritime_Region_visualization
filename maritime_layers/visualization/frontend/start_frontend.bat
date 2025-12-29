@echo off
REM Frontend Server Launcher - Windows
REM Starts a local web server for the frontend

cls
echo.
echo ==================================================
echo 🗺️  Maritime Boundaries - Frontend Server
echo ==================================================
echo.

REM Get the directory where this script is located
cd /d "%~dp0"

REM Go to parent directory (visualization root)
cd ..

echo 📁 Frontend directory: %CD%\frontend
echo.

REM Check if Python is available
where python3 >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    goto :run_python3
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    goto :run_python2
)

echo ❌ Python not found on your system.
echo.
echo Please install Python from: https://www.python.org/downloads/
echo.
pause
exit /b 1

:run_python3
echo 🚀 Starting frontend server with Python 3
echo.
echo ✓ Available at:
echo   http://localhost:8000/frontend/maritime_interactive_map.html
echo.
echo 📂 Serving files from: %CD%
echo.
echo To stop the server, press Ctrl+C
echo.
python3 -m http.server 8000
exit /b 0

:run_python2
echo 🚀 Starting frontend server with Python 2
echo.
echo ✓ Available at:
echo   http://localhost:8000/frontend/maritime_interactive_map.html
echo.
echo 📂 Serving files from: %CD%
echo.
echo To stop the server, press Ctrl+C
echo.
python -m SimpleHTTPServer 8000
exit /b 0

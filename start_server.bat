@echo off
REM Maritime Boundaries Interactive Map - Local Server Launcher (Windows)
REM This script starts a local web server to serve the maritime_interactive_map.html file

echo.
echo 🗺️  Maritime Boundaries - Interactive Explorer
echo ==================================================
echo.

REM Get the directory where this script is located
cd /d "%~dp0"

echo 📁 Server directory: %CD%
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
echo Or use an alternative:
echo   - Node.js: npx http-server
echo   - Ruby: ruby -run -ehttpd . -p8000
echo   - PHP: php -S localhost:8000
echo.
pause
exit /b 1

:run_python3
echo 🚀 Starting web server with Python 3
echo.
echo ✓ Files being served:
echo   - maritime_interactive_map.html
echo   - maritime_layers/processed_data/
echo.
echo 📂 Access the map at:
echo   http://localhost:8000/maritime_interactive_map.html
echo.
echo To stop the server, press Ctrl+C
echo.
python3 -m http.server 8000
exit /b 0

:run_python2
echo 🚀 Starting web server with Python 2
echo.
echo ✓ Files being served:
echo   - maritime_interactive_map.html
echo   - maritime_layers/processed_data/
echo.
echo 📂 Access the map at:
echo   http://localhost:8000/maritime_interactive_map.html
echo.
echo To stop the server, press Ctrl+C
echo.
python -m SimpleHTTPServer 8000
exit /b 0

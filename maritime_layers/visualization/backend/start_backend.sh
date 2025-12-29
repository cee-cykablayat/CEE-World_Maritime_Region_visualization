#!/bin/bash

# Backend Server Launcher - Linux/macOS
# Starts a local web server for the backend

echo ""
echo "=================================================="
echo "🗺️  Maritime Boundaries - Backend Server"
echo "=================================================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

echo "📁 Backend directory: $SCRIPT_DIR"
echo "🌐 Base directory: $PARENT_DIR"
echo ""

# Change to parent directory (visualization root)
cd "$PARENT_DIR"

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python not found"
        echo ""
        echo "Please install Python 3 from: https://www.python.org/downloads/"
        exit 1
    fi
    PYTHON_CMD="python"
else
    PYTHON_CMD="python3"
fi

echo "🚀 Starting backend server..."
echo ""
echo "✓ Backend available at:"
echo "  http://localhost:8000"
echo ""
echo "✓ Frontend available at:"
echo "  http://localhost:8000/frontend/maritime_interactive_map.html"
echo ""
echo "📂 Serving files from: $PARENT_DIR"
echo ""
echo "To stop the server, press Ctrl+C"
echo ""

$PYTHON_CMD -m http.server 8000

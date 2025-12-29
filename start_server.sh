#!/bin/bash

# Maritime Boundaries Interactive Map - Local Server Launcher
# This script starts a local web server to serve the maritime_interactive_map.html file

echo "🗺️  Maritime Boundaries - Interactive Explorer"
echo "=================================================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "📁 Server directory: $SCRIPT_DIR"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Trying Python 2..."
    if command -v python &> /dev/null; then
        cd "$SCRIPT_DIR"
        echo "🚀 Starting web server on http://localhost:8000"
        echo ""
        echo "To stop the server, press Ctrl+C"
        echo ""
        python -m SimpleHTTPServer 8000
        exit 0
    else
        echo "❌ Neither Python 3 nor Python 2 found."
        echo ""
        echo "Please install Python or use an alternative:"
        echo ""
        echo "  Node.js: npx http-server"
        echo "  Ruby: ruby -run -ehttpd . -p8000"
        echo "  PHP: php -S localhost:8000"
        exit 1
    fi
fi

# Use Python 3
cd "$SCRIPT_DIR"
echo "🚀 Starting web server on http://localhost:8000"
echo ""
echo "✓ Files being served:"
echo "  - maritime_interactive_map.html"
echo "  - maritime_layers/processed_data/"
echo ""
echo "📂 Access the map at:"
echo "  http://localhost:8000/maritime_interactive_map.html"
echo ""
echo "To stop the server, press Ctrl+C"
echo ""

python3 -m http.server 8000

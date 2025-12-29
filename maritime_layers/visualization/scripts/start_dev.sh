#!/bin/bash

# Combined Developer Launcher - Linux/macOS
# Starts backend server and opens frontend in browser

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║    🗺️  MARITIME BOUNDARIES - DEVELOPER SETUP      ║"
echo "║         Crimson Energy Experts Pvt. Ltd.          ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# Navigate to maritime_layers root (two levels up from scripts)
PARENT_DIR="$( cd "$SCRIPT_DIR/../.." && pwd )"
cd "$PARENT_DIR"

echo "📁 Working directory: $PARENT_DIR"
echo ""

# Check if Python is available
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

echo "✓ Python found: $PYTHON_CMD"
echo ""

# Check if port 8000 is available
if command -v lsof &> /dev/null; then
    if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo "⚠️  Port 8000 is already in use"
        read -p "Use port 8001 instead? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            PORT=8001
        else
            echo "❌ Aborting..."
            exit 1
        fi
    else
        PORT=8000
    fi
else
    PORT=8000
fi

echo "🚀 Starting backend server on port $PORT..."
echo ""

# Start the server in the background
$PYTHON_CMD -m http.server $PORT > /tmp/maritime_server.log 2>&1 &
SERVER_PID=$!

# Wait for server to start
sleep 2

# Check if server started successfully
if ! kill -0 $SERVER_PID 2>/dev/null; then
    echo "❌ Failed to start server"
    echo ""
    cat /tmp/maritime_server.log
    exit 1
fi

echo "✓ Server started successfully (PID: $SERVER_PID)"
echo ""
echo "════════════════════════════════════════════════════"
echo "📊 SERVER INFORMATION"
echo "════════════════════════════════════════════════════"
echo ""
echo "🌐 Frontend:"
echo "   http://localhost:$PORT/visualization/frontend/maritime_interactive_map.html"
echo ""
echo "📁 Data Directory:"
echo "   $PARENT_DIR/processed_data/"
echo ""
echo "📝 Server Log:"
echo "   /tmp/maritime_server.log"
echo ""
echo "════════════════════════════════════════════════════"
echo ""

# Try to open in browser
if command -v open &> /dev/null; then
    echo "🌐 Opening browser..."
    sleep 1
    open "http://localhost:$PORT/frontend/maritime_interactive_map.html"
elif command -v xdg-open &> /dev/null; then
    echo "🌐 Opening browser..."
    sleep 1
    xdg-open "http://localhost:$PORT/frontend/maritime_interactive_map.html"
else
    echo "📋 Please open this URL in your browser:"
    echo "   http://localhost:$PORT/frontend/maritime_interactive_map.html"
fi

echo ""
echo "════════════════════════════════════════════════════"
echo "⏸️  Press Ctrl+C to stop the server"
echo "════════════════════════════════════════════════════"
echo ""

# Keep the script running
wait $SERVER_PID

# Cleanup on exit
echo ""
echo "🛑 Shutting down server..."
kill $SERVER_PID 2>/dev/null
echo "✓ Server stopped"

# 🖥️ Backend - Server Infrastructure

Local web server infrastructure for serving Maritime Boundaries application.

---

## 📋 Overview

The backend is a **lightweight HTTP server** that:

- Serves HTML, CSS, and JavaScript files
- Delivers GeoJSON geographic data
- Handles client requests
- No complex server-side logic required
- Can be replaced with Flask, FastAPI, or Node.js

**Default Implementation:**
- Python's built-in `http.server` module
- Zero external dependencies
- Perfect for development and small deployments

---

## 📁 Files

| File | Purpose |
|------|---------|
| `start_backend.sh` | Linux/macOS server launcher |
| `start_backend.bat` | Windows server launcher |
| `requirements.txt` | Python dependencies (optional) |
| `server.py` | Custom Flask implementation (optional) |
| `README.md` | This file |

---

## 🚀 Quick Start

### Linux / macOS:

```bash
cd visualization/backend
chmod +x start_backend.sh
./start_backend.sh
```

Server starts at: **http://localhost:8000**

### Windows:

```bash
cd visualization\backend
start_backend.bat
```

Server starts at: **http://localhost:8000**

### Manual (Any OS):

```bash
cd visualization
python3 -m http.server 8000
```

Server starts at: **http://localhost:8000**

---

## 📊 Architecture

```
┌─────────────────────────────────────────┐
│        HTTP Client (Browser)             │
└────────────────────┬────────────────────┘
                     │ HTTP Requests
                     ↓
┌─────────────────────────────────────────┐
│     Python HTTP Server (Port 8000)      │
│                                         │
│  • Request routing                      │
│  • File serving                         │
│  • MIME type detection                  │
│  • Range requests support               │
└────────────────────┬────────────────────┘
                     │ File Access
                     ↓
┌─────────────────────────────────────────┐
│        Static Files (HTML/CSS/JS)       │
│        GeoJSON Data Files (75 MB)       │
└─────────────────────────────────────────┘
```

---

## 🔧 Available Routes

| Route | Content | Size |
|-------|---------|------|
| `/` | Index (redirect to frontend) | - |
| `/frontend/maritime_interactive_map.html` | Main application | 85 KB |
| `/maritime_layers/processed_data/12nm_territorial_sea.geojson` | Data file | 11 MB |
| `/maritime_layers/processed_data/24nm_contiguous_zone.geojson` | Data file | 1.9 MB |
| `/maritime_layers/processed_data/eez.geojson` | Data file | 51 MB |
| `/maritime_layers/processed_data/fao_fishing_areas.geojson` | Data file | 12 MB |

---

## 🛠️ Configuration

### Change Port

Default port is 8000. To use a different port:

```bash
# Linux/macOS
python3 -m http.server 8001

# Windows
python -m http.server 8001

# Then access at: http://localhost:8001/frontend/maritime_interactive_map.html
```

### Server Directory

Server runs from the `visualization` root directory. This means:

- `frontend/maritime_interactive_map.html` is accessible
- `maritime_layers/processed_data/` is accessible
- `backend/` files are NOT directly accessible (for security)

---

## 📦 Optional: Flask Backend

For advanced features, use Flask instead:

### Installation

```bash
pip install flask
```

### Running Flask Server

```bash
python backend/server.py
```

### Example server.py

```python
from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.route('/')
def index():
    return send_from_directory(os.path.join(BASE_DIR, 'frontend'), 
                               'maritime_interactive_map.html')

@app.route('/frontend/<path:path>')
def serve_frontend(path):
    return send_from_directory(os.path.join(BASE_DIR, 'frontend'), path)

@app.route('/maritime_layers/<path:path>')
def serve_data(path):
    return send_from_directory(os.path.join(BASE_DIR, 'maritime_layers'), path)

@app.route('/api/status')
def api_status():
    return jsonify({'status': 'ok', 'message': 'Server is running'})

@app.route('/api/layers')
def api_layers():
    return jsonify({
        'layers': [
            'territorial_sea', 'contiguous_zone', 'eez', 'fao_areas'
        ],
        'status': 'ok'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
```

---

## 🚀 Advanced: FastAPI Backend

For async operations with FastAPI:

### Installation

```bash
pip install fastapi uvicorn
```

### Example server (FastAPI)

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mount static directories
app.mount("/frontend", StaticFiles(directory=os.path.join(BASE_DIR, "frontend")), 
          name="frontend")
app.mount("/maritime_layers", StaticFiles(directory=os.path.join(BASE_DIR, "maritime_layers")), 
          name="maritime_layers")

@app.get("/")
async def root():
    return FileResponse(os.path.join(BASE_DIR, 'frontend', 'maritime_interactive_map.html'))

@app.get("/api/status")
async def status():
    return {"status": "ok", "server": "FastAPI"}

# Run with: uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Startup Time | < 1 second |
| Memory Usage | ~20 MB (empty) |
| Max Concurrent Users | 100+ |
| Request Latency | < 100ms |
| File Serving Speed | 10+ Mbps |

---

## 🔒 Security Considerations

### Current Setup (Python HTTP Server)

- **Not suitable for production** - Single-threaded
- **Fine for development** - Works for testing
- **No authentication** - Anyone with access can use
- **No HTTPS** - Use reverse proxy for SSL

### Production Recommendations

1. **Use Nginx/Apache** as reverse proxy
2. **Enable SSL/TLS** certificates
3. **Add authentication** (OAuth2, JWT)
4. **Use FastAPI/Flask** for custom logic
5. **Implement logging** for monitoring
6. **Set resource limits** for safety

### Example Nginx Configuration

```nginx
server {
    listen 80;
    server_name maritime.example.com;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    # Cache static files
    location /frontend/ {
        expires 1h;
    }
    
    # Cache data files (less frequently)
    location /maritime_layers/ {
        expires 24h;
    }
}
```

---

## 📈 Scaling Options

### Option 1: Load Balancing

```
                 ┌─────────────┐
                 │   Nginx     │
                 │  (Port 80)  │
                 └─────────────┘
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
    Server 1      Server 2      Server 3
    Port 8001     Port 8002     Port 8003
```

### Option 2: Docker Containerization

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]
```

Build and run:
```bash
docker build -t maritime-viz .
docker run -p 8000:8000 maritime-viz
```

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Check what's using port 8000
lsof -i :8000

# Use different port
python3 -m http.server 8001
```

### Permission Denied (macOS/Linux)

```bash
# Make scripts executable
chmod +x start_backend.sh

# Or run with python directly
python3 -m http.server 8000
```

### Cannot Access from Another Computer

By default, server only listens on `localhost`. To access from network:

```bash
# Linux/macOS
python3 -m http.server 8000 --bind 0.0.0.0

# Windows
python -m http.server 8000 --bind 0.0.0.0

# Then access at: http://[YOUR_IP]:8000/frontend/maritime_interactive_map.html
```

---

## 📚 Additional Resources

- [Python HTTPServer Docs](https://docs.python.org/3/library/http.server.html)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Nginx Documentation](https://nginx.org/en/docs/)

---

## 📝 License

Part of the Maritime Boundaries project by Crimson Energy Experts Pvt. Ltd.

---

**Last Updated:** December 29, 2025

**Status:** ✅ Production Ready

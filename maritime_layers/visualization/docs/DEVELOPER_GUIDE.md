# 👨‍💻 Developer Guide - Maritime Boundaries Visualization

Complete guide for developers working with the Maritime Boundaries system.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [System Architecture](#system-architecture)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Code Overview](#code-overview)
- [Adding Features](#adding-features)
- [Testing](#testing)
- [Debugging](#debugging)
- [Deployment](#deployment)

---

## 🎯 Project Overview

**Maritime Boundaries Visualization System** is a web-based geographic information system (GIS) for exploring maritime boundary zones.

**Technology Stack:**
- Frontend: HTML5, CSS3, JavaScript (ES6+), Leaflet.js
- Backend: Python (http.server)
- Data: GeoJSON format
- Styling: CSS Grid/Flexbox, Font Awesome icons

**Key Components:**
1. **Frontend** - Interactive map interface
2. **Backend** - Static file server
3. **Data** - Preprocessed GeoJSON files
4. **Scripts** - Automation and deployment

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    BROWSER (Client)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │   maritime_interactive_map.html                      │  │
│  │   ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │  │
│  │   │   Leaflet    │  │  Checkboxes  │  │  Popups  │  │  │
│  │   │     Map      │  │  & Controls  │  │ & Info   │  │  │
│  │   └──────────────┘  └──────────────┘  └──────────┘  │  │
│  └─────────────────────┬──────────────────────────────┘  │
│                        │ AJAX Fetch                       │
└────────────────────────┼────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│              BACKEND (Server - Port 8000)                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │        Python HTTP Server                            │  │
│  │  (Serves HTML/CSS/JS and GeoJSON Files)              │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────┐
│                   FILESYSTEM (Data)                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  frontend/maritime_interactive_map.html              │  │
│  │  maritime_layers/processed_data/                     │  │
│  │    ├── 12nm_territorial_sea.geojson (11 MB)          │  │
│  │    ├── 24nm_contiguous_zone.geojson (1.9 MB)         │  │
│  │    ├── eez.geojson (51 MB)                           │  │
│  │    └── fao_fishing_areas.geojson (12 MB)             │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.6+ (for HTTP server)
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Text editor or IDE (VS Code recommended)
- Git (for version control)

### Installation

1. **Navigate to project:**
   ```bash
   cd /path/to/visualization
   ```

2. **Verify Python installation:**
   ```bash
   python3 --version
   # Should output: Python 3.x.x
   ```

3. **Check data files:**
   ```bash
   ls -lh ../maritime_layers/processed_data/
   # Should show 4 .geojson files
   ```

4. **Start development server:**
   ```bash
   python3 -m http.server 8000
   ```

5. **Open browser:**
   - Go to: `http://localhost:8000/frontend/maritime_interactive_map.html`

---

## 📁 Project Structure

```
visualization/
├── README.md                          # Main documentation
├── ARCHITECTURE.md                    # Detailed system design
│
├── frontend/                          # Client-side application
│   ├── maritime_interactive_map.html  # Main UI (ALL IN ONE FILE)
│   ├── start_frontend.sh              # Linux/macOS launcher
│   ├── start_frontend.bat             # Windows launcher
│   └── README.md                      # Frontend docs
│
├── backend/                           # Server infrastructure
│   ├── start_backend.sh               # Linux/macOS launcher
│   ├── start_backend.bat              # Windows launcher
│   ├── requirements.txt               # Python dependencies
│   ├── server.py                      # Optional Flask server
│   └── README.md                      # Backend docs
│
├── scripts/                           # Automation scripts
│   ├── start_dev.sh                   # Combined start (Linux/macOS)
│   ├── start_dev.bat                  # Combined start (Windows)
│   ├── setup.sh                       # Initial setup
│   ├── setup.bat                      # Windows setup
│   └── install_dependencies.sh        # Install packages
│
└── docs/                              # Documentation
    ├── DEVELOPER_GUIDE.md             # This file
    ├── TROUBLESHOOTING.md             # Common issues
    ├── API_REFERENCE.md               # API documentation
    └── CUSTOMIZATION.md               # How to customize
```

---

## ▶️ How to Run

### Development Mode

**Quick start (Linux/macOS):**
```bash
cd visualization
chmod +x scripts/start_dev.sh
./scripts/start_dev.sh
```

**Quick start (Windows):**
```bash
cd visualization
scripts\start_dev.bat
```

**Manual start (Any OS):**
```bash
cd visualization
python3 -m http.server 8000
# Then open: http://localhost:8000/frontend/maritime_interactive_map.html
```

### Debug Mode

**With verbose logging:**
```bash
cd visualization
python3 -m http.server 8000 --directory . --log-level DEBUG
```

**In separate terminals:**

Terminal 1 - Start backend:
```bash
cd visualization/backend
./start_backend.sh
```

Terminal 2 - Develop frontend:
```bash
cd visualization/frontend
# Edit maritime_interactive_map.html
# Refresh browser to see changes
```

---

## 💻 Code Overview

### Frontend Structure (maritime_interactive_map.html)

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Meta tags and CSS -->
    <style>
        /* All styling here */
    </style>
</head>
<body>
    <!-- Navigation bar with Crimson branding -->
    <!-- Sidebar with layer controls -->
    <!-- Main map container -->
    
    <script>
        // Configuration (layer definitions)
        const layers = { ... }
        
        // Map initialization (Leaflet)
        const map = L.map('map').setView([20, 0], 2)
        
        // Layer management functions
        function initializeLayerControls() { ... }
        function loadGeoJsonLayer() { ... }
        function toggleLayer() { ... }
        function updateStatus() { ... }
        
        // Initialization on page load
        document.addEventListener('DOMContentLoaded', async () => { ... })
    </script>
</body>
</html>
```

### Key JavaScript Sections

#### 1. Layer Configuration
```javascript
const layers = {
    'territorial_sea': {
        name: '12NM Territorial Sea',
        color: '#e74c3c',
        file: '../../maritime_layers/processed_data/12nm_territorial_sea.geojson',
        opacity: 0.7,
        fillOpacity: 0.5
    }
    // ... more layers
}
```

#### 2. Map Initialization
```javascript
const map = L.map('map').setView([20, 0], 2)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map)
```

#### 3. GeoJSON Loading
```javascript
async function loadGeoJsonLayer(layerId, layerConfig) {
    // Fetch GeoJSON file
    // Parse features
    // Create Leaflet GeoJSON layer
    // Add styling and popups
    // Store in geoJsonLayers object
}
```

#### 4. Layer Toggle
```javascript
function toggleLayer(event) {
    const checkbox = event.target
    const layerId = checkbox.getAttribute('data-layer')
    
    if (checkbox.checked) {
        map.addLayer(geoJsonLayers[layerId])
    } else {
        map.removeLayer(geoJsonLayers[layerId])
    }
    
    updateStatus()
}
```

---

## 🎨 Adding Features

### Add a New Layer Type

1. **Create GeoJSON file** in `maritime_layers/processed_data/`
2. **Add layer config** to `const layers`:
   ```javascript
   'new_layer': {
       name: 'New Maritime Zone',
       color: '#ff0000',
       file: '../../maritime_layers/processed_data/new_layer.geojson',
       opacity: 0.7,
       fillOpacity: 0.5
   }
   ```
3. **Add styling** in the `loadGeoJsonLayer` function
4. **Test** by loading in browser

### Customize Popup Content

Edit the `onEachFeature` function in `loadGeoJsonLayer`:

```javascript
onEachFeature: (feature, layer) => {
    let popupContent = '<div style="font-family: Arial;">'
    popupContent += `<b>${feature.properties.NAME}</b><br>`
    popupContent += `<hr>`
    
    // Add custom fields
    popupContent += `<b>Field1:</b> ${feature.properties.FIELD1}<br>`
    popupContent += `<b>Field2:</b> ${feature.properties.FIELD2}`
    
    popupContent += '</div>'
    layer.bindPopup(popupContent)
}
```

### Change Map Appearance

**Tile Provider:**
```javascript
L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenTopoMap'
}).addTo(map)
```

**Color Scheme:**
Update CSS variables at top of `<style>` tag

**Default Zoom:**
```javascript
const map = L.map('map').setView([20, 0], 3)  // Change 2 to 3 for more zoom
```

### Add Custom Controls

```javascript
// Add custom button to map
const customControl = L.Control.extend({
    onAdd: function(map) {
        const div = L.DomUtil.create('div', 'custom-control')
        div.innerHTML = '<button onclick="alert(\'Clicked!\')">Click Me</button>'
        return div
    }
})

map.addControl(new customControl({ position: 'topright' }))
```

---

## 🧪 Testing

### Browser DevTools

1. **Open DevTools:** Press `F12`
2. **Console Tab:** Check for JavaScript errors
3. **Network Tab:** Verify GeoJSON files load
4. **Elements Tab:** Inspect HTML structure
5. **Performance Tab:** Check loading times

### Test Checklist

- [ ] All 4 layers load successfully
- [ ] Checkboxes toggle layers on/off
- [ ] Click popups show correct info
- [ ] Map zooms and pans smoothly
- [ ] Page works on mobile devices
- [ ] No console errors
- [ ] Different browsers work

### Automated Testing

```bash
# Simple HTTP test
curl http://localhost:8000/frontend/maritime_interactive_map.html | head -20

# Check data files
curl http://localhost:8000/maritime_layers/processed_data/eez.geojson | head -c 200
```

---

## 🐛 Debugging

### Common Issues

1. **GeoJSON files not loading**
   - Check browser console (F12)
   - Verify file paths are correct
   - Ensure web server is running
   - Check file permissions

2. **Map not displaying**
   - Verify Leaflet CDN is accessible
   - Check #map container exists
   - Review console for errors
   - Try full page reload (Ctrl+F5)

3. **Popups not showing**
   - Check onEachFeature function
   - Verify feature properties exist
   - Check HTML in popup is valid

4. **Slow performance**
   - Normal on first load (15-20 seconds)
   - Check browser memory usage
   - Simplify GeoJSON if possible
   - Use browser caching

### Debug Logging

Add logging to understand execution:

```javascript
console.log('Loading layer:', layerId)
console.log('GeoJSON features:', geojson.features.length)
console.log('Toggle event:', event)
console.log('Layer visibility:', map.hasLayer(layer))
```

View logs in browser console (F12 → Console tab)

---

## 🚀 Deployment

### Development Server
```bash
python3 -m http.server 8000
```

### Production with Nginx

**nginx.conf:**
```nginx
server {
    listen 80;
    server_name maritime.example.com;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
    }
}
```

**Start with:**
```bash
nginx
python3 -m http.server 8000
```

### Production with Docker

**Dockerfile:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]
```

**Build and run:**
```bash
docker build -t maritime-viz .
docker run -p 8000:8000 maritime-viz
```

---

## 📚 Additional Resources

- [Leaflet.js Documentation](https://leafletjs.com/)
- [GeoJSON Specification](https://geojson.org/)
- [MDN JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [OpenStreetMap](https://www.openstreetmap.org/)

---

## 🤝 Contributing

1. Create a branch: `git checkout -b feature/your-feature`
2. Make changes
3. Test thoroughly
4. Document changes
5. Submit pull request

---

## 📝 License

Part of the Maritime Boundaries project by Crimson Energy Experts Pvt. Ltd.

---

**Last Updated:** December 29, 2025

**Status:** ✅ Production Ready

---

**Need Help?** Check [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) or open an issue.

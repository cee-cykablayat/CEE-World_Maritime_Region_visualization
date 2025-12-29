# 🗺️ Frontend - Maritime Boundaries Explorer

Professional interactive web interface for exploring maritime boundaries.

---

## 📋 Overview

The frontend is a **Leaflet.js-based interactive map** that displays four maritime boundary layers:

- **12NM Territorial Sea** - Sovereign territorial waters
- **24NM Contiguous Zone** - Secondary enforcement area
- **Exclusive Economic Zone (EEZ)** - Resource rights zone
- **FAO Fishing Areas** - International fishing management zones

**Features:**
- ✅ Interactive map with pan and zoom
- ✅ Real-time layer toggle with checkboxes
- ✅ Click popups for zone details
- ✅ Professional Crimson Energy branding
- ✅ Responsive design (desktop & mobile)
- ✅ Cross-browser compatible
- ✅ No external dependencies (Leaflet CDN)

---

## 📁 Files

| File | Purpose |
|------|---------|
| `maritime_interactive_map.html` | Main interactive map application |
| `start_frontend.sh` | Linux/macOS launcher |
| `start_frontend.bat` | Windows launcher |
| `README.md` | This file |

---

## 🚀 Quick Start

### Linux / macOS:

```bash
cd visualization/frontend
chmod +x start_frontend.sh
./start_frontend.sh
```

Then open: **http://localhost:8000/frontend/maritime_interactive_map.html**

### Windows:

```bash
cd visualization\frontend
start_frontend.bat
```

Then open: **http://localhost:8000/frontend/maritime_interactive_map.html**

### Manual (Any OS):

```bash
cd visualization
python3 -m http.server 8000
```

Then open: **http://localhost:8000/frontend/maritime_interactive_map.html**

---

## 🎨 User Interface

### Top Navigation Bar
- Crimson Energy logo and branding
- System status indicator
- Professional header styling

### Left Sidebar
- Layer selection checkboxes
- Color-coded zone indicators
- Maritime zone information
- Layer status display

### Main Map
- OpenStreetMap base layer
- Interactive zone rendering
- Click-to-explore popups
- Zoom and pan controls

---

## 🎯 Usage

1. **Start the application** using one of the methods above
2. **Wait for data to load** (~15-20 seconds on first run)
3. **Toggle layers** by checking/unchecking boxes in the sidebar
4. **Explore zones** by clicking any zone on the map
5. **Zoom and pan** to focus on regions of interest

---

## 🔧 Customization

### Change Map Tiles

Find the `L.tileLayer()` call and replace with alternatives:

**Satellite View:**
```javascript
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles © Esri',
    maxZoom: 19
})
```

**Dark Mode:**
```javascript
L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '© CartoDB'
})
```

### Change Colors

Modify the layer colors in the `layers` configuration:

```javascript
'territorial_sea': {
    color: '#e74c3c',  // Change this hex color
    ...
}
```

### Add New Layers

Add entries to the `layers` object:

```javascript
'new_layer': {
    name: 'New Maritime Zone',
    color: '#ff0000',
    icon: 'fa-star',
    file: '../../maritime_layers/processed_data/new_layer.geojson',
    visible: false,
    opacity: 0.7,
    fillOpacity: 0.5
}
```

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Initial Load | 15-20 seconds |
| Layer Toggle | 1-2 seconds |
| Data Size | 75 MB |
| Browser Memory | 500-800 MB |
| Supported Features | 1,100+ zones |

---

## 🌐 Browser Support

| Browser | Status |
|---------|--------|
| Chrome 90+ | ✅ Supported |
| Firefox 88+ | ✅ Supported |
| Safari 14+ | ✅ Supported |
| Edge 90+ | ✅ Supported |
| IE 11 | ❌ Not Supported |

---

## 📱 Responsive Design

The interface automatically adapts to different screen sizes:

- **Desktop (1024px+)** - Full sidebar + large map
- **Tablet (768px-1024px)** - Compact sidebar + map
- **Mobile (<768px)** - Stacked layout with collapsible sidebar

---

## 🐛 Troubleshooting

### Issue: "Cannot load GeoJSON files"

**Cause:** Opening HTML directly from disk (file:// protocol)

**Solution:** Use a web server (HTTP)
```bash
python3 -m http.server 8000
# Then open http://localhost:8000/frontend/maritime_interactive_map.html
```

### Issue: Blank map or no data

**Solution:** Check browser console (F12 → Console tab)
- Look for error messages
- Verify data files exist in `maritime_layers/processed_data/`
- Check network tab to see if files are loading

### Issue: Slow loading

**Normal behavior** - First load takes 15-20 seconds (75 MB data)

---

## 🔐 Security Notes

- **No server-side processing** - All computation in browser
- **No data transmission** - Data stays local
- **CORS-friendly** - Works with any backend
- **HTTPS compatible** - Works on secure connections

---

## 📚 Technologies Used

- **Leaflet.js 1.9.4** - Interactive map library
- **Vanilla JavaScript** - No frameworks required
- **OpenStreetMap** - Base layer tiles
- **GeoJSON** - Vector data format
- **HTML5/CSS3** - Responsive design

---

## 🤝 Integration

The frontend is designed to be easily integrated with:

- **Flask/FastAPI backends** - RESTful API support
- **Custom data sources** - Easy to connect new GeoJSON feeds
- **Analytics platforms** - Event tracking support
- **Authentication systems** - Can add login support

---

## 📝 License

Part of the Maritime Boundaries project by Crimson Energy Experts Pvt. Ltd.

---

**Last Updated:** December 29, 2025

**Status:** ✅ Production Ready

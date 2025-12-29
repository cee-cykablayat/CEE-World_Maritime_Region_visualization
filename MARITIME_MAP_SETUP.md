# 🗺️ Maritime Boundaries Interactive Map - Setup Guide

## Quick Start (Choose One)

### Option 1: Use the Startup Script (RECOMMENDED)

#### Linux / macOS:
```bash
cd /home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas
chmod +x start_server.sh
./start_server.sh
```

#### Windows:
```bash
cd \Users\[YourUsername]\Desktop\Deep_Darshak\References\Build_1_docs\Fishing_areas
start_server.bat
```

Then open your browser to: **http://localhost:8000/maritime_interactive_map.html**

---

### Option 2: Manual Server Setup

#### Python 3 (Windows, macOS, Linux):
```bash
cd /home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas
python3 -m http.server 8000
```

#### Python 2:
```bash
python -m SimpleHTTPServer 8000
```

#### Node.js (if installed):
```bash
cd /home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas
npx http-server
```

#### Ruby:
```bash
ruby -run -ehttpd . -p8000
```

#### PHP:
```bash
php -S localhost:8000
```

---

### Option 3: Browser Extensions

- **VS Code**: Install "Live Server" extension
  - Right-click on `maritime_interactive_map.html`
  - Select "Open with Live Server"

- **Chrome**: Install "Web Server for Chrome" extension
  - Choose this folder as the root
  - Click "Start"

---

## Why a Web Server?

Your browser has security restrictions that prevent loading local files directly (file:// protocol). A local web server works around this limitation.

**You will see this warning if you open the file directly:**
```
⚠️ Local File Access
This page is being loaded from disk (file://).
Some data may fail to load due to browser security restrictions.
```

**Solution:** Use any of the methods above to serve the files over HTTP.

---

## Directory Structure

```
Fishing_areas/
├── maritime_interactive_map.html          ← Main file to open
├── start_server.sh                        ← Linux/macOS launcher
├── start_server.bat                       ← Windows launcher
├── MARITIME_MAP_SETUP.md                  ← This file
├── maritime_layers/
│   └── processed_data/
│       ├── 12nm_territorial_sea.geojson   ← 12NM data
│       ├── 24nm_contiguous_zone.geojson   ← 24NM data
│       ├── eez.geojson                    ← EEZ data
│       └── fao_fishing_areas.geojson      ← FAO data
```

---

## Accessing the Map

After starting your server:

1. **Open your browser**
2. **Go to:** `http://localhost:8000/maritime_interactive_map.html`
3. **Use the checkboxes** on the left to toggle layers
4. **Click any zone** on the map to see details

---

## Features

✅ **Interactive Checkboxes** - Toggle layers on/off in real-time  
✅ **Instant Updates** - No delays or rendering issues  
✅ **Clickable Zones** - Get details about any maritime boundary  
✅ **Beautiful UI** - Professional interface with gradient header  
✅ **Mobile Responsive** - Works on desktop and tablets  
✅ **Cross-browser** - Chrome, Firefox, Safari, Edge supported  

---

## Layers Available

| Layer | Color | Coverage |
|-------|-------|----------|
| **12NM Territorial Sea** | 🔴 Red | 230 zones worldwide |
| **24NM Contiguous Zone** | 🔵 Blue | 220 zones worldwide |
| **Exclusive Economic Zone (EEZ)** | 🟢 Green | 285 zones (140.8M km²) |
| **FAO Fishing Areas** | 🟠 Multi-color | 370 areas by ocean |

---

## Troubleshooting

### Issue: "Failed to load" errors for GeoJSON files

**Solution:** Make sure you're running a web server (HTTP), not opening the file directly.

**Verification:**
- ❌ Wrong: `file:///path/to/maritime_interactive_map.html`
- ✅ Correct: `http://localhost:8000/maritime_interactive_map.html`

### Issue: Browser shows security warning

**Cause:** Browser blocking local file access for security reasons.

**Solution:** Use the startup script or one of the server options above.

### Issue: Layers load but show no data

**Check:**
1. Verify GeoJSON files exist in: `maritime_layers/processed_data/`
2. Open browser console (F12) and look for error messages
3. Files should be ~11MB (12NM), ~2MB (24NM), ~51MB (EEZ), ~12MB (FAO)

### Issue: "Port 8000 already in use"

**Solution:** Change port number:
```bash
python3 -m http.server 8001
# Then open: http://localhost:8001/maritime_interactive_map.html
```

### Issue: Page won't load at all

**Try:**
1. Clear browser cache (Ctrl+Shift+Delete)
2. Try a different browser
3. Check if Python is installed: `python3 --version`
4. Check if port 8000 is accessible: `netstat -an | grep 8000`

---

## Performance Notes

- **First load:** ~15-20 seconds (loading 75MB of GeoJSON data)
- **Layer toggle:** ~1-2 seconds
- **Click popup:** Instant
- **Browser zoom/pan:** Smooth
- **RAM usage:** ~500-800MB
- **Network:** ~75MB data (cached after first load)

---

## File Sizes

| File | Size | Features |
|------|------|----------|
| 12nm_territorial_sea.geojson | 11 MB | 230 |
| 24nm_contiguous_zone.geojson | 1.9 MB | 220 |
| eez.geojson | 51 MB | 285 |
| fao_fishing_areas.geojson | 12 MB | 370 |
| **Total** | **75 MB** | **1105** |

---

## Advanced Usage

### Change Map Tile Provider

Open `maritime_interactive_map.html` in a text editor and find:

```javascript
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
    maxZoom: 19
}).addTo(map);
```

Replace with alternatives:

**Satellite View:**
```javascript
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri',
    maxZoom: 19
}).addTo(map);
```

**Terrain View:**
```javascript
L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Tiles © OpenTopoMap',
    maxZoom: 17
}).addTo(map);
```

### Add Custom Styles

You can modify layer colors by editing the layer configuration:

```javascript
'territorial_sea': {
    color: '#ff6b6b',        // Change this hex color
    opacity: 0.5,            // Change transparency (0-1)
    fillOpacity: 0.5,        // Change fill transparency
    ...
}
```

---

## Browser Compatibility

| Browser | Status |
|---------|--------|
| Chrome 90+ | ✅ Fully Supported |
| Firefox 88+ | ✅ Fully Supported |
| Safari 14+ | ✅ Fully Supported |
| Edge 90+ | ✅ Fully Supported |
| Internet Explorer | ❌ Not Supported |

---

## Getting Help

If you encounter issues:

1. **Check the browser console** (F12 → Console tab) for error messages
2. **Verify file paths** - Make sure GeoJSON files exist in `maritime_layers/processed_data/`
3. **Use a different browser** - Try Chrome, Firefox, or Safari
4. **Restart the server** - Stop (Ctrl+C) and run the startup script again
5. **Clear cache** - Ctrl+Shift+Delete in most browsers

---

## Next Steps

Once the map is running:

1. **Explore the data** - Toggle different layers and zoom to regions
2. **Click zones** for information about maritime boundaries
3. **Share the map** - The HTML file can be hosted on any web server
4. **Customize** - Modify colors, add new layers, or change the tile provider

---

## Credits

- **Map Library:** Leaflet.js
- **Tile Provider:** OpenStreetMap
- **Data Sources:**
  - 12NM & 24NM: World EEZ boundaries
  - EEZ: UN EEZ database
  - FAO: Food and Agriculture Organization

---

**Happy exploring! 🗺️**

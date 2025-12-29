# 🗺️ QUICK START - Maritime Boundaries Interactive Map

## TL;DR - Get Running in 30 Seconds

### Linux / macOS:
```bash
cd /home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas
chmod +x start_server.sh
./start_server.sh
# Then open: http://localhost:8000/maritime_interactive_map.html
```

### Windows:
```bash
cd "C:\Users\[YourUsername]\Desktop\Deep_Darshak\References\Build_1_docs\Fishing_areas"
start_server.bat
# Then open: http://localhost:8000/maritime_interactive_map.html
```

### Alternative (Any OS):
```bash
cd /home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas
python3 -m http.server 8000
# Then open: http://localhost:8000/maritime_interactive_map.html
```

---

## What You Get

✅ **Interactive Map** - Pan, zoom, click zones  
✅ **4 Layer Types** - Toggle on/off instantly  
✅ **Detailed Popups** - Click any zone for info  
✅ **Beautiful UI** - Professional interface  
✅ **Mobile Friendly** - Works on tablets/phones  

---

## Layers

| Name | Color | Features |
|------|-------|----------|
| 12NM Territorial Sea | 🔴 | 230 zones |
| 24NM Contiguous Zone | 🔵 | 220 zones |
| Exclusive Economic Zone | 🟢 | 285 zones |
| FAO Fishing Areas | 🟠 | 370 areas |

---

## Why a Web Server?

Browser security prevents loading local files directly. Use the startup scripts or `python3 -m http.server` to serve files over HTTP.

---

## Files Included

- `maritime_interactive_map.html` ← **Main file**
- `start_server.sh` - Linux/macOS launcher
- `start_server.bat` - Windows launcher
- `MARITIME_MAP_SETUP.md` - Detailed setup guide
- `maritime_layers/processed_data/` - GeoJSON data files

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Files won't load | Use web server (not file://) |
| Port 8000 in use | `python3 -m http.server 8001` |
| Page blank | Check browser console (F12) |
| Slow loading | Normal (75MB data, ~15-20s first load) |

---

**Need more help?** Read `MARITIME_MAP_SETUP.md`

---

**Ready? Start the server and open:** `http://localhost:8000/maritime_interactive_map.html` 🗺️

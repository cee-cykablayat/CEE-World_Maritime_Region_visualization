# Maritime Single Map Explorer - User Guide

## Overview

The **Maritime Single Map Explorer** notebook provides an interactive web-based interface where you can:

- **View a single persistent map** with all maritime boundary layers loaded
- **Toggle layers on/off** using checkboxes to control what's displayed
- **Click on zones** to see detailed information (territory name, area, sovereign state, etc.)
- **Zoom and pan** the map using standard controls
- **Instantly see updates** when you check/uncheck layers

## How to Run

### Option 1: Using Jupyter Notebook

```bash
cd /home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas
jupyter notebook maritime_single_map_explorer.ipynb
```

Then:
1. Run each cell sequentially (Shift + Enter)
2. The map will appear with checkboxes below it
3. Use the checkboxes to toggle layers

### Option 2: Using JupyterLab

```bash
cd /home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas
jupyter lab maritime_single_map_explorer.ipynb
```

## Notebook Structure

### Cell 1: Import Libraries
- Imports all required packages (folium, geopandas, ipywidgets)
- Sets up paths and imports custom maritime layer classes

### Cell 2: Initialize Base Map
- Creates a single interactive Folium map
- Adds layer controls and legend
- Centers map on world (0°, 0°) with zoom level 2

### Cell 3: Load Maritime Boundary Data
- Loads all 4 maritime boundary datasets:
  - 12NM Territorial Sea (230 zones)
  - 24NM Contiguous Zone (220 zones)
  - Exclusive Economic Zone (285 zones)
  - FAO Fishing Areas (370 areas)

### Cell 4: Create Feature Groups
- Converts each dataset into Folium feature groups
- Each feature group contains all zones with:
  - Appropriate color styling
  - Interactive popups with zone information
  - Hover tooltips

### Cell 5: Create Interactive Controls
- Creates 4 checkboxes (one per layer)
- Stores checkbox references for callback management

### Cell 6: Define Update Callbacks
- Attaches event listeners to checkboxes
- Updates layer visibility when checkboxes change
- Refreshes map display in real-time

### Cell 7: Display Interface
- Creates a beautiful control panel with:
  - Header banner
  - Layer selection checkboxes
  - Information display area
  - Map display area

### Cell 8: Export Map
- Saves the complete interactive map to HTML file
- File can be opened in any web browser

## Features

### 1. Layer Checkboxes
Each layer has a checkbox you can toggle:

```
☐ 12NM Territorial Sea
☐ 24NM Contiguous Zone
☐ Exclusive Economic Zone (EEZ)
☐ FAO Fishing Areas
```

**Behavior**:
- Check the box → layer appears on map
- Uncheck the box → layer disappears from map
- Multiple layers can be shown simultaneously
- Map updates instantly when you toggle

### 2. Color Scheme
Each layer has a distinct color for easy identification:

| Layer | Color | Hex Code |
|-------|-------|----------|
| 12NM Territorial Sea | Red | #ff6b6b |
| 24NM Contiguous Zone | Blue | #1f77b4 |
| Exclusive Economic Zone | Green | #2ca02c |
| FAO Fishing Areas | Multi-color | Ocean-based |

### 3. Interactive Popups
Clicking on any zone displays:

**For Territorial Sea/Contiguous Zone/EEZ:**
- Zone name (GEONAME)
- Territory
- Area (in km²)

**For FAO Fishing Areas:**
- Area name
- Area code
- Ocean (Atlantic, Pacific, Indian, Arctic)
- Status (Major, Minor, etc.)

### 4. Responsive Legend
The map includes a color-coded legend showing all available layers

### 5. Map Controls
Standard Folium controls:
- Zoom in/out buttons (+/-)
- Layer control (toggle visibility)
- Attribution
- Attribution links

## Usage Examples

### Example 1: View Only Territorial Seas
1. Check **12NM Territorial Sea**
2. Leave other checkboxes unchecked
3. Map shows only the 230 territorial sea zones in red

### Example 2: Compare EEZ and FAO Areas
1. Check **Exclusive Economic Zone (EEZ)**
2. Check **FAO Fishing Areas**
3. Map shows both layers, making it easy to see the overlap
4. Uncheck either to remove it

### Example 3: Full Maritime Picture
1. Check all 4 checkboxes
2. Map displays all maritime boundaries
3. Zoom in to a specific region (e.g., Mediterranean)
4. Click zones to see details

## Output Files

### HTML Export
The notebook automatically saves the interactive map:

**File**: `maritime_interactive_single_map.html`
**Location**: `/home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas/`
**Size**: ~1.5 GB (all layers enabled)
**Usage**: Open in any web browser (Chrome, Firefox, Safari, Edge)

## Performance

### Loading Times
- Data loading: ~12 seconds (first time)
- Layer rendering: ~30-45 seconds (depends on selected layers)
- Map updates on toggle: ~1-2 seconds

### Browser Compatibility
- ✓ Chrome/Chromium (recommended)
- ✓ Firefox
- ✓ Safari
- ✓ Edge
- ✓ Opera

### Memory Usage
- Base map: ~100 MB
- With all layers: ~1.5 GB
- Recommended: 4+ GB RAM for smooth operation

## Troubleshooting

### Issue: Map doesn't display
**Solution**: 
- Ensure Jupyter is running with proper kernel
- Run Cell 1 first to set up paths
- Check that all data files exist

### Issue: Slow rendering
**Solution**:
- Use fewer layers at a time
- Zoom in to reduce geometry complexity
- Close other browser tabs

### Issue: Checkboxes don't update map
**Solution**:
- Make sure to run Cell 6 (callback setup)
- Restart kernel if cells run out of order
- Run cells 1-7 sequentially

### Issue: Missing data
**Solution**:
- Run preprocessing script first: `python maritime_layers/preprocessing/preprocess_data.py`
- Verify data files exist in source directories
- Check file permissions

## Advanced Usage

### Modify Layer Colors
Edit Cell 4 to change colors:

```python
folium.GeoJson(
    feature,
    style_function=lambda x: {
        'fillColor': '#YOUR_COLOR',  # Change here
        'color': '#YOUR_OUTLINE',     # And here
        'weight': 1,
        'opacity': 0.7,
        'fillOpacity': 0.5
    }
)
```

### Add Custom Information to Popups
Edit the popup text in Cell 4:

```python
popup=folium.Popup(
    f"<b>{feature['properties'].get('GEONAME')}</b><br>"
    f"<b>NEW INFO:</b> {feature['properties'].get('ANY_FIELD')}<br>"  # Add here
    f"Area: {feature['properties'].get('AREA_KM2'):,} km²",
    max_width=300
)
```

### Change Map Tiles
In Cell 2, modify:

```python
base_map = folium.Map(
    location=[0, 0],
    zoom_start=2,
    tiles='OpenStreetMap'  # Try: 'CartoDB positron', 'CartoDB Voyager', etc.
)
```

### Add More Layers
You can add more maritime boundary datasets by:
1. Creating a new layer class (if needed)
2. Following the pattern in Cell 3
3. Adding a feature group in Cell 4
4. Adding a checkbox in Cell 5

## Key Differences from Other Notebooks

| Feature | Interactive Explorer | Single Map Explorer |
|---------|--------------------|--------------------|
| Number of maps | Creates new map each time | Single persistent map |
| Layer rendering | Sequential | Simultaneous |
| Checkbox effect | Recreates map | Updates visibility |
| Speed | Slower (full re-render) | Faster (toggle only) |
| User experience | Tab-like interface | Real-time toggle |
| Best for | Deep exploration | Quick comparison |

## Support & Questions

For issues or questions:
1. Check the troubleshooting section above
2. Review the maritime_layers documentation
3. Check notebook cell comments for inline documentation
4. Examine the OOP classes in `maritime_layers/utils/map_layers.py`

---

**Created**: December 29, 2025
**Version**: 1.0
**Tested with**: Python 3.12.3, Jupyter Notebook/Lab


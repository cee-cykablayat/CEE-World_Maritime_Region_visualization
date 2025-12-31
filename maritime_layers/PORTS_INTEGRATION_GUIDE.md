# Ports Integration Guide - v1.0.1

## Overview
This guide explains the ports layer integration in the Maritime Boundaries Explorer. The ports layer provides interactive visualization of 106 Indian ports with category-based styling and comprehensive metadata.

## Features

### 📍 Port Categories
The ports layer implements a three-tier categorization system based on data quality and importance:

#### 1. **Major Ports** ⭐ (14 ports)
- Ports with historical/descriptive information
- **Marker Size**: 10px radius
- **Border Style**: Bold black borders (weight: 3)
- **Opacity**: 95% fill opacity
- **Examples**: Beyt Dwarka (Gujarat), JNPT (Maharashtra)
- **Visual Indicator**: ⭐ in tooltip

#### 2. **Verified Ports** ✓ (23 ports)
- Ports with verified source URLs
- **Marker Size**: 7px radius
- **Border Style**: Dark gray borders (weight: 2.5)
- **Opacity**: 85% fill opacity
- **Visual Indicator**: ✓ in tooltip

#### 3. **Regular Ports** • (69 ports)
- Documented ports without additional metadata
- **Marker Size**: 5px radius
- **Border Style**: Medium gray borders (weight: 1.5)
- **Opacity**: 70% fill opacity
- **Visual Indicator**: • in tooltip

### 🎨 State-Based Color Coding
Each port uses the state color from the unified palette:

- **Maharashtra** (#e67e22 - Orange): 45 ports (11 major, 14 verified, 20 regular)
- **Gujarat** (#e74c3c - Red): 33 ports (3 major, 4 verified, 26 regular)
- **Kerala** (#9b59b6 - Purple): 13 ports (0 major, 3 verified, 10 regular)
- **Karnataka** (#3498db - Blue): 10 ports (0 major, 0 verified, 10 regular)
- **Goa** (#27ae60 - Green): 5 ports (0 major, 2 verified, 3 regular)

### 📊 Port Data Structure

Each port feature includes:
```json
{
  "Port_Name": "Port name",
  "state": "State name",
  "location": "Regional location",
  "country": "India",
  "lat": 22.8227,
  "lon": 69.3496,
  "port_category": "major|verified|regular",
  "port_order": 1,
  "type_of_harbor": "Harbor type",
  "also_known_as": "Alternative name",
  "main_trades": "Primary trades",
  "major_exports": "Export commodities",
  "major_imports": "Import commodities",
  "has_description": true,
  "has_source": true
}
```

## Usage

### Accessing the Map

1. **Local Development**:
   ```bash
   cd maritime_layers/visualization
   python -m http.server 8000
   ```
   Then visit: `http://localhost:8000/frontend/maritime_interactive_map.html`

2. **GitHub Repository**:
   Visit your GitHub Pages deployment (if enabled)

### Interacting with Ports Layer

1. **Toggle Visibility**:
   - Check "Port Details & Coordinates" in the sidebar
   - All 106 ports will appear on the map with state-based colors

2. **Inspect Port Details**:
   - Click on any port marker
   - A card popup opens with:
     - Port name and category badge
     - Location details (state, region, coordinates)
     - Harbor type and alternative names
     - Trading information (exports/imports)
     - Establishment year (if available)

3. **Visual Hierarchy**:
   - Larger markers = More important ports (major)
   - Stronger borders = More verified ports
   - Opacity gradient = Confidence/importance ranking

## Data Sources

The ports data (`ports_decimal_coordinates.csv`) contains:
- **Total Ports**: 106 documented Indian ports
- **Source**: Compiled from maritime authority databases
- **Verification**: Cross-referenced with JNPT, SHIMPL, and state port authorities
- **Format**: CSV with lat/lon decimal coordinates

## Technical Implementation

### Files Modified/Created

1. **`maritime_layers/preprocessing/preprocess_ports.py`**
   - Converts CSV to GeoJSON format
   - Analyzes metadata to assign port categories
   - Generates statistics JSON with category breakdown

2. **`maritime_layers/utils/map_layers.py`**
   - `PortsLayer` class with category-aware styling
   - Dynamic marker sizing based on port importance
   - Enhanced popup generation with category badges

3. **`maritime_layers/visualization/frontend/maritime_interactive_map.html`**
   - Port layer checkbox control in sidebar
   - `pointToLayer` function with category-based styling
   - Category indicators in tooltips (⭐/✓/•)
   - Enhanced popup rendering with metadata

4. **`maritime_layers/processed_data/ports.geojson`**
   - 106 features with complete metadata
   - Includes category and styling properties
   - Ready for Leaflet integration

### Styling Logic

```javascript
// Marker size and styling based on category
if (portCategory === 'major') {
    radius = 10;      // Largest markers
    weight = 3;       // Bold borders
    fillOpacity = 0.95; // Most opaque
} else if (portCategory === 'verified') {
    radius = 7;       // Medium markers
    weight = 2.5;
    fillOpacity = 0.85;
} else {
    radius = 5;       // Subtle markers
    weight = 1.5;
    fillOpacity = 0.7;
}
```

## Future Enhancements

- [ ] Port capacity and throughput data
- [ ] Real-time ship movement tracking
- [ ] Port facilities list (cranes, warehouses, etc.)
- [ ] Seasonal traffic patterns
- [ ] Environmental impact data
- [ ] Historical port evolution visualization

## Troubleshooting

### Ports not appearing?
1. Check if "Port Details & Coordinates" checkbox is checked
2. Verify ports.geojson is loaded (check browser console)
3. Ensure HTTP server is running if viewing locally

### Slow map performance?
- Reduce number of visible layers
- Zoom into specific maritime region
- Check browser developer tools for errors

### Data discrepancies?
- Verify source data in ports_decimal_coordinates.csv
- Check port coordinates against official port authority records
- Report issues with specific ports

## Version History

### v1.0.1 (December 31, 2025)
- ✨ Category-based port styling system
- ✨ Enhanced interactive popups with metadata
- ✨ Improved visual hierarchy on map
- 🐛 Fixed port marker sizing
- 📝 Added comprehensive documentation

## Support & Feedback

For issues, suggestions, or data corrections:
1. Check the GitHub repository issues
2. Submit PR with improvements
3. Contact maritime intelligence team

---

**Crimson Energy Experts Pvt. Ltd.**
Maritime Intelligence System

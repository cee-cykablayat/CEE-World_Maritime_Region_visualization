# Maritime Boundaries Interactive Visualization

## Overview

This project provides an object-oriented solution for visualizing and exploring multiple maritime boundary layers interactively. Users can toggle different maritime boundary types on/off using a user-friendly interface.

## Project Structure

```
Fishing_areas/
├── maritime_layers/
│   ├── __init__.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── map_layers.py          # Main OOP classes for layers
│   ├── preprocessing/
│   │   └── preprocess_data.py      # Data preprocessing script
│   └── processed_data/             # Output directory for optimized data
├── maritime_interactive_explorer.ipynb  # Main interactive notebook
├── world_contiguous_zones.ipynb
├── world_territorial_sea.ipynb
├── world_EEZ.ipynb
├── FAO_area_visualization.ipynb
└── World_Boundaries/               # Source geographic data
```

## Features

### 1. Object-Oriented Design

The solution uses a class-based approach with the following key components:

- **MaritimeLayer (Abstract Base Class)**
  - Base class for all maritime boundary layers
  - Defines interface for loading data, creating popups, and styling
  - Provides common functionality like add_to_map() and to_geojson()

- **Concrete Layer Classes**
  - `TerritorialSeaLayer`: 12 Nautical Miles territorial seas (Red)
  - `ContiguousZoneLayer`: 24 Nautical Miles contiguous zones (Blue)
  - `EEZLayer`: Exclusive Economic Zones (Green)
  - `FAOFishingAreaLayer`: FAO fishing areas with ocean-based coloring

- **MaritimeMapController**
  - Manages multiple layers on a single map
  - Handles layer registration, rendering, and map output
  - Supports legend and controls

### 2. Interactive Controls

The `maritime_interactive_explorer.ipynb` notebook provides:

- **Layer Checkboxes**: Toggle each layer on/off independently
- **Real-time Map Updates**: Map updates dynamically when checkboxes change
- **Interactive Popups**: Click on any zone to see detailed information
- **Dynamic Legend**: Shows selected layers and their color schemes

### 3. Data Optimization

The preprocessing pipeline (`preprocess_data.py`) includes:

- **Geometry Simplification**: Reduces file size while maintaining accuracy
- **GeoJSON Conversion**: Exports optimized data for faster loading
- **Statistics Generation**: Creates summary files with layer metadata
- **Batch Processing**: Processes all datasets in one run

## Available Maritime Layers

### 1. 12 Nautical Miles Territorial Sea
- **Source**: World_12NM_v4_20231025_gpkg/eez_12nm_v4.gpkg
- **Color**: Red (#ff6b6b)
- **Features**: ~220 zones
- **Information**: Territory name, sovereign state, area, political type

### 2. 24 Nautical Miles Contiguous Zone
- **Source**: World_24NM_v4_20231025_gpkg/eez_24nm_v4.gpkg
- **Color**: Blue (#1f77b4)
- **Features**: ~220 zones
- **Information**: Territory name, sovereign state, area, political type

### 3. Exclusive Economic Zone (EEZ)
- **Source**: World_EEZ_v12_20231025_gpkg/eez_v12.gpkg
- **Color**: Green (#2ca02c)
- **Features**: 250+ zones
- **Information**: Territory name, sovereign state, area, ISO code

### 4. FAO Fishing Areas
- **Source**: FAO_AREAS_ERASE.json
- **Colors**: Ocean-specific (Arctic, Atlantic, Pacific, Indian, Southern, Mediterranean)
- **Features**: 87 fishing areas
- **Information**: Area name, code, ocean, status, level

## Usage

### 1. Running the Interactive Notebook

```bash
jupyter notebook maritime_interactive_explorer.ipynb
```

**Steps**:
1. Run each cell in order
2. Use the checkboxes to select which layers to display
3. The map updates automatically
4. Click on zones for detailed information

### 2. Using the OOP Classes Directly

```python
from maritime_layers.utils.map_layers import (
    TerritorialSeaLayer,
    MaritimeMapController
)

# Create a layer
territorial_sea = TerritorialSeaLayer()
territorial_sea.load_data('path/to/data.gpkg')

# Create controller and add layer
controller = MaritimeMapController()
controller.add_layer(territorial_sea)
controller.render_layers(['12NM Territorial Sea'])
controller.add_legend()

# Get and display map
map_obj = controller.get_map()
map_obj.save('output.html')
```

### 3. Preprocessing Data

```bash
python maritime_layers/preprocessing/preprocess_data.py
```

This will:
1. Load all geographic data
2. Simplify geometries for faster loading
3. Convert to GeoJSON format
4. Generate statistics files
5. Output optimized files to `processed_data/`

## Performance Optimization Strategies

### 1. Geometry Simplification
- Simplification tolerance: 0.01 degrees
- Reduces file size by 40-60%
- Minimal visual impact for web display

### 2. GeoJSON Format
- More efficient than GeoPackage for web delivery
- Smaller file sizes when simplified
- Better browser compatibility

### 3. Lazy Loading
- Layers are only rendered when selected
- Reduces initial load time
- Smoother user experience

### 4. Feature Group Management
- Each layer managed separately
- Layer control enables/disables rendering
- No redundant rendering

## Output Files

### Generated Files
- `maritime_boundaries_interactive.html`: Full map with all layers
- `processed_data/12nm_territorial_sea.geojson`: Optimized 12NM data
- `processed_data/24nm_contiguous_zone.geojson`: Optimized 24NM data
- `processed_data/eez.geojson`: Optimized EEZ data
- `processed_data/fao_fishing_areas.geojson`: Optimized FAO data
- `processed_data/*_stats.json`: Metadata and statistics

## Advantages of This Approach

1. **Reusability**: Classes can be imported and used in other projects
2. **Extensibility**: Easy to add new maritime boundary types
3. **Maintainability**: Clear separation of concerns
4. **Performance**: Optimized data loading and rendering
5. **User Experience**: Interactive controls for intuitive exploration
6. **Documentation**: Self-documenting code with docstrings

## Extending the System

### Adding a New Layer Type

```python
from maritime_layers.utils.map_layers import MaritimeLayer

class MyCustomLayer(MaritimeLayer):
    def __init__(self):
        super().__init__(
            name="My Custom Layer",
            color="#aabbcc",
            opacity=0.7,
            fill_opacity=0.5
        )
    
    def load_data(self, file_path: str) -> None:
        # Your loading logic
        self.gdf = gpd.read_file(file_path)
        self.geojson_data = json.loads(self.gdf.to_json())
    
    def create_popup(self, feature: Dict) -> str:
        # Your popup logic
        return "<b>Custom Info</b>"
```

## Dependencies

- geopandas
- folium
- ipywidgets (for interactive notebook)
- json
- pandas
- shapely

## Future Enhancements

1. **Web Application**: Convert to Flask/Django web app with REST API
2. **Data Updates**: Automated data refresh from official sources
3. **Search Functionality**: Search zones by country/territory
4. **Comparison Tools**: Compare boundaries between different types
5. **Export Options**: Export selected zones to various formats
6. **Mobile Responsive**: Adapt for mobile/tablet viewing

## Support

For questions or issues, refer to the inline documentation in:
- `maritime_layers/utils/map_layers.py`: Class documentation
- `maritime_layers/preprocessing/preprocess_data.py`: Preprocessing docs
- `maritime_interactive_explorer.ipynb`: Usage examples

---

**Created**: December 2024
**Version**: 1.0

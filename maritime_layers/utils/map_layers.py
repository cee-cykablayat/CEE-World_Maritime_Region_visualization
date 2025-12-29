"""
Maritime Map Layer Classes
Object-oriented approach for managing different maritime boundary layers
"""

import geopandas as gpd
import folium
import json
from abc import ABC, abstractmethod
from typing import Dict, Optional, List
import os


class MaritimeLayer(ABC):
    """Abstract base class for maritime boundary layers"""
    
    def __init__(self, name: str, color: str, opacity: float = 0.5, fill_opacity: float = 0.5):
        self.name = name
        self.color = color
        self.opacity = opacity
        self.fill_opacity = fill_opacity
        self.gdf = None
        self.geojson_data = None
        
    @abstractmethod
    def load_data(self, file_path: str) -> None:
        """Load geographic data from file"""
        pass
    
    @abstractmethod
    def create_popup(self, feature: Dict) -> str:
        """Create popup HTML for feature"""
        pass
    
    def style_function(self, feature: Dict) -> Dict:
        """Default style function"""
        return {
            'fillColor': self.color,
            'color': self.color,
            'weight': 1,
            'opacity': self.opacity,
            'fillOpacity': self.fill_opacity
        }
    
    def add_to_map(self, map_obj: folium.Map) -> None:
        """Add layer to folium map"""
        if self.geojson_data is None:
            raise ValueError(f"GeoJSON data not loaded for {self.name}")
        
        for feature in self.geojson_data['features']:
            folium.GeoJson(
                feature,
                style_function=self.style_function,
                popup=folium.Popup(self.create_popup(feature), max_width=300),
                tooltip=feature['properties'].get('GEONAME', self.name)
            ).add_to(map_obj)
    
    def to_geojson(self, output_path: str) -> None:
        """Export layer to GeoJSON file"""
        if self.geojson_data is None:
            raise ValueError(f"GeoJSON data not loaded for {self.name}")
        
        with open(output_path, 'w') as f:
            json.dump(self.geojson_data, f)
        print(f"✓ Exported {self.name} to {output_path}")


class TerritorialSeaLayer(MaritimeLayer):
    """12 Nautical Miles Territorial Sea Layer"""
    
    def __init__(self):
        super().__init__(
            name="12NM Territorial Sea",
            color="#ff6b6b",  # Red
            opacity=0.7,
            fill_opacity=0.5
        )
    
    def load_data(self, file_path: str) -> None:
        """Load 12NM territorial sea data"""
        print(f"Loading 12NM Territorial Sea from {file_path}...")
        self.gdf = gpd.read_file(file_path)
        self.geojson_data = json.loads(self.gdf.to_json())
        print(f"✓ Loaded {len(self.gdf)} territorial sea zones")
    
    def create_popup(self, feature: Dict) -> str:
        """Create popup for territorial sea"""
        props = feature['properties']
        return f"""
        <div style="font-family: Arial; font-size: 12px; width: 280px;">
        <b style="color: #c92a2a;">{props.get('GEONAME', 'Unknown')}</b><br>
        <hr style="margin: 5px 0;">
        <b>Territory:</b> {props.get('TERRITORY1', 'N/A')}<br>
        <b>Sovereign:</b> {props.get('SOVEREIGN1', 'N/A')}<br>
        <b>Area:</b> {props.get('AREA_KM2', 'N/A'):,} km²<br>
        <b>Type:</b> {props.get('POL_TYPE', 'N/A')}<br>
        <b>Zone Type:</b> 12 Nautical Miles
        </div>
        """


class ContiguousZoneLayer(MaritimeLayer):
    """24 Nautical Miles Contiguous Zone Layer"""
    
    def __init__(self):
        super().__init__(
            name="24NM Contiguous Zone",
            color="#1f77b4",  # Blue
            opacity=0.7,
            fill_opacity=0.5
        )
    
    def load_data(self, file_path: str) -> None:
        """Load 24NM contiguous zone data"""
        print(f"Loading 24NM Contiguous Zone from {file_path}...")
        self.gdf = gpd.read_file(file_path)
        self.geojson_data = json.loads(self.gdf.to_json())
        print(f"✓ Loaded {len(self.gdf)} contiguous zones")
    
    def create_popup(self, feature: Dict) -> str:
        """Create popup for contiguous zone"""
        props = feature['properties']
        return f"""
        <div style="font-family: Arial; font-size: 12px; width: 280px;">
        <b style="color: #0051ba;">{props.get('GEONAME', 'Unknown')}</b><br>
        <hr style="margin: 5px 0;">
        <b>Territory:</b> {props.get('TERRITORY1', 'N/A')}<br>
        <b>Sovereign:</b> {props.get('SOVEREIGN1', 'N/A')}<br>
        <b>Area:</b> {props.get('AREA_KM2', 'N/A'):,} km²<br>
        <b>Type:</b> {props.get('POL_TYPE', 'N/A')}<br>
        <b>Zone Type:</b> 24 Nautical Miles
        </div>
        """


class EEZLayer(MaritimeLayer):
    """Exclusive Economic Zone Layer"""
    
    def __init__(self):
        super().__init__(
            name="Exclusive Economic Zone (EEZ)",
            color="#2ca02c",  # Green
            opacity=0.7,
            fill_opacity=0.4
        )
    
    def load_data(self, file_path: str) -> None:
        """Load EEZ data"""
        print(f"Loading EEZ from {file_path}...")
        self.gdf = gpd.read_file(file_path)
        self.geojson_data = json.loads(self.gdf.to_json())
        print(f"✓ Loaded {len(self.gdf)} EEZ zones")
    
    def create_popup(self, feature: Dict) -> str:
        """Create popup for EEZ"""
        props = feature['properties']
        return f"""
        <div style="font-family: Arial; font-size: 12px; width: 280px;">
        <b style="color: #1b5e20;">{props.get('GEONAME', 'Unknown')}</b><br>
        <hr style="margin: 5px 0;">
        <b>Territory:</b> {props.get('TERRITORY1', 'N/A')}<br>
        <b>Sovereign:</b> {props.get('SOVEREIGN1', 'N/A')}<br>
        <b>Area:</b> {props.get('AREA_KM2', 'N/A'):,} km²<br>
        <b>ISO:</b> {props.get('ISO_TER1', 'N/A')}<br>
        <b>Zone Type:</b> Exclusive Economic Zone
        </div>
        """


class FAOFishingAreaLayer(MaritimeLayer):
    """FAO Fishing Areas Layer"""
    
    # Ocean-specific colors
    OCEAN_COLORS = {
        'Arctic': '#1f77b4',
        'Atlantic': '#ff7f0e',
        'Pacific': '#2ca02c',
        'Indian': '#d62728',
        'Southern': '#9467bd',
        'Mediterranean': '#8c564b'
    }
    
    def __init__(self):
        super().__init__(
            name="FAO Fishing Areas",
            color="#ffa500",  # Orange (default)
            opacity=0.7,
            fill_opacity=0.3
        )
    
    def load_data(self, file_path: str) -> None:
        """Load FAO fishing areas data"""
        print(f"Loading FAO Fishing Areas from {file_path}...")
        self.gdf = gpd.read_file(file_path)
        self.geojson_data = json.loads(self.gdf.to_json())
        print(f"✓ Loaded {len(self.gdf)} FAO fishing areas")
    
    def style_function(self, feature: Dict) -> Dict:
        """Style function based on ocean"""
        props = feature['properties']
        ocean = props.get('OCEAN', 'Arctic')
        color = self.OCEAN_COLORS.get(ocean, '#cccccc')
        
        return {
            'fillColor': color,
            'color': color,
            'weight': 1,
            'opacity': self.opacity,
            'fillOpacity': self.fill_opacity
        }
    
    def create_popup(self, feature: Dict) -> str:
        """Create popup for FAO area"""
        props = feature['properties']
        return f"""
        <div style="font-family: Arial; font-size: 12px; width: 280px;">
        <b style="color: #ff8c00;">{props.get('F_NAME', 'Unknown')}</b><br>
        <hr style="margin: 5px 0;">
        <b>Code:</b> {props.get('F_CODE', 'N/A')}<br>
        <b>Ocean:</b> {props.get('OCEAN', 'N/A')}<br>
        <b>Status:</b> {props.get('F_STATUS', 'N/A')}<br>
        <b>Level:</b> {props.get('F_LEVEL', 'N/A')}
        </div>
        """


class MaritimeMapController:
    """Controller for managing multiple maritime layers on a single map"""
    
    def __init__(self, center: tuple = [0, 0], zoom_start: int = 2):
        self.map = folium.Map(
            location=center,
            zoom_start=zoom_start,
            tiles='OpenStreetMap'
        )
        self.layers: Dict[str, MaritimeLayer] = {}
        self.active_layers: set = set()
        self._setup_controls()
    
    def _setup_controls(self) -> None:
        """Setup layer control"""
        folium.LayerControl().add_to(self.map)
    
    def add_layer(self, layer: MaritimeLayer, active: bool = False) -> None:
        """Add a maritime layer"""
        self.layers[layer.name] = layer
        if active:
            self.active_layers.add(layer.name)
    
    def render_layers(self, layers_to_render: Optional[List[str]] = None) -> None:
        """Render specified layers to map"""
        if layers_to_render is None:
            layers_to_render = list(self.active_layers)
        
        for layer_name in layers_to_render:
            if layer_name in self.layers:
                print(f"Rendering {layer_name}...")
                self.layers[layer_name].add_to_map(self.map)
    
    def add_legend(self) -> None:
        """Add legend to map"""
        legend_html = '''
        <div style="position: fixed; 
                bottom: 50px; right: 50px; width: 300px; height: auto; 
                background-color: white; border:3px solid #333; z-index:9999; 
                font-size:13px; padding: 15px; border-radius: 5px; box-shadow: 2px 2px 6px rgba(0,0,0,0.3);">
        <h3 style="margin-top: 0; color: #333;">Maritime Boundaries</h3>
        <hr style="margin: 10px 0;">
        <p style="margin: 8px 0; font-size: 11px;"><b style="color: #c92a2a;">■</b> 12NM Territorial Sea</p>
        <p style="margin: 8px 0; font-size: 11px;"><b style="color: #0051ba;">■</b> 24NM Contiguous Zone</p>
        <p style="margin: 8px 0; font-size: 11px;"><b style="color: #1b5e20;">■</b> Exclusive Economic Zone</p>
        <p style="margin: 8px 0; font-size: 11px;"><b style="color: #ff7f0e;">■</b> FAO Fishing Areas</p>
        <hr style="margin: 10px 0;">
        <p style="margin: 5px 0; font-size: 10px; color: #666;">Click on any zone for details</p>
        </div>
        '''
        self.map.get_root().html.add_child(folium.Element(legend_html))
    
    def get_map(self) -> folium.Map:
        """Get the folium map object"""
        return self.map
    
    def save(self, output_path: str) -> None:
        """Save map to HTML file"""
        self.map.save(output_path)
        print(f"✓ Map saved to {output_path}")

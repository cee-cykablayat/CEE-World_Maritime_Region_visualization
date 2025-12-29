"""
Data Preprocessing Script
Converts raw geodata to optimized GeoJSON and simplified formats for faster frontend loading
"""

import geopandas as gpd
import json
import os
from pathlib import Path


class DataPreprocessor:
    """Preprocess geographic data for faster loading"""
    
    def __init__(self, base_path: str, output_dir: str = 'processed_data'):
        self.base_path = base_path
        self.output_dir = os.path.join(base_path, 'maritime_layers', output_dir)
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def simplify_geometry(self, gdf, tolerance: float = 0.01):
        """Simplify geometries to reduce file size"""
        print(f"  Simplifying geometries with tolerance {tolerance}...")
        gdf['geometry'] = gdf['geometry'].simplify(tolerance)
        return gdf
    
    def process_12nm_territorial_sea(self, simplify: bool = True):
        """Process 12NM territorial sea data"""
        print("\n" + "="*70)
        print("Processing 12NM Territorial Sea")
        print("="*70)
        
        file_path = os.path.join(
            self.base_path, 'World_Boundaries', 'World_12NM_v4_20231025_gpkg', 'eez_12nm_v4.gpkg'
        )
        
        if not os.path.exists(file_path):
            print(f"✗ File not found: {file_path}")
            return None
        
        print(f"Loading from {file_path}...")
        gdf = gpd.read_file(file_path)
        print(f"✓ Loaded {len(gdf)} features")
        
        if simplify:
            gdf = self.simplify_geometry(gdf)
        
        # Save as GeoJSON
        output_path = os.path.join(self.output_dir, '12nm_territorial_sea.geojson')
        geojson_data = json.loads(gdf.to_json())
        with open(output_path, 'w') as f:
            json.dump(geojson_data, f)
        
        print(f"✓ Saved to {output_path}")
        
        # Save summary statistics
        summary = {
            'name': '12NM Territorial Sea',
            'total_features': len(gdf),
            'total_area_km2': float(gdf['AREA_KM2'].sum()),
            'unique_territories': int(gdf['GEONAME'].nunique()),
            'crs': str(gdf.crs),
            'bounds': gdf.total_bounds.tolist()
        }
        
        stats_path = os.path.join(self.output_dir, '12nm_territorial_sea_stats.json')
        with open(stats_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"✓ Statistics saved to {stats_path}")
        return gdf
    
    def process_24nm_contiguous_zone(self, simplify: bool = True):
        """Process 24NM contiguous zone data"""
        print("\n" + "="*70)
        print("Processing 24NM Contiguous Zone")
        print("="*70)
        
        file_path = os.path.join(
            self.base_path, 'World_Boundaries', 'World_24NM_v4_20231025_gpkg', 'eez_24nm_v4.gpkg'
        )
        
        if not os.path.exists(file_path):
            print(f"✗ File not found: {file_path}")
            return None
        
        print(f"Loading from {file_path}...")
        gdf = gpd.read_file(file_path)
        print(f"✓ Loaded {len(gdf)} features")
        
        if simplify:
            gdf = self.simplify_geometry(gdf)
        
        # Save as GeoJSON
        output_path = os.path.join(self.output_dir, '24nm_contiguous_zone.geojson')
        geojson_data = json.loads(gdf.to_json())
        with open(output_path, 'w') as f:
            json.dump(geojson_data, f)
        
        print(f"✓ Saved to {output_path}")
        
        # Save summary statistics
        summary = {
            'name': '24NM Contiguous Zone',
            'total_features': len(gdf),
            'total_area_km2': float(gdf['AREA_KM2'].sum()),
            'unique_territories': int(gdf['GEONAME'].nunique()),
            'crs': str(gdf.crs),
            'bounds': gdf.total_bounds.tolist()
        }
        
        stats_path = os.path.join(self.output_dir, '24nm_contiguous_zone_stats.json')
        with open(stats_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"✓ Statistics saved to {stats_path}")
        return gdf
    
    def process_eez(self, simplify: bool = True):
        """Process Exclusive Economic Zone data"""
        print("\n" + "="*70)
        print("Processing Exclusive Economic Zone (EEZ)")
        print("="*70)
        
        file_path = os.path.join(
            self.base_path, 'World_EEZ_v12_20231025_gpkg', 'eez_v12.gpkg'
        )
        
        if not os.path.exists(file_path):
            print(f"✗ File not found: {file_path}")
            return None
        
        print(f"Loading from {file_path}...")
        gdf = gpd.read_file(file_path)
        print(f"✓ Loaded {len(gdf)} features")
        
        if simplify:
            gdf = self.simplify_geometry(gdf)
        
        # Save as GeoJSON
        output_path = os.path.join(self.output_dir, 'eez.geojson')
        geojson_data = json.loads(gdf.to_json())
        with open(output_path, 'w') as f:
            json.dump(geojson_data, f)
        
        print(f"✓ Saved to {output_path}")
        
        # Save summary statistics
        summary = {
            'name': 'Exclusive Economic Zone',
            'total_features': len(gdf),
            'total_area_km2': float(gdf['AREA_KM2'].sum()),
            'unique_territories': int(gdf['GEONAME'].nunique()),
            'crs': str(gdf.crs),
            'bounds': gdf.total_bounds.tolist()
        }
        
        stats_path = os.path.join(self.output_dir, 'eez_stats.json')
        with open(stats_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"✓ Statistics saved to {stats_path}")
        return gdf
    
    def process_fao_fishing_areas(self, simplify: bool = True):
        """Process FAO fishing areas data"""
        print("\n" + "="*70)
        print("Processing FAO Fishing Areas")
        print("="*70)
        
        file_path = os.path.join(self.base_path, 'FAO_AREAS_ERASE.json')
        
        if not os.path.exists(file_path):
            print(f"✗ File not found: {file_path}")
            return None
        
        print(f"Loading from {file_path}...")
        gdf = gpd.read_file(file_path)
        print(f"✓ Loaded {len(gdf)} features")
        
        if simplify:
            gdf = self.simplify_geometry(gdf)
        
        # Save as GeoJSON
        output_path = os.path.join(self.output_dir, 'fao_fishing_areas.geojson')
        geojson_data = json.loads(gdf.to_json())
        with open(output_path, 'w') as f:
            json.dump(geojson_data, f)
        
        print(f"✓ Saved to {output_path}")
        
        # Get ocean statistics
        ocean_counts = gdf['OCEAN'].value_counts().to_dict()
        
        # Save summary statistics
        summary = {
            'name': 'FAO Fishing Areas',
            'total_features': len(gdf),
            'unique_oceans': int(gdf['OCEAN'].nunique()),
            'areas_by_ocean': ocean_counts,
            'crs': str(gdf.crs),
            'bounds': gdf.total_bounds.tolist()
        }
        
        stats_path = os.path.join(self.output_dir, 'fao_fishing_areas_stats.json')
        with open(stats_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"✓ Statistics saved to {stats_path}")
        return gdf
    
    def process_all(self, simplify: bool = True):
        """Process all datasets"""
        print("\n" + "="*70)
        print("PROCESSING ALL MARITIME BOUNDARY DATA")
        print("="*70)
        
        self.process_12nm_territorial_sea(simplify)
        self.process_24nm_contiguous_zone(simplify)
        self.process_eez(simplify)
        self.process_fao_fishing_areas(simplify)
        
        print("\n" + "="*70)
        print("✓ ALL DATA PROCESSED SUCCESSFULLY")
        print("="*70)
        print(f"\nProcessed files saved to: {self.output_dir}")
        print(f"File list:")
        for file in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, file)
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
            print(f"  - {file} ({file_size_mb:.2f} MB)")


if __name__ == '__main__':
    base_path = '/home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas'
    
    processor = DataPreprocessor(base_path, output_dir='processed_data')
    processor.process_all(simplify=True)

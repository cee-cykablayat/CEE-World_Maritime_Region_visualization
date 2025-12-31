"""
Ports Data Preprocessor
Converts ports CSV to optimized GeoJSON format for faster frontend loading
"""

import pandas as pd
import json
import os
from pathlib import Path


class PortsPreprocessor:
    """Preprocess ports data to GeoJSON format"""
    
    def __init__(self, base_path: str, output_dir: str = 'processed_data'):
        self.base_path = base_path
        self.output_dir = os.path.join(base_path, 'maritime_layers', output_dir)
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def process_ports(self):
        """Process ports CSV to GeoJSON with enhanced styling"""
        print("\n" + "="*70)
        print("Processing Ports Data with Styling Information")
        print("="*70)
        
        file_path = os.path.join(
            self.base_path, 'maritime_layers', 'processed_data', 'ports_decimal_coordinates.csv'
        )
        
        if not os.path.exists(file_path):
            print(f"✗ File not found: {file_path}")
            return None
        
        print(f"Loading from {file_path}...")
        df = pd.read_csv(file_path)
        print(f"✓ Loaded {len(df)} ports")
        
        # Filter valid coordinates
        df_valid = df[
            (df['lat'].notna()) & 
            (df['lon'].notna()) &
            (df['Port_Name'].notna())
        ].copy()
        
        # Convert to float
        df_valid['lat'] = pd.to_numeric(df_valid['lat'], errors='coerce')
        df_valid['lon'] = pd.to_numeric(df_valid['lon'], errors='coerce')
        df_valid = df_valid.dropna(subset=['lat', 'lon'])
        
        print(f"✓ {len(df_valid)} ports with valid coordinates")
        
        # Create GeoJSON features with styling information
        features = []
        state_port_count = {}  # Track port number within each state
        
        for idx, row in df_valid.iterrows():
            state = str(row.get('state', 'Other'))
            
            # Track port order within state for sequential numbering
            if state not in state_port_count:
                state_port_count[state] = 0
            state_port_count[state] += 1
            port_order = state_port_count[state]
            
            # Determine port category based on metadata
            also_known = str(row.get('also_known_as', '')).strip()
            has_description = pd.notna(row.get('also_known_as')) and also_known not in ['', 'nan', 'None']
            
            source_url = str(row.get('source_url', '')).strip()
            has_source = pd.notna(row.get('source_url')) and source_url not in ['', 'nan', 'None']
            
            # Category: major (has description), verified (has source), or regular
            if has_description:
                port_category = 'major'  # Important/Major ports
            elif has_source:
                port_category = 'verified'  # Verified ports with sources
            else:
                port_category = 'regular'  # Regular/smaller ports
            
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(row['lon']), float(row['lat'])]
                },
                "properties": {
                    "Port_Name": str(row.get('Port_Name', 'Unknown')),
                    "lat": float(row['lat']),
                    "lon": float(row['lon']),
                    "state": state,
                    "location": str(row.get('location', 'N/A')),
                    "country": str(row.get('country', 'India')),
                    "type_of_harbor": str(row.get('type_of_harbor', 'N/A')),
                    "also_known_as": also_known,
                    "opened_in": str(row.get('opened_in', 'N/A')),
                    "main_trades": str(row.get('main_trades', 'N/A')),
                    "major_exports": str(row.get('major_exports', 'N/A')),
                    "major_imports": str(row.get('major_imports', 'N/A')),
                    # New styling properties
                    "port_category": port_category,
                    "port_order": port_order,
                    "has_description": has_description,
                    "has_source": has_source,
                }
            }
            features.append(feature)
        
        # Create FeatureCollection
        geojson_data = {
            "type": "FeatureCollection",
            "features": features
        }
        
        # Save as GeoJSON
        output_path = os.path.join(self.output_dir, 'ports.geojson')
        with open(output_path, 'w') as f:
            json.dump(geojson_data, f, indent=2)
        
        print(f"✓ Saved to {output_path}")
        
        # Save summary statistics with category breakdown
        by_state = df_valid['state'].value_counts().to_dict()
        
        major_count = sum(1 for f in features if f['properties']['port_category'] == 'major')
        verified_count = sum(1 for f in features if f['properties']['port_category'] == 'verified')
        regular_count = sum(1 for f in features if f['properties']['port_category'] == 'regular')
        
        summary = {
            'name': 'Ports Data',
            'total_ports': len(df_valid),
            'ports_by_state': by_state,
            'port_categories': {
                'major_ports': major_count,
                'verified_ports': verified_count,
                'regular_ports': regular_count
            },
            'crs': 'EPSG:4326',
            'bounds': {
                'north': float(df_valid['lat'].max()),
                'south': float(df_valid['lat'].min()),
                'east': float(df_valid['lon'].max()),
                'west': float(df_valid['lon'].min())
            }
        }
        
        stats_path = os.path.join(self.output_dir, 'ports_stats.json')
        with open(stats_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"✓ Statistics saved to {stats_path}")
        print(f"\nPort Categories:")
        print(f"  • Major Ports (with descriptions): {major_count}")
        print(f"  • Verified Ports (with sources): {verified_count}")
        print(f"  • Regular Ports: {regular_count}")
        print(f"\nPorts by State:")
        for state, count in sorted(by_state.items(), key=lambda x: x[1], reverse=True):
            print(f"  {state}: {count} ports")
        
        return df_valid


if __name__ == '__main__':
    base_path = '/home/crimsondeepdarshak/Desktop/Deep_Darshak/References/Build_1_docs/Fishing_areas'
    
    processor = PortsPreprocessor(base_path)
    processor.process_ports()
    
    print("\n" + "="*70)
    print("✓ PORTS DATA PREPROCESSED SUCCESSFULLY")
    print("="*70)

import pandas as pd
from pathlib import Path

def convert_ghcnd_stations_to_csv(input_txt_path_str, output_csv_path_str):
    """
    Reads the fixed-width ghcnd-stations.txt file and converts it to a CSV.
    """
    input_txt_path = Path(input_txt_path_str)
    output_csv_path = Path(output_csv_path_str)

    if not input_txt_path.exists():
        print(f"Error: Input file '{input_txt_path}' not found. Ensure it's in the correct path.")
        return False

    colspecs = [
        (0, 11),   # ID (Station ID)
        (12, 20),  # LATITUDE
        (21, 30),  # LONGITUDE
        (31, 37),  # ELEVATION
        (38, 40),  # STATE (U.S. state or Canadian province code)
        (41, 71),  # NAME (Station Name)
        (72, 75),  # GSN_FLAG (GSN Flag)
        (76, 79),  # HCN_CRN_FLAG (HCN/CRN Flag)
        (80, 85)   # WMO_ID (WMO ID)
    ]
    names = [
        'ID', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'STATE', 'NAME',
        'GSN_FLAG', 'HCN_CRN_FLAG', 'WMO_ID'
    ]

    try:
        df = pd.read_fwf(input_txt_path, colspecs=colspecs, names=names)
        df['NAME'] = df['NAME'].str.strip()
        
        output_csv_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_csv_path, index=False)
        
        print(f"Successfully converted '{input_txt_path.name}' to '{output_csv_path}'. Total rows: {len(df)}")
        return True

    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return False

if __name__ == "__main__":
    input_txt_file = Path("data/raw") / "ghcnd-stations.txt"
    output_csv_file = Path("data/interim") / "gsn_stations.csv" 
    convert_ghcnd_stations_to_csv(input_txt_file, str(output_csv_file))
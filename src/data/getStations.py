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


def convert_ghcnd_countries_to_csv(input_txt_path_str, output_csv_path_str):
    """
    Reads the ghcnd-countries.txt file and converts it to a CSV.
    """
    input_txt_path = Path(input_txt_path_str)
    output_csv_path = Path(output_csv_path_str)

    if not input_txt_path.exists():
        print(f"Error: Input file '{input_txt_path}' not found. Ensure it's in the correct path.")
        return False

    try:
        lines = input_txt_path.read_text().splitlines()
        
        data = []
        for line in lines:
            if not line.strip(): 
                continue
            # Split only on the first whitespace to separate code from full name
            parts = line.strip().split(maxsplit=1) 
            
            country_code = parts[0] if len(parts) > 0 else ''
            country_name = parts[1] if len(parts) > 1 else ''
            
            data.append({'COUNTRY_CODE_FIPS': country_code, 'COUNTRY_NAME': country_name})

        df = pd.DataFrame(data)

        output_csv_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_csv_path, index=False)
        
        print(f"Successfully converted '{input_txt_path.name}' to '{output_csv_path}'. Total countries: {len(df)}")
        return True

    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return False


def combine_stations_with_countries(stations_csv_path_str, countries_csv_path_str, output_csv_path_str):
    """
    Combines station data with country names, placing COUNTRY_NAME and COUNTRY_CODE_FIPS first.
    """
    stations_csv_path = Path(stations_csv_path_str)
    countries_csv_path = Path(countries_csv_path_str)
    output_csv_path = Path(output_csv_path_str)

    if not stations_csv_path.exists():
        print(f"Error: Stations file '{stations_csv_path}' not found.")
        return False
    if not countries_csv_path.exists():
        print(f"Error: Countries file '{countries_csv_path}' not found.")
        return False

    try:
        df_stations = pd.read_csv(stations_csv_path)
        df_countries = pd.read_csv(countries_csv_path)

        station_base_cols = list(df_stations.columns)

        df_stations['COUNTRY_CODE_FIPS'] = df_stations['ID'].str[:2]

        merged_df = pd.merge(df_stations, df_countries, 
                             on='COUNTRY_CODE_FIPS', 
                             how='left')
        
        # Construct the final desired order
        desired_order = ['COUNTRY_NAME', 'COUNTRY_CODE_FIPS'] + station_base_cols
        
        # Select and reorder columns
        merged_df = merged_df[desired_order]

        output_csv_path.parent.mkdir(parents=True, exist_ok=True)
        merged_df.to_csv(output_csv_path, index=False)
        
        print(f"Successfully combined '{stations_csv_path.name}' and '{countries_csv_path.name}'.")
        print(f"Result saved to '{output_csv_path}'. Total records: {len(merged_df)}")
        
        print("\n--- First 5 rows of the combined CSV with desired column order: ---")
        print(merged_df.head())

        return True

    except Exception as e:
        print(f"An error occurred during combination: {e}")
        return False


def filter_gsn_stations(combined_stations_path_str, output_gsn_path_str):
    """
    Filters the combined stations data to include only Global Climate Observing System (GSN) stations.
    """
    combined_stations_path = Path(combined_stations_path_str)
    output_gsn_path = Path(output_gsn_path_str)

    if not combined_stations_path.exists():
        print(f"Error: Combined stations file '{combined_stations_path}' not found.")
        return False

    try:
        df_combined = pd.read_csv(combined_stations_path)

        # Filter rows where GSN_FLAG column is not NaN and its value is 'GSN' (after stripping any whitespace)
        gsn_df = df_combined[df_combined['GSN_FLAG'].notna() & 
                              (df_combined['GSN_FLAG'].astype(str).str.strip() == 'GSN')].copy()
        
        output_gsn_path.parent.mkdir(parents=True, exist_ok=True)
        gsn_df.to_csv(output_gsn_path, index=False)

        print(f"Successfully filtered GSN stations from '{combined_stations_path.name}'.")
        print(f"Result saved to '{output_gsn_path}'. Total GSN stations found: {len(gsn_df)}")
        
        print("\n--- First 5 rows of the GSN stations CSV: ---")
        print(gsn_df.head())

        return True

    except Exception as e:
        print(f"An error occurred during GSN filtering: {e}")
        return False


if __name__ == "__main__":
    input_txt_file = Path("data/raw") / "ghcnd-stations.txt"
    output_csv_file = Path("data/interim") / "ghcnd_stations.csv" 
    convert_ghcnd_stations_to_csv(input_txt_file, str(output_csv_file))

    input_file_path = Path("data") / "raw" / "ghcnd-countries.txt" 
    output_file_path = Path("data") / "interim" / "ghcnd_countries.csv" 
    convert_ghcnd_countries_to_csv(str(input_file_path), str(output_file_path))

    #Note: This code block must run before combining for the next block to be executed without errors
    stations_input = Path("data") / "interim" / "ghcnd_stations.csv"
    countries_input = Path("data") / "interim" / "ghcnd_countries.csv"
    output_combined = Path("data") / "interim" / "stations_with_country_names.csv"
    combine_stations_with_countries(str(stations_input), str(countries_input), str(output_combined))

    #If above code is not run or is faulty, the below code will cause error due to missing combined file
    combined_stations_input = Path("data") / "interim" / "stations_with_country_names.csv"
    output_gsn_stations = Path("data") / "interim" / "gsn_stations.csv"
    filter_gsn_stations(str(combined_stations_input), str(output_gsn_stations))


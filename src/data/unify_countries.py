import pandas as pd
from pathlib import Path
import os 

RAW_DATA_INPUT_DIR = Path("data") / "raw" / "gsoy_data" 
PROCESSED_OUTPUT_FILE = Path("data") / "processed" / "unified_countries.csv"

def combine_raw_gsoy_data():
    """
    Combines all individual GSOY station CSVs (organized by country) into a single consolidated CSV file.
    """
    # 1. Check if input directory exists
    if not RAW_DATA_INPUT_DIR.exists():
        print(f"Error: Raw GSOY data input directory '{RAW_DATA_INPUT_DIR}' not found.")
        print("Ensure data collection has been run and data is stored in this directory.")
        return

    all_station_dfs = [] 
    processed_files_count = 0
    
    print(f"Starting to combine CSV files from '{RAW_DATA_INPUT_DIR}'...")

    for country_dir in RAW_DATA_INPUT_DIR.iterdir(): 
        if country_dir.is_dir(): 
            print(f"  Processing country directory: {country_dir.name}")
            
            for station_file in country_dir.glob("*.csv"): 
                try:
                    df_station = pd.read_csv(station_file)
                    all_station_dfs.append(df_station)
                    processed_files_count += 1
                except Exception as e: 
                    print(f"    Warning: Could not read file '{station_file.name}'. Error: {e}")
    
    if not all_station_dfs:
        print("No CSV files found to combine. Ensure data has been downloaded into the raw data directory.")
        return

    print(f"\nSuccessfully read {processed_files_count} individual station data files.")
    print("Concatenating all data into a single DataFrame...")

    try:
        # 5. Concatenate DataFrames
        combined_df = pd.concat(all_station_dfs, ignore_index=True)
        
        # 6. Ensure Output Directory and Save
        PROCESSED_OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
        combined_df.to_csv(PROCESSED_OUTPUT_FILE, index=False)
                                                                
        print(f"\nAll GSOY data combined and saved to '{PROCESSED_OUTPUT_FILE}'.")
        print(f"Total rows in combined file: {len(combined_df)}")
        print(f"Total columns in combined file: {len(combined_df.columns)}")
        print("\n--- First 5 rows of the combined data: ---")
        print(combined_df.head(3))

    except Exception as e:
        print(f"An error occurred during concatenation or saving: {e}")

if __name__ == "__main__":
    print("Starting GSOY data processing (combination) process...")
    combine_raw_gsoy_data()
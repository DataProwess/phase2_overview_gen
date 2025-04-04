import pandas as pd
import os
from datetime import datetime

def merge_all_csvs(directory, output_filename="merged_output_bauld_all_4th_april.csv"):
    merged_df = pd.DataFrame()  # Empty DataFrame to store merged data

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):  # Process only CSV files
                file_path = os.path.join(root, file)
                try:
                    df = pd.read_csv(file_path, delimiter='|', encoding='utf-8', low_memory=False, dtype=str)
                    merged_df = pd.concat([merged_df, df], ignore_index=True)  # Merge CSVs
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    # Generate timestamped output file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    final_output_file = f"{output_filename.replace('.csv', '')}_{timestamp}.csv"
    merged_df.to_csv(final_output_file, index=False, encoding='utf-8', sep='|')  # Save merged data
    
    print(f"Merged {len(merged_df)} rows into {final_output_file}")

if __name__ == "__main__":
    input_directory = "Bauld_Files_Complete"  # Change this to your target folder
    merge_all_csvs(input_directory)

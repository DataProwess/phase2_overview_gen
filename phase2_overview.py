import pandas as pd
from collections import defaultdict
import argparse
import os
from datetime import datetime

def process_csv(input_file, output_folder):
    # Read the input file
    df = pd.read_csv(input_file, sep='|', dtype=str)
    
    # Initialize dictionary to store aggregated data
    folder_data = defaultdict(lambda: {'size': 0, 'subfolders': set(), 'files': 0})
    
    for _, row in df.iterrows():
        directory = row['DirectoryName']
        size = int(row['Length']) if row['Length'].isdigit() else 0
        
        # Extract Drive and Top-Level Folder
        parts = directory.split('\\')
        if len(parts) >= 2:
            drive = parts[0] + '\\' + parts[1]
            top_level_folder = parts[2] if len(parts) > 2 else 'Not Applicable'
        else:
            drive = directory
            top_level_folder = 'Not Applicable'
        
        # Update dictionary
        folder_key = (drive, top_level_folder)
        folder_data[folder_key]['size'] += size
        folder_data[folder_key]['subfolders'].add(directory)
        folder_data[folder_key]['files'] += 1
    
    # Prepare the output data
    output_rows = [['Server_Name', 'Drive', 'Top Level Folder', 'Data(GB)', 'Number of SubFolders', 'Number of Files']]
    for (drive, folder), data in folder_data.items():
        output_rows.append([
            'SGSIN021MF6001P',  # Fixed Server_Name
            drive,
            folder,
            round(data['size'] / (1024**3), 2),  # Convert size to GB
            len(data['subfolders']),
            data['files']
        ])
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_folder, f'output_{timestamp}.csv')
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        for row in output_rows:
            f.write('|'.join(map(str, row)) + '\n')
    
    print(f"Output file saved at: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a pipe-separated CSV and generate a summary file.")
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("output_folder", help="Path to the output folder")
    
    args = parser.parse_args()
    process_csv(args.input_csv, args.output_folder)

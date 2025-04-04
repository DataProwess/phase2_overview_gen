import pandas as pd
import csv
from collections import defaultdict
import argparse
import os
import time
from datetime import datetime

def write_log(message, log_path):
    print(message)
    with open(log_path, 'a', encoding='utf-8') as log:
        log.write(message + '\n')

def process_csv(file_identity, input_file, output_folder):
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(output_folder, f"process_log_{timestamp}.txt")
    error_log_file = os.path.join(output_folder, f"error_log_{timestamp}.txt")

    try:
        write_log(f"Starting processing: {input_file}", log_file)

        # Read the input file
        # df = pd.read_csv(input_file, sep='|', dtype=str, quotechar='"')
        df = pd.read_csv(
            input_file,
            sep='|',
            dtype=str,
            quoting=csv.QUOTE_NONE,
            engine='python',
            keep_default_na=False,
            na_values=[''],
            on_bad_lines='warn'
        )


        # Extract Server Name from the first row
        server_name = df.iloc[0]['ServerName'] if 'ServerName' in df.columns else 'Unknown'

        # Dictionary to store aggregated data
        folder_data = defaultdict(lambda: {'size': 0, 'subfolders': set(), 'files': 0})

        for _, row in df.iterrows():
            # Skip empty rows
            if row.isnull().all():
                write_log(f"Skipping empty row {_}: {row.to_dict()}", log_file)
                continue

            # Check for missing 'DirectoryName' values
            if pd.isna(row['DirectoryName']):
                write_log(f"Skipping row {_} due to missing DirectoryName: {row.to_dict()}", log_file)
                continue

            directory = str(row['DirectoryName']).strip('\\')
            size = int(row['Length']) if str(row['Length']).isdigit() else 0

            # Extract Drive and Top-Level Folder
            parts = directory.split('\\')

            if len(parts) >= 2:
                drive = f"\\\\{parts[0]}\\{parts[1]}"
                top_level_folder = parts[2] if len(parts) > 2 else 'Not Applicable'
            else:
                drive = directory
                top_level_folder = 'Not Applicable'

            folder_key = (drive, top_level_folder)

            # Add all subfolders beyond Top-Level, excluding files
            if len(parts) > 3:
                subfolders = ['\\'.join(parts[3:i+1]) for i in range(3, len(parts))]
                if '.' in parts[-1]:  
                    subfolders.pop()
                folder_data[folder_key]['subfolders'].update(subfolders)

            # Update dictionary
            folder_data[folder_key]['size'] += size
            folder_data[folder_key]['files'] += 1

        # Prepare the output data
        output_rows = [['"Server_Name"', '"Drive"', '"Top Level Folder"', '"Data(GB)"', '"Number of SubFolders"', '"Number of Files"']]
        for (drive, folder), data in folder_data.items():
            output_rows.append([
                f'"{server_name}"',
                f'"{drive}"',
                f'"{folder}"',
                f'"{round(data["size"] / (1024**3), 2)}"',
                f'"{len(data["subfolders"])}"',
                f'"{data["files"]}"'
            ])

        # Ensure output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Generate timestamped filename
        output_file = os.path.join(output_folder, f'overview_{file_identity}_{timestamp}.csv')

        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            for row in output_rows:
                f.write('|'.join(row) + '\n')

        end_time = time.time()
        execution_time = round(end_time - start_time, 2)
        write_log(f"Processing completed in {execution_time} seconds. Output saved at: {output_file}", log_file)
        write_log(f"[{datetime.now()}] Processed: {input_file}, Execution Time: {execution_time} seconds", log_file)
        write_log(f"Log written to: {log_file}", log_file)

    except Exception as e:
        error_message = f"[{datetime.now()}] Error processing {input_file}: {str(e)}"
        write_log("An error occurred. Check the error log for details.", error_log_file)
        write_log(error_message, error_log_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a pipe-separated CSV and generate a summary file.")
    parser.add_argument("file_identity", help="A unique identifier for the output file")
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("output_folder", help="Path to the output folder")

    args = parser.parse_args()
    process_csv(args.file_identity, args.input_csv, args.output_folder)

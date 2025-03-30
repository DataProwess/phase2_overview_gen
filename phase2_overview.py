import pandas as pd
from collections import defaultdict
import argparse
import os
import time
from datetime import datetime

def process_csv(input_file, output_folder, file_identity):
    start_time = time.time()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(output_folder, f"process_log_{timestamp}.txt")
    error_log_file = os.path.join(output_folder, f"error_log_{timestamp}.txt")

    try:
        print(f"Starting processing: {input_file}")

        # Read the input file
        df = pd.read_csv(input_file, sep='|', dtype=str)

        # Extract Server Name from the first row
        server_name = df.iloc[0]['ServerName'] if 'ServerName' in df.columns else 'Unknown'

        # Dictionary to store aggregated data
        folder_data = defaultdict(lambda: {'size': 0, 'subfolders': set(), 'files': 0})

        for _, row in df.iterrows():
            directory = row['DirectoryName'].strip('\\')
            size = int(row['Length']) if row['Length'].isdigit() else 0

            # Extract Drive and Top-Level Folder
            parts = directory.split('\\')

            if len(parts) >= 2:
                # drive = f"\\{parts[0]}\\{parts[1]}"  # Drive
                drive = f"\\\\{parts[0]}\\{parts[1]}"  # Drive
                top_level_folder = parts[2] if len(parts) > 2 else 'Not Applicable'
            else:
                drive = directory
                top_level_folder = 'Not Applicable'

            folder_key = (drive, top_level_folder)

            # Add all subfolders beyond Top-Level, excluding files
            if len(parts) > 3:
                subfolders = ['\\'.join(parts[3:i+1]) for i in range(3, len(parts))]
                # Remove the last entry if it's a file (has an extension)
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
                f'"{round(data["size"] / (1024**3), 2)}"',  # Convert size to GB
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
        print(f"Processing completed in {execution_time} seconds. Output saved at: {output_file}")

        # Log execution time
        with open(log_file, 'a', encoding='utf-8') as log:
            log.write(f"[{datetime.now()}] Processed: {input_file}, Execution Time: {execution_time} seconds\n")

        print(f"Log written to: {log_file}")

    except Exception as e:
        error_message = f"[{datetime.now()}] Error processing {input_file}: {str(e)}\n"
        print("An error occurred. Check the error log for details.")
        with open(error_log_file, 'a', encoding='utf-8') as error_log:
            error_log.write(error_message)
        print(f"Error log written to: {error_log_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a pipe-separated CSV and generate a summary file.")
    parser.add_argument("file_identity", help="A unique identifier for the output file")
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("output_folder", help="Path to the output folder")
    

    args = parser.parse_args()
    process_csv(args.file_identity, args.input_csv, args.output_folder)


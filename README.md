# CSV Processing Script

This Python script processes a pipe-separated CSV file and generates a summary report containing details about the drive, top-level folder, total data size, number of subfolders, and number of files.

## Features
- Reads a `|` (pipe)-separated CSV file.
- Extracts and summarizes drive, top-level folder, data size (GB), number of subfolders, and file count.
- Handles errors and logs execution details.
- Saves the output as a new CSV file in the specified output folder.

## Prerequisites
- Python 3.x
- Pandas library (`pip install pandas`)

## Usage

### Run the script:
```sh
python script.py <input_csv> <output_folder>
```

### Example:
```sh
python phase2_overview.py "D:\phase2_overview_gen\files\MOD_File_Discovery_abi_ev1_rerun_20250329_205710 - Copy.csv" "D:\phase2_overview_gen\files"
```
This will process `data.csv` and generate an output file inside the `output/` folder.

## Output Format
The script generates a CSV file with the following columns:
```
"Server_Name"|"Drive"|"Top Level Folder"|"Data(GB)"|"Number of SubFolders"|"Number of Files"
```

## Logs
- A log file (`process_log_<timestamp>.txt`) is created in the output folder.
- An error log (`error_log_<timestamp>.txt`) is also generated in case of errors.

## Notes

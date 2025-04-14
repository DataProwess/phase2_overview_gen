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
    ```sh
    pip install pandas
    ```

- Make sure to run this command on powershell
    ```sh
    Set-ExecutionPolicy Bypass -Scope Process -Force
    ```

- Make sure that **LongPathsEnabled** is enabled in **regedit**:

    #### How to Enable Long Paths in Windows

    1. Press `Win + R`, type `regedit`, and press **Enter**.
    2. Navigate to the following key:
        ```
        HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
        ```
    3. In the right pane:
        - Look for a DWORD value named `LongPathsEnabled`.
        - If it doesn’t exist, right-click and choose **New → DWORD (32-bit) Value**, then name it `LongPathsEnabled`.
    4. Double-click `LongPathsEnabled`, set the **Value data** to `1`, and click **OK**.

## Usage

## Notes
- Always Check folder access before running FileDetailAnalysis_on_individual_path.ps1 script

### Run the script for Check_access.ps1:
```sh
.\Check_access.ps1 <path of folder to be scanned>
```

### Example:
```sh
.\Check_access.ps1 "C:\folder\sub_folder"
```

### Run the script for FileDetailAnalysis_on_individual_path.ps1:
```sh
.\FileDetailAnalysis_on_individual_path.ps1 -vserver_name <> -path <path of folder to be scanned> -OutputFolder <path of the output folder>
```

### Example:
```sh
.\FileDetailAnalysis_on_individual_path.ps1 -vserver_name "svm_prod_abi_cifs_01" -path "C:\folder\sub_folder" -OutputFolder "D:\folder\output_folder"
```
### For Longer Paths i.e 300 characters long, Run the script for FileDetailAnalysis_on_individual_path.ps1 but make sure to map the fileshare in "This PC":

### Example:
```sh
.\FileDetailAnalysis_on_individual_path.ps1 -vserver_name "svm_prod_abi_cifs_01" -path "\\?\C:\folder\sub_folder" -OutputFolder "D:\folder\output_folder"
```


### For Error paths in Error Log, Run the script for FileDetailAnalysis_on_csv_batch_file.ps1 for Batch processing on the problematic paths from error log after cleaning it and transferring it into csv file with the header name as "path":

### Run the script for FileDetailAnalysis_on_csv_batch_file.ps1:
```sh
.\FileDetailAnalysis_on_csv_batch_file.ps1 -vserver_name <> -CSVPath <path to errorlog csv file> -OutputFolder <path of the output folder>
```

### Example:
```sh
.\FileDetailAnalysis_on_csv_batch_file.ps1 -vserver_name "svm_prod_abi_cifs_01" -CSVPath "C:\path to\error log csv file" -OutputFolder "D:\folder\output_folder"
```

### Run the script:
```sh
python phase2_overview.py <file idenitty> <input_csv> <output_folder>
```

### Example:
```sh
python phase2_overview.py "file idenitty(give as per your convenience)" "D:\folder\input.csv" "D:\folder\output_folder"
```

## Output Format
The script generates a CSV file with the following columns:
```
"Server_Name"|"Drive"|"Top Level Folder"|"Data(GB)"|"Number of SubFolders"|"Number of Files"
```

## Logs
- A log file (`process_log_<timestamp>.txt`) is created in the output folder.
- An error log (`error_log_<timestamp>.txt`) is also generated in case of errors.




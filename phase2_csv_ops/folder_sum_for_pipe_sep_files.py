import pandas as pd
from datetime import datetime
import os

def sum_length_all_csvs(directory):
    total_length = 0  # Store cumulative total length

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                file_path = os.path.join(root, file)
                try:
                    df = pd.read_csv(file_path, delimiter='|', low_memory=False, dtype=str)
                    # total_length += df['Length'].sum()
                    df['Length'] = pd.to_numeric(df['Length'], errors='coerce')  # Convert to numeric, set invalid values to NaN
                    total_length += df['Length'].sum(skipna=True)  # Sum while ignoring NaN values

                except (KeyError, ValueError):
                    pass  # Ignore files without 'Length' column

    # Convert to KB, MB, GB
    kb = total_length / 1024
    mb = kb / 1024
    gb = mb / 1024

    # Generate output file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"total_length_summary_{input_directory}_{timestamp}.txt"

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"Total Length Sum Across All CSVs: {total_length} Bytes\n")
        file.write(f"Total Length Sum Across All CSVs: {kb:.2f} KB\n")
        file.write(f"Total Length Sum Across All CSVs: {mb:.2f} MB\n")
        file.write(f"Total Length Sum Across All CSVs: {gb:.2f} GB\n")

    print(f"Total Length Sum Across All CSVs: {total_length} Bytes")
    print(f"Total Length Sum Across All CSVs: {kb:.2f} KB")
    print(f"Total Length Sum Across All CSVs: {mb:.2f} MB")
    print(f"Total Length Sum Across All CSVs: {gb:.2f} GB")
    print(f"Summary written to {output_file}")

if __name__ == "__main__":
    input_directory = "rama_3" # Change this to your target folder
    sum_length_all_csvs(input_directory)

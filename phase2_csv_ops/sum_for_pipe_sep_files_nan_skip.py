import pandas as pd
from datetime import datetime
import os

def sum_length_column(input_file):
    try:
        df = pd.read_csv(input_file, delimiter='|', low_memory=False)  # Disable dtype warning
        df['Length'] = pd.to_numeric(df['Length'], errors='coerce')  # Convert non-numeric to NaN
        total_length = df['Length'].sum(skipna=True)  # Sum ignoring NaNs
    except (KeyError, ValueError):
        total_length = 0  

    kb = total_length / 1024
    mb = kb / 1024
    gb = mb / 1024

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    input_filename = os.path.splitext(os.path.basename(input_file))[0]
    output_file = f"output_{input_filename}_{timestamp}.txt"

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"Total Length Sum for {input_filename}: {total_length} Bytes\n")
        file.write(f"Total Length Sum for {input_filename}: {kb:.2f} KB\n")
        file.write(f"Total Length Sum for {input_filename}: {mb:.2f} MB\n")
        file.write(f"Total Length Sum for {input_filename}: {gb:.2f} GB\n")

    print(f"Total Length Sum for {input_filename}: {total_length} Bytes")
    print(f"Total Length Sum for {input_filename}: {kb:.2f} KB")
    print(f"Total Length Sum for {input_filename}: {mb:.2f} MB")
    print(f"Total Length Sum for {input_filename}: {gb:.2f} GB")
    print(f"Total length sum has been written to {output_file}")



if __name__ == "__main__":
    input_csv = "File_Discovery_bauld_archive_bauldarch1_d_archive_nswact2_20250401_051233.csv"  # Change this to your actual file path
    sum_length_column(input_csv)
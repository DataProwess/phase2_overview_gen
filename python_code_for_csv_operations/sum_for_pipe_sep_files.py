import pandas as pd
from datetime import datetime
import os
import argparse

def sum_length_column(input_file):
    try:
        df = pd.read_csv(input_file, delimiter='|', dtype=str)  # Read all columns as strings
        df['Length'] = df['Length'].str.replace('"', '', regex=True).astype(float)  # Remove quotes and convert to float
        total_length = df['Length'].sum()
    except (KeyError, ValueError):
        total_length = 0  # Handle missing or invalid values
    
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
    parser = argparse.ArgumentParser(description="Calculate sum of Length column in a CSV file.")
    parser.add_argument("input_csv", help="Path to the input CSV file")
    args = parser.parse_args()
    
    sum_length_column(args.input_csv)

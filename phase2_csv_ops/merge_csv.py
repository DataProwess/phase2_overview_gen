import os
import pandas as pd
from glob import glob
import argparse

def merge_large_csvs(folder_path, output_file, sep="|", chunksize=100000):
    csv_files = glob(os.path.join(folder_path, "*.csv"))
    
    if not csv_files:
        print("No CSV files found in the folder.")
        return
    
    with open(output_file, "w", encoding="utf-8", newline='') as out_file:
        header_written = False
        for file in csv_files:
            print(f"Processing {file}...")
            for chunk in pd.read_csv(file, sep=sep, encoding="utf-8", chunksize=chunksize, low_memory=False):
                chunk.to_csv(out_file, sep=sep, index=False, header=not header_written, mode="a", lineterminator='\n')
                header_written = True  # Write header only once
    
    print(f"Merged {len(csv_files)} CSV files into {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge all pipe-separated CSV files in a folder into a single output file.")
    parser.add_argument("input_folder", type=str, help="Path to the folder containing CSV files")
    parser.add_argument("output_file", type=str, help="Path to save the merged CSV file")
    
    args = parser.parse_args()
    merge_large_csvs(args.input_folder, args.output_file)

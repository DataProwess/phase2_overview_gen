import pandas as pd
import sys
import os

def split_csv(input_file, output_prefix="python_split", max_rows=500000):
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    # Read the CSV in chunks
    chunk_iter = pd.read_csv(input_file, chunksize=max_rows)
    
    for i, chunk in enumerate(chunk_iter):
        output_file = f"{output_prefix}_part{i+1}.csv"
        chunk.to_csv(output_file, index=False)
        print(f"Saved: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_csv.py <full_path_to_csv>")
    else:
        input_file = sys.argv[1]
        split_csv(input_file)

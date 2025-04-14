import pandas as pd
import sys
import os

def split_csv(input_file, output_prefix=None, max_rows=500000):
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    # Extract filename without extension
    base_filename = os.path.splitext(os.path.basename(input_file))[0]
    
    # Set output prefix if not provided
    if output_prefix is None:
        output_prefix = base_filename

    # Read the CSV in chunks, specifying the pipe ('|') as the delimiter
    chunk_iter = pd.read_csv(input_file, chunksize=max_rows, encoding="utf-8", sep="|", dtype=str)
    
    for i, chunk in enumerate(chunk_iter):
        output_file = f"{output_prefix}_part{i+1}.csv"
        chunk.to_csv(output_file, index=False, encoding="utf-8", sep="|")  # Preserve pipe delimiter
        print(f"Saved: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_csv.py <full_path_to_pipe_separated_csv>")
    else:
        input_file = sys.argv[1]
        split_csv(input_file)

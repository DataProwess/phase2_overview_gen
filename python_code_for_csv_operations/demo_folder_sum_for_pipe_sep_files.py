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
                    # for index, row in df.iterrows():
                    #     try:
                    #         df.at[index, 'Length'] = pd.to_numeric(row['Length'])
                    #     except Exception as e:
                    #         print(f"Error in file: {file_path} at line {index + 1}, value: {row['Length']}")
                    #         print(f"Error details: {e}")
                    for index, row in df.iterrows():
                        try:
                            value = row['Length']
                            num_value = pd.to_numeric(value)  # Try converting the value
                        except Exception as e:
                            print(f"❌ Error in file: {file_path} at line {index + 1}, value: {value}")
                            print(f"Error details: {e}")
                            


                    # df['Length'] = pd.to_numeric(df['Length'], errors='coerce')  # Convert to numeric, set invalid values to NaN
                    total_length += df['Length'].sum(skipna=True)  # Sum while ignoring NaN values

                except (KeyError, ValueError):
                    pass  # Ignore files without 'Length' column

    # Convert to KB, MB, GB
    kb = total_length / 1024
    mb = kb / 1024
    gb = mb / 1024

    # Generate output file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"total_length_summary_{timestamp}.txt"

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
    input_directory = "Bauld_Files"  # Change this to your target folder
    sum_length_all_csvs(input_directory)

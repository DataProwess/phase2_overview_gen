import pandas as pd

def filter_csv(input_file):
    # Read the CSV file with '|' as the delimiter
    df = pd.read_csv(input_file, delimiter='|', dtype=str)
    
    # Filter out rows where 'FullName' contains 'HomeDirs'
    df_filtered = df[~df['FullName'].str.contains('HomeDirs', na=False, case=False)]
    
    # Generate output file name
    output_file = input_file.replace('.csv', '_EXCLUDING_HOMEDIRS.csv')
    
    # Save the filtered DataFrame to a new CSV file with UTF-8 encoding
    df_filtered.to_csv(output_file, index=False, sep='|', encoding='utf-8')
    
    print(f"Filtered CSV saved to {output_file}")

# Example usage
input_csv = "File_Discovery_abi_ev1_share_20250323_180500.csv"  # Replace with your actual file path
filter_csv(input_csv)

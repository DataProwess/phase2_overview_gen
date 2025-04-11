import os

def count_csv_files(directory):
    csv_count = 0
    for root, _, files in os.walk(directory):
        csv_count += sum(1 for file in files if file.lower().endswith('.csv'))
    return csv_count

if __name__ == "__main__":
    folder_path = r"D:\phase2_overview_gen\phase2_csv_ops\Bauld_Files_Complete"  # Set your folder path here
    if os.path.isdir(folder_path):
        total_csv_files = count_csv_files(folder_path)
        print(f"Total CSV files found: {total_csv_files}")
    else:
        print("Invalid folder path. Please enter a valid directory.")

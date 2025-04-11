import os
import shutil

# Define source and destination folders
source_folder = r"D:\phase2_overview_gen\phase2_csv_ops\Civil Tenders Archive"
destination_folder = r"D:\phase2_overview_gen\phase2_csv_ops\civil_tenders_indi"

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Walk through all subdirectories and files in the source folder
for root, _, files in os.walk(source_folder):
    for file in files:
        if file.endswith(".csv"):  # Only process CSV files
            src_path = os.path.join(root, file)
            dest_path = os.path.join(destination_folder, file)

            # If a file with the same name exists, rename it to avoid overwriting
            counter = 1
            while os.path.exists(dest_path):
                name, ext = os.path.splitext(file)
                new_filename = f"{name}_{counter}{ext}"
                dest_path = os.path.join(destination_folder, new_filename)
                counter += 1

            # Copy the file
            shutil.copy2(src_path, dest_path)
            print(f"Copied: {src_path} → {dest_path}")

print("CSV file copy completed!")

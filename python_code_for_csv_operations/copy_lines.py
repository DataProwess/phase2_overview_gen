import codecs

# Define the source and destination file paths
source_file = "merged_bauld_ind.csv"  # Change this to your actual file
output_file = "File_Discovery_output_file_errors.csv"  # Pipe-separated CSV output

# Define line range
start_line = 32138   # Start copying from this line 
end_line = 32150    # Stop copying at this line

# Define the header row
header = "ServerName|FullName|Date Created|Date Modified|Owner|Authors|Last Saved By|Length|Extension|Attributes|DirectoryName|Name"

# Open source file and write selected lines to a new file
with codecs.open(source_file, "r", encoding="utf-8") as infile, \
     codecs.open(output_file, "w", encoding="utf-8") as outfile:

    # Write the header first
    outfile.write(header + "\n")

    for current_line_number, line in enumerate(infile, start=1):
        if start_line <= current_line_number <= end_line:
            # Convert spaces or tabs to pipe-separated format
            formatted_line = "|".join(line.strip().split())  
            outfile.write(formatted_line + "\n")
        if current_line_number > end_line:
            break  # Stop reading once we reach the end line

print(f"Lines {start_line} to {end_line} copied to {output_file} with the header successfully!")

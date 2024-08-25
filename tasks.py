import string
import random
import os


# Ensure the file is saved in a safe location
safe_directory = os.path.expanduser('~/difficult_files')
os.makedirs(safe_directory, exist_ok=True)
file_path = os.path.join(safe_directory, difficult_filename)

# Write 50 lines to the file
write_lines_to_file(file_path)

print(f'File with difficult name created at: {file_path}')

import os
import re

def remove_last_period(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                old_path = os.path.join(root, file)
                
                # Use regular expression to replace the last period in the file name
                new_file = re.sub(r'(\d+)\.(\d+)\.(\d+)\.', r'\1.\2.\3 ', file, 1)
                new_path = os.path.join(root, new_file)
                
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: {file} to {new_file}")

# Get the directory where the script is located
script_directory = os.path.dirname(__file__)

# Remove the last period in file names in the script directory and its subdirectories
remove_last_period(script_directory)


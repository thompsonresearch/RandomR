import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Initialize the Tkinter root
root = tk.Tk()
root.withdraw()  # Hide the main window

# Prompt the user to select the source directory
source_dir = filedialog.askdirectory(title='Select Source Directory')

# Prompt the user to select the destination directory
destination_dir = filedialog.askdirectory(title='Select Destination Directory')

# Ensure both directories are selected
if source_dir and destination_dir:
    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(root, file)
            
            # Define the destination file path
            destination_file_path = os.path.join(destination_dir, file)
            
            # Copy the file to the destination directory
            shutil.copy(file_path, destination_file_path)

    print("Files have been copied successfully.")
else:
    print("Operation cancelled: Source and/or destination directory was not selected.")

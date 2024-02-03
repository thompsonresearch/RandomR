import arcpy
import tkinter as tk
from tkinter import filedialog

# Function to select shapefile directory or individual shapefiles
def select_shapefiles():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Prompt the user to choose between selecting a folder or files
    choice = input("Type 'folder' to select a folder, or 'files' to select individual shapefiles: ").lower()

    if choice == 'folder':
        folder_path = filedialog.askdirectory(title="Select Folder Containing Shapefiles")
        arcpy.env.workspace = folder_path
        shapefiles = arcpy.ListFeatureClasses()
    elif choice == 'files':
        file_path = filedialog.askopenfilenames(title="Select Shapefiles", filetypes=(("Shapefiles", "*.shp"),))
        shapefiles = list(file_path)
    else:
        print("Invalid choice. Please type 'folder' or 'files'.")
        return None, None

    return shapefiles, choice

# Main function to perform the merge
def merge_shapefiles():
    shapefiles, choice = select_shapefiles()

    if shapefiles and choice:
        # Output location and name for the merged shapefile
        output_shapefile = filedialog.asksaveasfilename(defaultextension=".shp", filetypes=[("Shapefiles", "*.shp")], title="Save the Merged Shapefile As")
        
        # Check if user cancelled the save operation
        if output_shapefile:
            # Merge shapefiles
            arcpy.Merge_management(inputs=shapefiles, output=output_shapefile)
            print(f"Merge completed successfully. Output saved to: {output_shapefile}")
        else:
            print("Merge operation cancelled.")
    else:
        print("No shapefiles selected. Exiting...")

# Run the merge function
merge_shapefiles()

import os

folder_path = "/Users/egloo/Library/Application Support/minecraft/fabric/resourcepacks/subtly emissive/assets/minecraft/textures/entity/fish"  # Replace "path_to_folder" with the actual folder path

# Get the list of files in the folder
file_list = os.listdir(folder_path)

# Iterate through each file in the folder
for file_name in file_list:
    # Create the new file name by adding "_e" to the original name
    new_file_name = file_name.split(".")[0] + "_e." + file_name.split(".")[1]

    # Construct the absolute paths for the original and new file names
    original_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, new_file_name)

    # Rename the file
    os.rename(original_file_path, new_file_path)

print("File renaming complete!")

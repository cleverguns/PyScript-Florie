import os
import shutil
import time

# Define source and destination paths
desktop_path = os.path.expanduser("~/Desktop")
destination_path = "D:/YourDestinationFolder"  # Replace with your actual destination folder

# Define the path for the log file in the destination folder
log_file = os.path.join(destination_path, "copy_log.txt")

# List of folders to copy from the desktop
folders_to_copy = ["Folder1", "Folder2", "Folder3"]  # Replace with your folder names

def copy_folder(src, dest):
    try:
        shutil.copytree(src, dest)
        return True
    except Exception as e:
        return False, str(e)

# Perform the copying and log the results
with open(log_file, "a") as log:
    log.write(f"Copy operation started at {time.ctime()}\n")
    for folder_name in folders_to_copy:
        src_folder = os.path.join(desktop_path, folder_name)
        dest_folder = os.path.join(destination_path, folder_name)
        
        success, error_message = copy_folder(src_folder, dest_folder)
        
        if success:
            log.write(f"Successfully copied {folder_name} to {destination_path} at {time.ctime()}\n")
        else:
            log.write(f"Failed to copy {folder_name} to {destination_path}: {error_message} at {time.ctime()}\n")
    
    log.write(f"Copy operation completed at {time.ctime()}\n")

# Print a success message
print("Copy operation completed successfully.")

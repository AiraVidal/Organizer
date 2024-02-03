import os
import shutil

def organize_files():
    # Get the current script's directory
    current_directory = os.getcwd()

    # Source folder is the current directory
    source_folder = current_directory

    # Destination folder is a subfolder called "Organized"
    destination_folder = os.path.join(current_directory, "Organized")

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List all files in the source folder
    files = os.listdir(source_folder)

    for file in files:
        # Build the full path to the file
        file_path = os.path.join(source_folder, file)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(file)

            # Remove the dot from the extension (optional)
            file_extension = file_extension[1:]

            # Create a folder for the extension if it doesn't exist
            extension_folder = os.path.join(destination_folder, file_extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            # Build the destination path for the file
            destination_path = os.path.join(extension_folder, file)

            # Move the file to the destination folder
            shutil.move(file_path, destination_path)

if __name__ == "__main__":
    organize_files()

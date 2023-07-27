import os
import shutil

def file_organizer(source_folder, destination_folder):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    for file in files:
        # Get the full path of the file
        source_file_path = os.path.join(source_folder, file)

        if os.path.isfile(source_file_path):
            # Extract the file extension
            _, file_extension = os.path.splitext(file)

            # Create a directory for the file extension if it doesn't exist
            destination_extension_folder = os.path.join(destination_folder, file_extension[1:])
            if not os.path.exists(destination_extension_folder):
                os.makedirs(destination_extension_folder)

            # Move the file to the corresponding extension folder
            destination_file_path = os.path.join(destination_extension_folder, file)
            shutil.move(source_file_path, destination_file_path)

if __name__ == "__main__":
    source_folder = "Downloads"
    destination_folder = "Downloads"
    file_organizer(source_folder, destination_folder)
    print("File organization complete.")

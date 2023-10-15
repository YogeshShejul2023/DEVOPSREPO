import os
import sys
import shutil
from datetime import datetime

def backup_files(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print("Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        destination_file = os.path.join(destination_dir, filename)

        if os.path.exists(destination_file):
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename, file_extension = os.path.splitext(filename)
            new_filename = f"{filename}_{timestamp}{file_extension}"
            destination_file = os.path.join(destination_dir, new_filename)

        try:
            shutil.copy(source_file, destination_file)
            print(f"Copied '{source_file}' to '{destination_file}'")
        except Exception as e:
            print(f"Error copying '{source_file}': {e}")

if len(sys.argv) != 3:
    print("Usage: python backup.py <source_directory> <destination_directory>")
else:
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    backup_files(source_dir, destination_dir)
import os
import sys
import shutil
from datetime import datetime

if len(sys.argv) != 3:
    print("Usage: python backup.py <source_directory> <destination_directory>")
else:
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]

    if not os.path.exists(source_dir):
        print("Oops! The source directory '", source_dir, "' doesn't exist.")
    else:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            destination_file = os.path.join(destination_dir, filename)

            if os.path.exists(destination_file):
                filename, file_extension = os.path.splitext(filename)
                new_filename = filename + "_" + timestamp + file_extension
                destination_file = os.path.join(destination_dir, new_filename)

            try:
                shutil.copy(source_file, destination_file)
                print("Backup: '", source_file, "' -> '", destination_file, "'")
            except Exception as e:
                print("An error occurred while copying '", source_file, "':", e)

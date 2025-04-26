import os

def delete_duplicates(dir1, dir2):
    """Delete files in dir1 that also exist in dir2."""
    # List files in both directories
    files_in_dir1 = set(os.listdir(dir1))
    files_in_dir2 = set(os.listdir(dir2))

    # Find common files
    duplicates = files_in_dir1.intersection(files_in_dir2)

    # Delete common files from dir1
    for file in duplicates:
        file_path = os.path.join(dir1, file)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

# Get user input for directories
dir1 = input("Enter the path of the first directory: ").strip()
dir2 = input("Enter the path of the second directory: ").strip()

# Validate directories
if not os.path.isdir(dir1) or not os.path.isdir(dir2):
    print("Error: One or both paths are not valid directories.")
else:
    delete_duplicates(dir1, dir2)
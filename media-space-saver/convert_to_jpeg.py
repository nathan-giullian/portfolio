# run with this script - python convert_to_jpeg.py
import os
import subprocess
from concurrent.futures import ProcessPoolExecutor

def convert_file(input_file):
    # Change output file extension to .jpeg
    output_file = os.path.splitext(input_file)[0] + '.jpeg'
    try:
        # Use 'magick' to convert the file to JPEG format
        subprocess.run(['magick', input_file, output_file], check=True)
        print(f"Converted: {input_file} to {output_file}")
        # Remove the original file after successful conversion
        os.remove(input_file)
        print(f"Deleted original file: {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file}: {e}")

def find_and_convert(directory, max_workers=4):
    # File extensions to search for
    extensions = ['.png', '.heic', '.bmp', '.arw', '.nef', '.dng', '.tiff', '.gif']
    files_to_convert = []

    # Traverse the directory recursively
    for root, _, files in os.walk(directory):
        for file in files:
            # Check if the file has an allowed extension
            if any(file.lower().endswith(ext) for ext in extensions):
                files_to_convert.append(os.path.join(root, file))

    # Use a ProcessPoolExecutor for parallel processing
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        executor.map(convert_file, files_to_convert)

if __name__ == "__main__":
    # Prompt the user for a directory
    directory = input("Enter the directory to search for image files: ").strip()
    find_and_convert(directory)
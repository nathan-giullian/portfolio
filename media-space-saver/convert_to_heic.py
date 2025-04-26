# run with this script - python convert_to_heic.py
import os
import subprocess
from concurrent.futures import ProcessPoolExecutor

def convert_file(input_file):
    output_file = os.path.splitext(input_file)[0] + '.heic'
    try:
        # Use a list with individual arguments to avoid issues with spaces in paths
        subprocess.run(['magick', input_file, output_file], check=True)
        print(f"Converted: {input_file} to {output_file}")
        os.remove(input_file)
        print(f"Deleted original file: {input_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file}: {e}")

def find_and_convert(directory, max_workers=4):
    extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.arw', '.nef', '.dng']
    files_to_convert = []

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                files_to_convert.append(os.path.join(root, file))

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        executor.map(convert_file, files_to_convert)

if __name__ == "__main__":
    directory = input("Enter the directory to search for PNG and JPG files: ").strip()
    find_and_convert(directory)
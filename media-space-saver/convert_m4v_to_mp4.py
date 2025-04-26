# run with this script - python convert_m4v_to_mp4.py
import os
import shutil

def convert_m4v_to_mp4(directory):
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.m4v'):
                # Get the full path of the M4V file
                m4v_file = os.path.join(root, file)
                # Create the new MP4 file path
                mp4_file = os.path.splitext(m4v_file)[0] + '.mp4'
                
                try:
                    # Rename the file to change the extension
                    shutil.move(m4v_file, mp4_file)
                    print(f"Converted: {m4v_file} to {mp4_file}")
                except Exception as e:
                    print(f"Error converting {m4v_file}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory to search for M4V files: ").strip()
    convert_m4v_to_mp4(directory)
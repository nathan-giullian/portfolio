# run with this script - python convert_to_h265.py
import os
import subprocess

def convert_to_h264(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mov', '.mkv', '.avi', '.wmv', '.mod', '.m4v', '.3g2', '.3gp')):
                input_file = os.path.join(root, file)
                output_file = os.path.splitext(input_file)[0] + '_h265.mp4'

                # Convert the video using FFmpeg
                try:
                    subprocess.run(['ffmpeg', '-i', input_file, '-c:v', 'libx265', '-crf', '28', output_file], check=True)
                    print(f"Converted: {input_file} to {output_file}")

                    # Delete the original file after successful conversion
                    os.remove(input_file)
                    print(f"Deleted original file: {input_file}")

                except subprocess.CalledProcessError as e:
                    print(f"Error converting {input_file}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory to search for video files: ").strip()
    convert_to_h264(directory)
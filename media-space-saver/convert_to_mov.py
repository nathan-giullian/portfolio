# run with this script - python convert_to_h264.py
import os
import subprocess

def convert_to_iphone_mov(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mkv', '.avi', '.wmv', '.mod', '.m4v', '.3g2', '.3gp', '.mpg', '.mp4')):
                input_file = os.path.join(root, file)
                output_file = os.path.splitext(input_file)[0] + '.mov'

                # Get original file's access and modification times
                stat = os.stat(input_file)
                atime = stat.st_atime
                mtime = stat.st_mtime

                try:
                    # Convert the video using FFmpeg to HEVC in MOV container
                    subprocess.run([
                        'ffmpeg', '-i', input_file,
                        '-map_metadata', '0',  # Copy as much metadata as possible
                        '-c:v', 'libx265', '-tag:v', 'hvc1', '-crf', '28',
                        '-c:a', 'aac', '-b:a', '128k',
                        output_file
                    ], check=True)
                    print(f"Converted: {input_file} to {output_file}")

                    # Use exiftool to copy all metadata from the original to the new file
                    subprocess.run([
                        'exiftool',
                        '-overwrite_original',
                        f'-TagsFromFile', input_file,
                        '-all:all',
                        output_file
                    ], check=True)
                    print(f"Copied metadata from {input_file} to {output_file}")

                    # Set the output file's times to match the original
                    os.utime(output_file, (atime, mtime))

                    # Delete the original file after successful conversion
                    os.remove(input_file)
                    print(f"Deleted original file: {input_file}")

                except subprocess.CalledProcessError as e:
                    print(f"Error converting {input_file}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory to search for video files: ").strip()
    convert_to_iphone_mov(directory)
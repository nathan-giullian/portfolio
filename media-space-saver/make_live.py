import os
from makelive import make_live_photo

def make_live_photos_in_directory(directory):
    """
    For each pair of files in the directory with matching names (ignoring extension),
    use the makelive package to create a Live Photo.
    """
    # Supported image and video extensions for Live Photos
    image_exts = {'.jpg', '.jpeg', '.heic'}
    video_exts = {'.mov', '.mp4'}

    # Map base filename (without extension) to files
    files_by_base = {}

    for file in os.listdir(directory):
        base, ext = os.path.splitext(file)
        ext = ext.lower()
        if ext in image_exts or ext in video_exts:
            files_by_base.setdefault(base, []).append((ext, os.path.join(directory, file)))

    for base, items in files_by_base.items():
        image_file = None
        video_file = None
        for ext, path in items:
            if ext in image_exts:
                image_file = path
            elif ext in video_exts:
                video_file = path
        if image_file and video_file:
            print(f"Creating Live Photo for: {image_file} + {video_file}")
            try:
                # makelive.make_live_photo(image_path, video_path, output_image_path=None, output_video_path=None)
                make_live_photo(image_file, video_file)
                print(f"Live Photo created for: {image_file} and {video_file}")
            except Exception as e:
                print(f"Error creating Live Photo for {image_file} and {video_file}: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory containing image/video pairs: ").strip()
    make_live_photos_in_directory(directory)
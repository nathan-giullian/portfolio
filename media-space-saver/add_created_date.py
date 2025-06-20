import os
import json
import datetime

def strip_all_extensions(filename):
    """Remove all extensions from a filename (e.g., IMG_1234.jpg.supplem.json -> IMG_1234)."""
    while True:
        base, ext = os.path.splitext(filename)
        if ext:
            filename = base
        else:
            break
    return filename

def update_created_date_from_json(directory):
    """
    For each JSON file in the directory, find the matching media file (by filename with all extensions removed)
    and update its created date using the 'photoTakenTime' or 'creationTime' from the JSON metadata (Google Takeout format).
    Handles both .json and .supplem.json endings. If successful, delete the JSON file.
    """
    print(f"Scanning directory: {directory}")
    # Build a mapping from base filename (no extensions) to media file path
    media_files = {}
    for file in os.listdir(directory):
        if not (file.lower().endswith('.json') or file.lower().endswith('.supplem.json') or file.lower().endswith('.supplemental-metadata.json')):
            base = strip_all_extensions(file)
            media_files[base] = os.path.join(directory, file)
    print(f"Found {len(media_files)} media files.")

    for file in os.listdir(directory):
        if file.lower().endswith('.json') or file.lower().endswith('.supplem.json'):
            json_path = os.path.join(directory, file)
            print(f"\nProcessing JSON file: {json_path}")
            base_name = strip_all_extensions(file)
            print(f"Base name for matching: {base_name}")
            # Find the media file with the same base name
            media_path = media_files.get(base_name)
            if media_path:
                print(f"Found matching media file: {media_path}")
                if os.path.exists(media_path):
                    try:
                        with open(json_path, 'r', encoding='utf-8') as f:
                            metadata = json.load(f)
                        taken_time = None
                        if 'photoTakenTime' in metadata and 'timestamp' in metadata['photoTakenTime']:
                            taken_time = int(metadata['photoTakenTime']['timestamp'])
                            print(f"Found photoTakenTime: {taken_time}")
                        elif 'creationTime' in metadata and 'timestamp' in metadata['creationTime']:
                            taken_time = int(metadata['creationTime']['timestamp'])
                            print(f"Found creationTime: {taken_time}")
                        else:
                            print("No valid timestamp found in JSON metadata.")
                        if taken_time:
                            os.utime(media_path, (taken_time, taken_time))
                            print(f"Updated {media_path} with created date {datetime.datetime.fromtimestamp(taken_time)}")
                            os.remove(json_path)
                            print(f"Deleted JSON metadata file: {json_path}")
                    except Exception as e:
                        print(f"Error processing {json_path} or updating {media_path}: {e}")
                else:
                    print(f"Media file does not exist: {media_path}")
            else:
                print(f"No matching media file found for base name: {base_name}")

if __name__ == "__main__":
    directory = input("Enter the directory containing Google Takeout JSON and media files: ").strip()
    update_created_date_from_json(directory)
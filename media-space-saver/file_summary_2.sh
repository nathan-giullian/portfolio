# run with this script - ./file_summary_2.sh /Volumes/plexshare/Movies (of course update the file path to the volume)
#!/bin/bash

# Check if the directory is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

DIR=$1

# Check if the provided argument is a valid directory
if [ ! -d "$DIR" ]; then
  echo "Error: $DIR is not a valid directory."
  exit 1
fi

# Find files and get their types and sizes
echo "Analyzing files in directory: $DIR"

find "$DIR" -type f | while read -r file; do
  filename=$(basename -- "$file")
  ext="${filename##*.}"
  if [ "$filename" = "$ext" ]; then
    ext="(no extension)"
  else
    ext=$(echo "$ext" | tr '[:upper:]' '[:lower:]')
  fi
  size=$(stat -f%z "$file")
  echo "$ext $size $file"
done | awk '
  {
    count[$1]++;
    size[$1] += $2;
    if (count[$1] == 1) {
      path[$1] = $3;
    } else {
      path[$1] = "";
    }
  }
  END {
    for (ext in count) {
      printf "File type: %-15s Count: %-10d Total Size: %d bytes\n", ext, count[ext], size[ext];
      if (count[ext] == 1) {
        printf "  File path: %s\n", path[ext];
      }
    }
  }
'
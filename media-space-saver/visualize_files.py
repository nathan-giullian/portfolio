import matplotlib.pyplot as plt

# Data from user
data = {
    "3g2": {"count": 1, "size": 347940},
    "AVI": {"count": 22, "size": 501246105},
    "wmv": {"count": 2, "size": 1916633},
    "mov": {"count": 21, "size": 245615861},
    "amr": {"count": 1, "size": 5001},
    "jpeg": {"count": 104, "size": 192986477},
    "MOD": {"count": 12, "size": 88337112},
    "JPG": {"count": 4386, "size": 6885947138},
    "3gp": {"count": 7, "size": 2941213},
    "NEF": {"count": 29, "size": 591867336},
    "MP": {"count": 448, "size": 1087669286},
    "icns": {"count": 1, "size": 5956},
    "bmp": {"count": 71, "size": 90772194},
    "PNG": {"count": 336, "size": 424225193},
    "mp4": {"count": 829, "size": 39406386623},
    "JPEG": {"count": 7, "size": 6059050},
    "tiff": {"count": 2, "size": 311985},
    "html": {"count": 1, "size": 0},
    "m4v": {"count": 2, "size": 12325914},
    "heic": {"count": 46, "size": 66459768},
    "MP4": {"count": 2135, "size": 8359792028},
    "avi": {"count": 12, "size": 371624140},
    "MOV": {"count": 1171, "size": 47773908413},
    "DS_Store": {"count": 9, "size": 1138724},
    "webp": {"count": 1, "size": 27842},
    "gif": {"count": 61, "size": 188702468},
    "TMP": {"count": 1, "size": 1385175},
    "jpg": {"count": 26317, "size": 23056648237},
    "HEIC": {"count": 6717, "size": 14005153884},
    "ARW": {"count": 498, "size": 12461604864},
    "png": {"count": 230, "size": 168516987},
    "db": {"count": 31, "size": 290326528}
}

# Categorize file types
photo_types = {"jpeg", "jpg", "png", "bmp", "gif", "tiff", "heic", "webp", "NEF", "ARW", "icns"}
video_types = {"mp4", "mov", "avi", "3gp", "3g2", "m4v", "wmv", "MOD"}

photos = {ftype: data[ftype] for ftype in data if ftype in photo_types and data[ftype]['size'] > 0}
videos = {ftype: data[ftype] for ftype in data if ftype in video_types and data[ftype]['size'] > 0}

# Convert sizes to megabytes
for ftype in photos:
    photos[ftype]['size'] /= 1048576  # 1 MB = 1048576 bytes

for ftype in videos:
    videos[ftype]['size'] /= 1048576  # 1 MB = 1048576 bytes

# Prepare data for plotting
categories = ['Photos', 'Videos']
counts = [sum(photos[ftype]['count'] for ftype in photos), sum(videos[ftype]['count'] for ftype in videos)]
sizes = [sum(photos[ftype]['size'] for ftype in photos), sum(videos[ftype]['size'] for ftype in videos)]

# Plotting the data
fig, ax1 = plt.subplots()

color = 'tab:blue'
ax1.set_xlabel('Category')
ax1.set_ylabel('Count', color=color)
ax1.bar(categories, counts, color=color, alpha=0.6, label='Count')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Total Size (MB)', color=color)
ax2.bar(categories, sizes, color=color, alpha=0.6, label='Size')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Counts and Sizes of Photos and Videos (in MB)')
plt.show()
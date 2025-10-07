import csv
import os
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, "input.csv")

theme_sums = defaultdict(float)
theme_counts = defaultdict(int)

with open(CSV_FILE, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        theme = row.get("theme", "").strip()
        value = row.get("current_value_used", "").replace(",", "")
        if theme and value:
            try:
                theme_sums[theme] += float(value)
                theme_counts[theme] += 1
            except ValueError:
                pass  # skip rows with invalid numbers

for theme in theme_sums:
    total = theme_sums[theme]
    count = theme_counts[theme]
    avg = total / count if count else 0
    print(f"{theme}: Total Value = {total:.2f}, Count = {count}, Average Value = {avg:.2f}")
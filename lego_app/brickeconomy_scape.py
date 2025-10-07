import requests
import csv
import os

api_key = os.getenv("BRICKECONOMY_API_KEY")
print(f"Using API key: {api_key}")

headers = {
    "accept": "application/json",
    "x-apikey": api_key,
    "User-Agent": "BrickEconomyDataScript/1.0"
}

BASE_URL = "https://www.brickeconomy.com/api/v1"
# Always use the directory where the script is located for CSV_FILE
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, "input.csv")

def get_set_info(set_num):
    url = f"{BASE_URL}/set/{set_num}"
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print(f"Failed to fetch set info: {resp.status_code} {resp.text}")
        return None
    try:
        return resp.json()
    except Exception as e:
        print(f"Error decoding JSON for set info {set_num}: {e}")
        print("Response text:", resp.text)
        return None

def read_csv(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows, reader.fieldnames

def write_csv(filename, rows, fieldnames):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    rows, fieldnames = read_csv(CSV_FILE)
    updated = False

    for row in rows:
        if row.get("complete", "").upper() != "TRUE":
            set_num = row["set_number"]
            print(f"Processing set {set_num}...")
            response = get_set_info(set_num)
            if response and "data" in response:
                data = response["data"]
                row["name"] = data.get("name", "")
                row["pieces_count"] = data.get("pieces_count", "")
                row["minifigs_count"] = data.get("minifigs_count", "")
                row["retail_price_us"] = data.get("retail_price_us", "")
                row["current_value_new"] = data.get("current_value_new", "")
                row["current_value_used"] = data.get("current_value_used", "")
                row["current_value_used_low"] = data.get("current_value_used_low", "")
                row["current_value_used_high"] = data.get("current_value_used_high", "")
                row["released_date"] = data.get("released_date", "")
                row["retired_date"] = data.get("retired_date", "")
                row["theme"] = data.get("theme", "")
                row["subtheme"] = data.get("subtheme", "")
                row["complete"] = "TRUE"
                updated = True
            else:
                print(f"Could not fetch data for set {set_num}. Skipping.")
    if updated:
        write_csv(CSV_FILE, rows, fieldnames)
        print("CSV updated with new data.")
    else:
        print("No updates made to CSV.")
# LEGO App

This folder contains scripts and data files to help you analyze and manage your LEGO collection.

## Contents

- `analysis.py` — Analyze your LEGO set data and generate useful insights.
- `brickeconomy_scape.py` — Scrape data from BrickEconomy for LEGO set values and details.
- `input.csv` — Enter your LEGO set numbers in the `set_number` column. All other fields can be left blank; scripts will attempt to fill them in automatically.
- `sample.json` — Example output or sample data for reference.

## Getting Started

1. **Enter your LEGO set numbers:**  
   Open `input.csv` and add your set numbers in the first column (`set_number`). Leave other fields empty.

2. **Run the analysis:**  
   Use the provided Python scripts to fetch data and analyze your collection.

   ```bash
   python analysis.py
   ```

   or

   ```bash
   python brickeconomy_scape.py
   ```

3. **Review results:**  
   The scripts will update your CSV or generate output files with details about your sets.

## Requirements

- Python 3.x
- Required packages (see script headers for details)

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Set your BrickEconomy API key as an environment variable:
    ```bash
    export BRICKECONOMY_API_KEY=your_api_key_here
    ```

3. Run the scripts as described above.

## Notes

- Make sure to back up your data before running scripts.
- The scripts are designed to help automate the process of gathering and analyzing LEGO set information.

## License

This project is for personal use and learning.  
Feel free to modify and improve!

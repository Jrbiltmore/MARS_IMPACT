# 3D_Modeling_Project/scripts/export_data.py

import pandas as pd
import json
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levellevelname)s - %(message)s'))
logger = logging.getLogger()
file_handler = logging.FileHandler('export_data.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levellevelname)s - %(message)s'))
logger.addHandler(file_handler)

def export_to_csv(data, output_path):
    """Export data to a CSV file."""
    try:
        df = pd.DataFrame(data)
        df.to_csv(output_path, index=False)
        logger.info(f"Data exported to CSV at {output_path}")
    except Exception as e:
        logger.error(f"Error exporting data to CSV: {e}")
        raise

def export_to_json(data, output_path):
    """Export data to a JSON file."""
    try:
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Data exported to JSON at {output_path}")
    except Exception as e:
        logger.error(f"Error exporting data to JSON: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export simulation data to different formats.")
    parser.add_argument('--input', type=str, required=True, help="Path to the simulation data JSON file.")
    parser.add_argument('--csv', type=str, required=False, help="Path to save the data as a CSV file.")
    parser.add_argument('--json', type=str, required=False, help="Path to save the data as a JSON file.")

    args = parser.parse_args()

    try:
        with open(args.input, 'r') as f:
            data = json.load(f)

        if args.csv:
            export_to_csv(data, args.csv)
        if args.json:
            export_to_json(data, args.json)
    except Exception as e:
        logger.error(f"Failed to export data: {e}")

# 3D_Modeling_Project/scripts/export_results.py

import pandas as pd
import json
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
file_handler = logging.FileHandler('export_results.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def load_processed_data(file_path):
    """Load processed data from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        logger.info(f"Processed data loaded from {file_path}")
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Error reading JSON file: {file_path}")
        raise

def export_to_csv(processed_data, output_path):
    """Export processed data to a CSV file."""
    try:
        df = pd.DataFrame(processed_data)
        df.to_csv(output_path, index=False)
        logger.info(f"Processed data exported to {output_path}")
    except IOError:
        logger.error(f"Error exporting processed data to {output_path}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export processed simulation data to CSV.")
    parser.add_argument('--input', type=str, required=True, help="Path to the processed data JSON file.")
    parser.add_argument('--output', type=str, required=True, help="Path to save the exported CSV file.")

    args = parser.parse_args()

    try:
        data = load_processed_data(args.input)
        export_to_csv(data, args.output)
    except Exception as e:
        logger.error(f"Failed to export data: {e}")

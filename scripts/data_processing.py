# 3D_Modeling_Project/scripts/data_processing.py

import numpy as np
import json
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
file_handler = logging.FileHandler('data_processing.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def load_simulation_data(file_path):
    """Load simulation data from a CSV file."""
    try:
        data = np.loadtxt(file_path, delimiter=',', skiprows=1)
        logger.info(f"Simulation data loaded from {file_path}")
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except ValueError:
        logger.error(f"Error reading CSV file: {file_path}")
        raise

def process_data(data):
    """Process the simulation data to extract relevant information."""
    try:
        height_map = data[:, 2]  # Assuming height data is in the third column
        impact_location = data[np.argmax(height_map), :2]  # X, Y location of the highest point
        processed_data = {
            'height_map': height_map.tolist(),
            'impact_location': impact_location.tolist()
        }
        logger.info("Data processed successfully.")
        return processed_data
    except IndexError:
        logger.error("Error processing data: Index out of range.")
        raise

def save_processed_data(processed_data, output_path):
    """Save processed data to a JSON file."""
    try:
        with open(output_path, 'w') as f:
            json.dump(processed_data, f, indent=4)
        logger.info(f"Processed data saved to {output_path}")
    except IOError:
        logger.error(f"Error saving processed data to {output_path}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process simulation data for the comet impact simulation.")
    parser.add_argument('--input', type=str, required=True, help="Path to the input CSV file.")
    parser.add_argument('--output', type=str, required=True, help="Path to save the processed data JSON file.")

    args = parser.parse_args()

    try:
        data = load_simulation_data(args.input)
        processed_data = process_data(data)
        save_processed_data(processed_data, args.output)
    except Exception as e:
        logger.error(f"Failed to process data: {e}")

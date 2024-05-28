# 3D_Modeling_Project/scripts/preprocess_data.py

import json
import pandas as pd
import numpy as np
from PIL import Image, UnidentifiedImageError
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_topography_map(file_path):
    """Load the topography map image."""
    try:
        topo_map = Image.open(file_path)
        logging.info(f"Topography map loaded from {file_path}")
        return topo_map
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except UnidentifiedImageError:
        logging.error(f"Cannot identify image file: {file_path}")
        raise

def process_impact_data(file_path):
    """Load and process the impact data CSV file."""
    try:
        impact_data = pd.read_csv(file_path)
        logging.info(f"Impact data loaded from {file_path}")
        return impact_data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except pd.errors.EmptyDataError:
        logging.error(f"No data in file: {file_path}")
        raise
    except pd.errors.ParserError:
        logging.error(f"Error parsing CSV file: {file_path}")
        raise

def save_json(data, file_path):
    """Save the processed data to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Processed data saved to {file_path}")
    except IOError:
        logging.error(f"Cannot write to file: {file_path}")
        raise

def preprocess_data():
    """Preprocess data for the comet impact simulation."""
    # Define file paths
    topo_map_path = '../data/mars_topography_map.png'
    impact_data_path = '../data/impact_data.csv'
    processed_data_path = '../data/processed_data.json'
    
    # Load and process data
    topo_map = load_topography_map(topo_map_path)
    impact_data = process_impact_data(impact_data_path)
    
    # Example data processing
    processed_data = {
        "entry_point": [150, 200],
        "exit_point": [400, 500],
        "impact_data_summary": impact_data.describe().to_dict()
    }
    
    # Save the processed data
    save_json(processed_data, processed_data_path)

if __name__ == "__main__":
    try:
        preprocess_data()
        logging.info("Data preprocessing completed successfully.")
    except Exception as e:
        logging.error(f"Data preprocessing failed: {e}")

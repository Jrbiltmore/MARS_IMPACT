# 3D_Modeling_Project/scripts/analyze_results.py

import pandas as pd
import json
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
file_handler = logging.FileHandler('analyze_results.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def load_simulation_output(file_path):
    """Load simulation output data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Simulation output data loaded from {file_path}")
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except pd.errors.EmptyDataError:
        logger.error(f"No data in file: {file_path}")
        raise
    except pd.errors.ParserError:
        logger.error(f"Error parsing CSV file: {file_path}")
        raise

def analyze_data(data):
    """Analyze simulation output data."""
    try:
        summary_stats = data.describe()
        logger.info("Data analysis completed successfully.")
        return summary_stats
    except Exception as e:
        logger.error(f"Error analyzing data: {e}")
        raise

def save_results(results, file_path):
    """Save analysis results to a JSON file."""
    try:
        with open(file_path, 'w') as f:
            json.dump(results.to_dict(), f, indent=4)
        logger.info(f"Analysis results saved to {file_path}")
    except IOError:
        logger.error(f"Cannot write to file: {file_path}")
        raise

def main(input_path, output_path):
    data = load_simulation_output(input_path)
    results = analyze_data(data)
    save_results(results, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze simulation results.")
    parser.add_argument('--input', type=str, required=True, help="Path to the simulation output CSV file.")
    parser.add_argument('--output', type=str, required=True, help="Path to save the analysis results JSON file.")
    
    args = parser.parse_args()
    
    try:
        main(args.input, args.output)
        logger.info("Data analysis completed successfully.")
    except Exception as e:
        logger.error(f"Data analysis failed: {e}")

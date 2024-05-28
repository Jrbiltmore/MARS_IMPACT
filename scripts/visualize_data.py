# 3D_Modeling_Project/scripts/visualize_data.py

import matplotlib.pyplot as plt
import pandas as pd
import json
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levellevelname)s - %(message)s'))
logger = logging.getLogger()
file_handler = logging.FileHandler('visualize_data.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def load_simulation_data(file_path):
    """Load simulation data from a JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        logger.info(f"Simulation data loaded from {file_path}")
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Error reading JSON file: {file_path}")
        raise

def plot_height_map(height_map):
    """Plot the height map using a heatmap."""
    try:
        plt.imshow(height_map, cmap='viridis')
        plt.colorbar(label='Height')
        plt.title('Height Map')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.show()
        logger.info("Height map plotted successfully.")
    except Exception as e:
        logger.error(f"Error plotting height map: {e}")
        raise

def save_plot(height_map, output_path):
    """Save the height map plot to a file."""
    try:
        plt.imshow(height_map, cmap='viridis')
        plt.colorbar(label='Height')
        plt.title('Height Map')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.savefig(output_path)
        logger.info(f"Plot saved to {output_path}")
    except IOError:
        logger.error(f"Error saving plot to {output_path}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize simulation data.")
    parser.add_argument('--input', type=str, required=True, help="Path to the simulation data JSON file.")
    parser.add_argument('--output', type=str, required=False, help="Path to save the plot image file.")

    args = parser.parse_args()

    try:
        data = load_simulation_data(args.input)
        plot_height_map(data['height_map'])
        if args.output:
            save_plot(data['height_map'], args.output)
    except Exception as e:
        logger.error(f"Failed to visualize data: {e}")

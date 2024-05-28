# 3D_Modeling_Project/scripts/run_simulation.py

import numpy as np
import json
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
file_handler = logging.FileHandler('run_simulation.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def simulate_comet_impact(duration, time_step):
    """Run a simulation of a comet impact."""
    try:
        t = np.arange(0, duration, time_step)
        height_map = np.sin(t)  # Simplified example of height variation
        impact_location = (np.random.uniform(0, 100), np.random.uniform(0, 100))
        logger.info(f"Simulation run successfully for duration {duration} with time step {time_step}")
        return {
            'height_map': height_map.tolist(),
            'impact_location': impact_location
        }
    except Exception as e:
        logger.error(f"Error during simulation: {e}")
        raise

def save_simulation_results(results, output_path):
    """Save simulation results to a JSON file."""
    try:
        with open(output_path, 'w') as f:
            json.dump(results, f)
        logger.info(f"Simulation results saved to {output_path}")
    except IOError:
        logger.error(f"Error saving simulation results to {output_path}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run comet impact simulation.")
    parser.add_argument('--duration', type=float, required=True, help="Duration of the simulation.")
    parser.add_argument('--time_step', type=float, required=True, help="Time step for the simulation.")
    parser.add_argument('--output', type=str, required=True, help="Path to save the simulation results.")

    args = parser.parse_args()

    try:
        results = simulate_comet_impact(args.duration, args.time_step)
        save_simulation_results(results, args.output)
    except Exception as e:
        logger.error(f"Failed to run simulation: {e}")

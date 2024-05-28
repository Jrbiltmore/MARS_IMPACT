# 3D Modeling Project: Comet Impact Simulation

## Overview

This project aims to simulate the impact of a comet on Mars using advanced 3D modeling and simulation techniques. The project includes data preprocessing, 3D model generation, impact simulation, and result analysis.

## Prerequisites

- Blender
- Python 3.7+
- Required Python packages listed in `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd 3D_Modeling_Project
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure Blender is installed and the Blender Python API is accessible.

## Running the Scripts

1. **Preprocess Data**:
    ```sh
    python scripts/preprocess_data.py --topo_map data/mars_topography_map.png --impact_data data/impact_data.csv --image data/impact_image.png --config configs/config.json --output data/processed_data.json --contour_output data/contour_visualization.png
    ```

2. **Generate 3D Model**:
    ```sh
    blender --background --python scripts/generate_3d_model.py -- --input data/processed_data.json --output models/impact_simulation.blend
    ```

3. **Simulate Impact**:
    ```sh
    blender --background --python scripts/simulate_impact.py -- --config configs/simulation_config.json
    ```

4. **Analyze Results**:
    ```sh
    python scripts/analyze_results.py --input results/simulation_output.csv --output results/analysis_results.json
    ```

## Authors

- Jacob Thomas Messer Redmond
- ChatGPT-4o

## License

This project is licensed under the MIT License. See the LICENSE file for details.

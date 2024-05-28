# 3D Modeling Project: Comet Impact Simulation

## Project Overview

This project aims to simulate the impact of a comet on Mars, using advanced 3D modeling and simulation techniques. The project involves the following steps:

1. **Preprocessing Data**: Load and process topographical and impact data.
2. **Generating 3D Models**: Create 3D models of the terrain and impact site.
3. **Simulating the Impact**: Run simulations to model the impact event.
4. **Analyzing Results**: Analyze the simulation output to derive meaningful insights.

## Context and Supporting Simulation

### Martian Dichotomy

The stark contrast between Mars' northern and southern hemispheres is one of the most notable features of the planet. The northern hemisphere is characterized by smooth, low-lying plains, while the southern hemisphere is higher and heavily cratered. Research suggests that a giant impact, possibly from a comet or asteroid, could have caused this dichotomy. An impact of this magnitude would strip away a significant portion of the crust, particularly in the northern hemisphere, leading to the current topographical differences​ (Science News, Eos).

### Impact Craters and Geological Evidence

New studies have identified massive impact craters in the southern hemisphere of Mars. These craters, such as the Borealis Basin, are consistent with impacts that would generate enough force to create widespread geological changes. This hypothesis is supported by the discovery of specific features like elliptical boundaries and massive depressions that can only be formed by significant impact events​ (PhysOrg).

### Martian Meteorites

Analysis of Martian meteorites found on Earth has revealed crystalline structures indicative of high-energy impacts. These structures, known as deformation twins, form under intense pressure and are commonly associated with large impacts. The presence of these features in Martian rocks suggests that Mars experienced significant impacts that could have contributed to its current geological state​ (Eos).

### Simulations and Models

Advanced 3D simulations have modeled the effects of a large impact on Mars. These models show that a comet or asteroid impact could create a hemispherical magma ocean, which upon cooling, results in a thicker crust in the southern hemisphere and a thinner crust in the north. Such impacts also align with the distribution of volcanic features and the timing of volcanic activity observed on Mars​ (Science News).

### Supporting Research

The study titled "Three-dimensional simulations of the southern polar giant impact hypothesis for the origin of the Martian dichotomy" by Giovanni Leone, Paul J. Tackley, Taras V. Gerya, Dave A. May, and Guizhi Zhu, published in *Geophysical Research Letters*, demonstrates that the impact of a ~lunar-sized body with Mars is capable of creating a hemispherical magma ocean. This ocean, upon cooling and solidification, resulted in the formation of the southern highlands and thus the Martian dichotomy. The study's numerical simulations suggest that the giant impact may have contributed a significant amount of iron to the Martian core and generated a deep thermal anomaly that led to the onset and development of volcanism in the southern highlands. Their model also predicts mantle plumes converging to the South Pole and the absence of significant large-scale volcanism in the northern lowlands, consistent with geological observations.

For more details, refer to the research article: [Three-dimensional simulations of the southern polar giant impact hypothesis for the origin of the Martian dichotomy](https://doi.org/10.1002/2014GL062261).

## Folder Structure

- **data/**: Contains raw data files including topography maps and impact data.
- **models/**: Stores the generated 3D models and simulation results.
- **scripts/**: Includes all the scripts for data preprocessing, 3D model generation, simulation, and analysis.
- **results/**: Contains the results of the simulations and analysis reports.
- **docs/**: Documentation files including project descriptions, methodologies, and references.
- **configs/**: Configuration files for the simulations and models.

## Getting Started

### Prerequisites

- Blender
- Python 3.7+
- Required Python packages: `pandas`, `numpy`, `Pillow`, `jsonschema`, `argparse`

### Installation

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

### Running the Scripts

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

## Project Details

### Data Preprocessing

The `preprocess_data.py` script loads and processes the topography map, impact data, and image data to identify features potentially related to the impact event. It validates the data against a predefined schema and saves the processed data to a JSON file.

### 3D Model Generation

The `generate_3d_model.py` script generates a 3D model of the terrain and impact site using Blender. It loads the processed data and creates the 3D elements accordingly.

### Impact Simulation

The `simulate_impact.py` script runs the impact simulation in Blender. It uses the configuration file to set up the simulation parameters and outputs the results as image files.

### Results Analysis

The `analyze_results.py` script analyzes the simulation output data. It calculates summary statistics and saves the analysis results to a JSON file.

## Authors

- Jacob Thomas Messer Redmond
- ChatGPT-4o

## License

This project is licensed under the MIT License. See the LICENSE file for details.

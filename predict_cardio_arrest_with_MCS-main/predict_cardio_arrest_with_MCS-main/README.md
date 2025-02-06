# Predicting Cardiac Arrest Impact on Traffic Accidents - Monte Carlo Simulation

## Project Structure

├── config/

├── data/

├── docs/

├── scripts/

├── src/

├── tests/

├── README.md

├── requirements.txt

└── setup.py

### **Root Directory**
- `requirements.txt` : all dependencies of the project
- `setup.py` : Packages needed for installation configuration

---

### **1. config/**
Contains all configuration files for the simulation:
- `cluster.yml` : Cluster computing settings for distributed simulations
- `parameters.yml` : Parameter distributions for Monte Carlo sampling
  - Defines statistical distributions for age, health status, SCA probability, etc.
- `simulation.yml` : Core simulation parameters
  - Number of samples, runtime limits, output formats

---

### **2. data/**
Handles all input/output data:
- `input_parameters/` : Baseline datasets
  - CSV/JSON files with driver demographics, historical SCA rates
- `simulation_results/` : Raw output from simulation runs
  - Contains batch directories with timestamped results
- `visualization_data/` : Processed data for graphical representation
  - Pickle files with aggregated results, PNG plots

---

### **3. docs/**
Project documentation:
- `architecture.md` : System design and component relationships
- `api_documentation.md` : Code API reference

---

### **4. scripts/**
Execution scripts:
- `run_simulation.py` : Main entry point for simulations
  - Handles command-line arguments and pipeline orchestration

---

### **5. src/**
Core source code;

#### **analysis/**
- `risk_aggregation.py` : Statistical analysis of results
  - Calculates incident rates, confidence intervals
- `visualization.py` : Plot generation tools
  - Creates histograms, heatmaps, time-series plots

#### **sampling/**
- `distributions.py` : Probability distribution implementations
  - Normal, LogNormal, Categorical distributions
- `parameter_sampler.py` : Sampling strategy controller
  - Handles nominal/importance sampling modes

#### **simulation/**
- `mcs_core.py` : Main Monte Carlo engine
  - Implements cardiac event modeling and accident prediction
  - Contains safety envelope calculations

#### **utils/**
- `file_io.py` : Data serialization/deserialization
  - Handles JSON, Pickle, CSV formats
- `validation.py` : Input sanity checks
  - Parameter range validation, type checking
- `config_loader.py` : Configuration management
  - YAML parsing and validation
- `cli.py` : Command-line interface setup
  - Argument parsing and help system

---

### **6. tests/**
Quality assurance:

#### **unit/**
- `test_sampling.py` : Sampling strategy tests
- `test_simulation.py` : Core logic validation

#### **integration/**
- `test_full_pipeline.py` : End-to-end workflow tests
- `test_risk_calculation.py` : Risk aggregation verification

---

## Getting Started

### Installation
```bash
pip install -r requirements.txt

```
### Create Virtual Environment
- `Note`: Python 2.7  doesn't support venv.
The venv module only exists in Python 3.3+.

```bash
python -m venv venv
.\venv\Scripts\activate
```
### If You Still Need Python 2.7
Use virtualenv as a workaround for Python 2.7:
- `Install virtualenv`
```bash
pip install virtualenv
```
- `Create environment`
```bash
virtualenv venv
```
- `Activate`
```bash
.\venv\Scripts\activate
```
### Running Simulation
```bash
python scripts/run_simulation.py \
    --num_samples=100000 \
    --config=config/parameters.yml \
    --output_dir=data/simulation_results
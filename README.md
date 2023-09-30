# EnergyConsumptionSimulation
A system to optimize energy flow in households, comprising energy producers, consumers, storage, and grid access, aiming to reduce carbon emissions and cut costs through clean energy usage.

# Installation and Usage Guide

## Prerequisites
To install energySystemApp on your machine, you'll need the following prerequisites:

- Conda (miniconda or anaconda)
- Python
- Visual Studio Code (optional)

## Installation Steps

### Clone the Repository
Clone the energySystemApp repository using Git:

```bash
git clone https://github.com/Kingatsar/EnergyConsumptionSimulation.git
```

### Set up the Environment
Open a terminal and navigate to the "hymateTask" directory.

Create a Conda environment named "pygmt" using the following commands:

```bash
conda create --name pygmt --channel conda-forge pygmt
conda activate pygmt
pip install pandas 
pip install django
```

### Start the Application
Make sure you are in the "hymateTask" directory.

Launch the application locally by running the following command:

```bash
python manage.py runserver 8080

```

Access the application in your web browser at http://localhost:8080.

### Configure and Run Simulations
Once the application is running, you can specify the number of clean energy producers and batteries with their maximum storage capacity.

Start the simulation to optimize energy flow.

### Access Generated Data
Find the generated data in the "data" directory within the repository.


# End-to-end-Machine-Learning-Project-with-MLflow

# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/navisk13/e2e-ml-mlflow.git
```
### STEP 01 - Activate the virtual environment (includes all requirements)

```bash
source virtualenv/bin/activate
```

### Or Install the requirements
```bash
pip install -r requirements.txt
```

### STEP 02 - Set up MLFlow and DagsHub

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/navisk13/e2e-ml-mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=navisk13

export MLFLOW_TRACKING_PASSWORD=9b8173a312566ade802f4964109101fdddd21ee9

```

MLFLOW_TRACKING_URI=https://dagshub.com/navisk13/e2e-ml-mlflow.mlflow
MLFLOW_TRACKING_USERNAME=navisk13
MLFLOW_TRACKING_PASSWORD=9b8173a312566ade802f4964109101fdddd21ee9


### STEP 03 - Run the application

```bash
streamlit run WineApp.py
```

### More Resources

[MLFlow Documentation](https://mlflow.org/docs/latest/index.html)

[DagsHub](https://dagshub.com/)









# End-to-end-Machine-Learning-Project-with-MLflow

# How to run?
### STEPS:

Clone the repository

```bash
git clone https://github.com/navisk13/e2e-ml-mlflow.git
```
### STEP 01 - Activate the virtual environment

```bash
source virtualenv/bin/activate
```


### STEP 02 - Install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03 - Run the application

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/navisk13/e2e-ml-mlflow.mlflow \
MLFLOW_TRACKING_USERNAME=navisk13 \
MLFLOW_TRACKING_PASSWORD=9b8173a312566ade802f4964109101fdddd21ee9 \
python script.py



Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/navisk13/e2e-ml-mlflow.mlflow

export MLFLOW_TRACKING_USERNAME=navisk13

export MLFLOW_TRACKING_PASSWORD=9b8173a312566ade802f4964109101fdddd21ee9

```



import cmd
import pickle
import os
import subprocess
import pandas as pd
import json
import gzip

#### SET VARS IN GLOBAL ####
main_code_data = """# Local imports
import datetime

# Third party imports
from pydantic import BaseModel, Field

from ms import app
from ms.functions import get_model_response


model_name = "Breast Cancer Wisconsin (Diagnostic)"
version = "v1.0.0"


# Input for data validation
class Input(BaseModel):
    concavity_mean: float = Field(..., gt=0)
    concave_points_mean: float = Field(..., gt=0)
    perimeter_se: float = Field(..., gt=0)
    area_se: float = Field(..., gt=0)
    texture_worst: float = Field(..., gt=0)
    area_worst: float = Field(..., gt=0)

    class Config:
        schema_extra = {
            "concavity_mean": 0.3001,
            "concave_points_mean": 0.1471,
            "perimeter_se": 8.589,
            "area_se": 153.4,
            "texture_worst": 17.33,
            "area_worst": 2019.0,
        }


# Ouput for data validation
class Output(BaseModel):
    label: str
    prediction: int


@app.get('/')
async def model_info():
    return {
        "name": model_name,
        "version": version
    }


@app.get('/health')
async def service_health():
    return {
        "ok"
    }


@app.post('/predict', response_model=Output)
async def model_predict(input: Input):
    response = get_model_response(input)
    return response

"""
function_code_data = """# Import packages
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib
import gzip


# Load the dataset
data = pd.read_csv('data/breast_cancer.csv')

# Preselected feature
selected_features = [
    'concavity_mean',
    'concave_points_mean',
    'perimeter_se',
    'area_se',
    'texture_worst',
    'area_worst'
]

# Preprocess dataset
data = data.set_index('id')
data['diagnosis'] = data['diagnosis'].replace(['B', 'M'], [0, 1])  # Encode y, B -> 0 , M -> 1

# Split into train and test set, 80%-20%
y = data.pop('diagnosis')
X = data
X = X[selected_features.copy()]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an ensemble of 3 models
estimators = []
estimators.append(('logistic', LogisticRegression()))
estimators.append(('cart', DecisionTreeClassifier()))
estimators.append(('svm', SVC()))

# Create the Ensemble Model
ensemble = VotingClassifier(estimators)

# Make preprocess Pipeline
pipe = Pipeline([
    ('imputer', SimpleImputer()),  # Missing value Imputer
    ('scaler', MinMaxScaler(feature_range=(0, 1))),  # Min Max Scaler
    ('model', ensemble)  # Ensemble Model
])

# Train the model
pipe.fit(X_train, y_train)

# Test Accuracy
print("Accuracy: %s%%" % str(round(pipe.score(X_test, y_test), 3) * 100))

# Export model
joblib.dump(pipe, gzip.open('model/model_binary.dat.gz', "wb"))


"""
requirements_data = """anyio==3.5.0
asgiref==3.5.0
click==8.1.2
cycler==0.11.0
fastapi==0.75.2
fonttools==4.32.0
h11==0.13.0
idna==3.3
joblib==1.1.0
kiwisolver==1.4.2
matplotlib==3.5.1
numpy==1.22.3
packaging==21.3
pandas==1.4.2
Pillow==9.1.0
pydantic==1.9.0
pyparsing==3.0.8
python-dateutil==2.8.2
pytz==2022.1
scikit-learn==1.0.2
scipy==1.8.0
six==1.16.0
sklearn==0.0
sniffio==1.2.0
starlette==0.17.1
threadpoolctl==3.1.0
typing_extensions==4.2.0
uvicorn==0.17.6
"""
documentation_data = """# POST method predict
curl -d '{"concavity_mean": 0.3001, "concave_points_mean": 0.1471, "perimeter_se": 8.589, "area_se": 153.4, "texture_worst": 17.33, "area_worst": 2019.0}' \
     -H "Content-Type: application/json" \
     -XPOST http://0.0.0.0:8000/predict

# GET method info
curl -XGET http://localhost:8000/info

# GET method health
curl -XGET http://localhost:8000/health
"""
#### SET VARS IN GLOBAL ####


# FUNCTION VARS
model_localpath = "C:/virtualenv_Bowen/model/model.dat.gz"
validation_data_localpath = "C:/virtualenv_Steve/data/data.gzip"
validation_control_localpath = "C:/virtualenv_Steve/data/data_control.gzip"

base_path = "c:/"           #### SET VARS IN GLOBAL ####
model_name = "test"        #### SET VARS IN GLOBAL ####

# OPTIONAL FUNCTION VARS
requirements_localpath = ""
documentation_localpath = ""
function_code_localpath = ""
online_enviro_code_localpath = ""

# INTERNAL VARS
validation_content = pd.DataFrame()
validation_control_content = pd.DataFrame()
model_data = ""
function_content = ""
requirements_content = ""
documentation_content = ""
main_content = ""

print("Starting folder generation...")

#### validation set copy ####
print("Locating and copying validation data set")
### Check file type extension ###
validation_filename, validation_file_extension = os.path.splitext(
    validation_data_localpath)
print("File extension is: " + str(validation_file_extension))
if validation_file_extension == ".csv":
    validation_content = pd.read_csv(validation_data_localpath)
elif validation_file_extension == ".pkl":
    validation_content = pd.read_pickle(validation_data_localpath)
elif validation_file_extension == ".gzip":
    validation_content = pd.read_parquet(validation_data_localpath)
print("Validation data collected")

#### Machine leanring model copy ####
model_filename, model_file_extension = os.path.splitext(
    model_localpath)
print("File extension is: " + str(model_file_extension))
if model_file_extension == ".gz":
    model_file = gzip.open(model_localpath, "rb")
    model_file_content = model_file.read()
elif model_file_extension == ".pkl":
    model_file = open(model_localpath, 'rb')

#### validation control copy ####
print("Locating and copying validation control data set")
### Check file type extension ###
validation_control_filename, validation_control_file_extension = os.path.splitext(
    validation_control_localpath)
print("File extension is: " + str(validation_control_file_extension))
if validation_control_file_extension == ".csv":
    validation_control_content = pd.read_csv(validation_control_localpath)
elif validation_control_file_extension == ".pkl":
    validation_contro_content = pd.read_pickle(validation_control_localpath)
elif validation_control_file_extension == ".gzip":
    validation_contro_content = pd.read_parquet(validation_control_localpath)
print("Validation data collected")

#### Function code copy ####
print("Creating function code")
if function_code_localpath == "":
    # Need to replace with globals when in package #
    function_content = function_code_data
else:
    function_content = open(function_code_localpath, "r")

#### Main code copy ####
print("Creating Main py code")
if function_code_localpath == "":
    main_content = main_code_data  # Need to replace with globals when in package #
else:
    main_content = open(online_enviro_code_localpath, "r")

#### Requirements copy ####
print("Creating Requirements file")
if function_code_localpath == "":
    requirements_content = requirements_data  # Need to replace with globals when in package #
else:
    requirements_content = open(requirements_localpath, "r")

#### Documentation copy ####
print("Creating documentation file")
if documentation_localpath == "":
    documentation_content = documentation_data  # Need to replace with globals when in package #
else:
    documentation_content = open(documentation_localpath, "r")

# Folder structure
print("Generating folder structure with data points")
folders = [{"path": base_path + "virtualenv_" + model_name + "/code/validate.py",
            "content": function_content},
           {"path": base_path + "virtualenv_" + model_name + "/data/data.gzip",
            "content": "clear"},
           {"path": base_path + "virtualenv_" + model_name + "/data/data_control.gzip",
            "content": "clear"},
           {"path": base_path + "virtualenv_" + model_name + "/model/model.pkl",
            "content": "clear"},
           {"path": base_path + "virtualenv_" + model_name + "/requirements.txt",
            "content": requirements_content},
           {"path": base_path + "virtualenv_" + model_name + "/docs/documentation.txt",
            "content": documentation_content},
           {"path": base_path + "virtualenv_" + model_name + "/main.py",
            "content": main_content}
           ]

#### Write files and directory's ####
for item in folders:
    os.makedirs(os.path.dirname(item["path"]), exist_ok=True)
    with open(item["path"], "w") as f:
        if item["content"] != "clear":
            f.write(item["content"])

#### Write PD to files ####
print("Writing data")
validation_content.to_parquet(
    base_path + "virtualenv_" + model_name + "/data/data.gzip")
validation_control_content.to_parquet(
    base_path + "virtualenv_" + model_name + "/data/data_control.gzip")

### Copy machine learning model ###
print("Writing Machine learning model")
copy_model_file = open(base_path + "virtualenv_" + model_name + "/model/model.pkl", "wb") 
pickle.dump(model_file_content, copy_model_file)

copy_model_file.close()
model_file.close()

#### Create files needed for the virtual machine ####
print("Generating VENV Data")
cmd = 'python -m venv ' + base_path + 'virtualenv_' + model_name
p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
print(p.stdout.decode())

#### Finish ####
print("Virtual machine folder structure created on: " +
      base_path + "/virtualenv_" + model_name)

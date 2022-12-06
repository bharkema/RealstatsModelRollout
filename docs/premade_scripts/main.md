[<- Go back to main page](../index.md)

# Main.py 
These scripts can be used to edit the functionality of the package
```python
# Local imports
import datetime

# Third party imports
from pydantic import BaseModel, Field

from ms import app
from ms.functions import get_model_response
from ms.train_model import train_model
from ms import Load_model

model_name = "Testing model"
version = "v1.0.0"
localpath = ""

# Input for data validation
class Inputs(BaseModel):
    temp: str
    # TODO

# Ouput for data validation
class Output(BaseModel):
    label: str
    prediction: int

class Validation_input(BaseModel):
    feature_array: list[str]
    param_values: object
    target: str
    localpath: str

class Validation_output(BaseModel):
    mae_value: float
    r2_value: float
    mape_value: float
    features: list[str]

class loaded_output(BaseModel):
    loaded: bool

@app.get('/')
async def help():
    return {
        "name": model_name,
        "version": version,
        "property": "Realstats"
    }

@app.get('/info')
async def model_info():
    return {
        "name": model_name,
        "version": version,
        "creator": "Realstats",
        "information": "Go look at the documentation for what calls to make"
    }

@app.post('/predict', response_model=Output)
async def model_predict(inputs: Inputs):
    response = get_model_response(inputs)
    print(response)
    return response

@app.put('/validate', response_model=Validation_output)
async def model_validate(input: Validation_input):
    response = train_model.Execute_training_testing(feature_array=input.feature_array,
    param_values=input.param_values, target=input.target, localpath=input.localpath)
    localpath = input.localpath

    Load_model(localpath)
    return response

@app.put('/loadmodel', response_model=loaded_output)
async def model_load():
    try:
        Load_model(localpath)
        return {
            "loaded": True
        }
    except:
        return {
            "loaded": False
        }
```
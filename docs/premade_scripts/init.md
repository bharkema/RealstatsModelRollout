[<- Go back to main page](../index.md)

# ms/__ init __.py 
These scripts can be used to edit the functionality of the package
```python
# Imports
from fastapi import FastAPI
import joblib

model = ""

# Initialize FastAPI app
app = FastAPI()

def Load_model():
    # Load model
    model = joblib.load('model/trained_model.pkl')

```
[<- Go back to main page](../index.md)

# ms/functions.py 
These scripts can be used to edit the functionality of the package
```python
import pandas as pd
import numpy as np
from ms import model
from sklearn.metrics import mean_absolute_error

def predict(X, model):
    prediction = model.predict(X)[0]
    return prediction

def get_model_response(input):
    X = pd.json_normalize(input.__dict__)
    prediction = predict(X, model)
    if prediction == 1:
        label = "M"
    else:
        label = "B"
    return {
        'label': label,
        'prediction': int(prediction)
    }
    
def percentage_error(actual, predicted):
    res = np.empty(actual.shape)
    for j in range(actual.shape[0]):
        if actual[j] != 0:
            res[j] = (actual[j] - predicted[j]) / actual[j]
        else:
            res[j] = predicted[j] / np.mean(actual)
    return res

def mean_absolute_percentage_error(y_true, y_pred):
    return (1 - np.mean(np.abs(percentage_error(np.asarray(y_true), np.asarray(y_pred))))) * 100

```
[<- Go back to Model()](../model.md)

## Load_model()
Validate_request(self, payload):

returns: <br>
requests.response object

This function Trains the model using the code in ms/functions.py which will the test the model and receive the following results:
* MAE
* MAPE
* R2

after which the model will load the model for use

```python 
import RealstatsModelRollout as RMR

model = RMR.Model()

model.Model_URL = "http://127.0.0.1"

model.Validate_request(payload=payload)
```
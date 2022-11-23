[<- Go back to Model()](../model.md)

## Load_model()
Load_model(self):

returns: <br>
requests.response object

This function sends a message to the running virtual machine to load the model and make it active. 

```python 
import RealstatsModelRollout as RMR

model = RMR.Model()

model.Model_URL = "http://127.0.0.1"
model.Load_model()
```
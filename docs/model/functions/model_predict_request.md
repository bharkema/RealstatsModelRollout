[<- Go back to Model()](../model.md)

## Predict_request()
Predict_request(self, json_data=''):

Predict request sends a POST request to the url given by either the package or set by the user.

```python
import RealstatsModelRollout as RMR

RMR.Model().Predict_request(json_data={})

```

The method uses requests to request the data from a URL. this function uses a POST request to handle getting the information
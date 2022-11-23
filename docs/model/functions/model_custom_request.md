[<- Go back to main page](https://bharkema.github.io/RealstatsModelRollout/)

## Custom_request()
Custom_request(self, request_type="", pathing="", json_data='Optional'):

Predict request sends a POST, GET or PUT request to the url given by either the package or set by the user.

```python
import RealstatsModelRollout as RMR

RMR.Model().Custom_request(request_type="get", pathing="info/model/data"):

```

The method uses requests to request the data from a URL. this function uses a POST, GET or PUT request to handle getting the information
[<- Go back to main page](../index)

## Model()

### How to use the class
The model class is used to communicate with the model that is either local or online. By default the settings of the model are set to test locally. you can update propertys to function with any URL or port

the following functions are available in Model():
* [Info_request()](./functions/model_info_request.md)
* [Predict_request()](./functions/model_predict_request.md)
* [Custom_request()](./functions/model_custom_request.md)
* [Validate_request()](./functions/model_validate_request.md) 
* [Load_model()](./functions/model_load_request.md)

### Code examples
``` python
import RealstatsModelRollout as RMR

model = RMR.Model()

# Get information from virtual enviroment
model.Info_request()

# let the virtual enviroment load a machine learning model
model.Load_model()

# Get a prediction from the machine learning model
json_data = {}
model.Predict_request(json_data=json_data)

# Send a custom request to the virtual enviroment
model.Model_URL = "URL"
model.Model_port = "8000"
model.Custom_request(request_type="post", pathing="user/auth", json_data='Development')

# Validate and train machine learning model
import RealstatsModelRollout as RMR

features = ["string"]
best_param_values = {
    "param_value": 1
}

payload = {
    "feature_array": features,
    "param_values": best_param_values,
    "target": "listing_price"
}

model = RMR.Model()
model.Model_URL = "http://127.0.0.1"

model.Validate_request(payload=payload)

```


### Properties within class
``` python

    @property
    def Model_port(self):
        """
        :type: string
        """
        return self._model_port

    @Model_port.setter
    def Model_port(self, value):
        """
        :type: string
        """
        if isinstance(value, string_types):
            self._model_port = value
        else:
            raise Exception("Value must be string")

    ### URL to model ###
    @property
    def Model_URL(self):
        """
        :type: string
        """
        return self._modelURL

    @Model_URL.setter
    def Model_URL(self, value):
        """
        :type: string
        """
        if isinstance(value, string_types):
            self._modelURL = value
        else:
            raise Exception("Value must be string")

```
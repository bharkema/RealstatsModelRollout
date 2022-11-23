[<- Go back to main page](https://bharkema.github.io/RealstatsModelRollout/)

## Start_validation()
Start_validation(self, localpath="Optional", model_url="Optional", model_port="Optional"):

This function will start the training of the model by sending the features, parameters and target to the running model and will then wait for the response of the model. When the testing values set by the user are within range of the expected value + the deviation percentage the model will be classified as valid and wil automatically be pushed to the online repo.

```python
import RealstatsModelRollout as RMR

# When used from generating the structure
v = RMR.Validate()

v.MAE_expected_value = 200
v.MAE_Deviation_percentage = 5

v.MAPE_expected_value = 80
v.MAPE_Deviation_percentage = 2

v.R2_expected_value = 90
v.R2_Deviation_percentage = 2

v.Feature_array = features
v.Model_parameters = best_param_values
v.Model_target = "target"

v.Start_validation()

# Editable settings
v.Start_validation(localpath="Optional", model_url="Optional", model_port="Optional")

```
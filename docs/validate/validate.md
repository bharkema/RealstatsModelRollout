[<- Go back to main page](../index.md)

## Validate()

### How to use the class
Validate can be used to create the validation files needed for saving the model to a repo 

the following functions are available in Versioning():
* [Start_validation()](./functions/start_validation.md)
* [Save_validation_results()](./functions/save_validation.md) <br>
This function is more for internal use and not for use by users but can be referenced if needed

More in depth information can be found in the links above

### Code examples
``` python 
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


### Properties within class
``` python
 
    # MAE values
    @property
    def MAE_Deviation_percentage(self):
        """
        :type: float
        """
        return self._mae_deviation_percentage

    @MAE_Deviation_percentage.setter
    def MAE_Deviation_percentage(self, value):
        """
        :type: float
        """
        self._mae_deviation_percentage = value

    @property
    def MAE_expected_value(self):
        """
        :type: float
        """
        return self._mae_expected_value

    @MAE_expected_value.setter
    def MAE_expected_value(self, value):
        """
        :type: float
        """
        self._mae_expected_value = value

    # R2 values
    @property
    def R2_Deviation_percentage(self):
        """
        :type: float
        """
        return self._r2_deviation_percentage

    @R2_Deviation_percentage.setter
    def R2_Deviation_percentage(self, value):
        """
        :type: float
        """
        self._r2_deviation_percentage = value

    @property
    def R2_expected_value(self):
        """
        :type: float
        """
        return self._r2_expected_value

    @R2_expected_value.setter
    def R2_expected_value(self, value):
        """
        :type: float
        """
        self._r2_expected_value = value

    # MAPE values
    @property
    def MAPE_Deviation_percentage(self):
        """
        :type: float
        """
        return self._mape_deviation_percentage

    @MAPE_Deviation_percentage.setter
    def MAPE_Deviation_percentage(self, value):
        """
        :type: float
        """
        self._mape_deviation_percentage = value

    @property
    def MAPE_expected_value(self):
        """
        :type: float
        """
        return self._mape_expected_value

    @MAPE_expected_value.setter
    def MAPE_expected_value(self, value):
        """
        :type: float
        """
        self._mape_expected_value = value

    # Features
    @property
    def Feature_array(self):
        """
        :type: float
        """
        return self._model_features

    @Feature_array.setter
    def Feature_array(self, value):
        """
        :type: float
        """
        self._model_features = value

    # target
    @property
    def Model_target(self):
        """
        :type: float
        """
        return self._target

    @Model_target.setter
    def Model_target(self, value):
        """
        :type: float
        """
        self._target = value

    # Param
    @property
    def Model_parameters(self):
        """
        :type: float
        """
        return self._param_settings

    @Model_parameters.setter
    def Model_parameters(self, value):
        """
        :type: float
        """
        self._param_settings = value
```
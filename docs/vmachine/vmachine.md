[<- Go back to main page](../index.md)

## Vmachine()

### How to use the class
Vmachine can be used for generating virtual enviroments and generating the folder structure needed to be able to use the model created by the data scientist.

the following functions are available in Vmachine():
* [Generate_structure()](./functions/generate_structure_rework.md)
* [Start_venv()](./functions/start_venv.md)

More in depth information can be found in the links above

### Code examples
``` python
import RealstatsModelRollout as RMR

# Generation of virtual enviroment folder base usage
RMR.Vmachine().Generate_structure(model_save_location="WHERE YOU WANT TO SAVE", model_name="MODEL NAME", model_current_location="PATH OF WHERE PROJECT IS")

# by calling Start_venv the enviroment will start
venv_machine.Start_venv()

```


### Properties within class
``` python
    # Identification of the platform the package is running on
    @property
    def Dev_platform(self):
        """
        :type: string
        """

    # Identification of the platform version the package is running on
    @property
    def Dev_platform_vers(self):
        """
        :type: string
        """

    # Identification of the platform release version the package is running on
    @property
    def Dev_platform_release(self):
        """
        :type: string
        """
```
[<- Go back to main page](https://bharkema.github.io/RealstatsModelRollout/)

## Vmachine()

### How to use the class
Vmachine can be used for generating virtual enviroments and generating the folder structure needed to be able to use the model created by the data scientist. 

the following functions are available in Vmachine():
* [Generate_structure()](https://bharkema.github.io/RealstatsModelRollout/functions/generate_structure)
* [Start_venv()](https://bharkema.github.io/RealstatsModelRollout/functions/start_venv)

More in depth information can be found in the links above

### Code examples
``` python 
import RealstatsModelRollout as RMR

# Generation of virtual enviroment folder base usage
RMR.vmachine().Generate_structure(model_localpath="%PATH TO MODEL TO COPY%", 
                                    validation_data_localpath="%PATH TO data TO COPY%", 
                                    validation_control_localpath="%PATH TO CONTROL DATA TO COPY%", 
                                    base_path="%PATH TO WHERE YOU WANT TO SAVE FOLDER%", 
                                    model_name = "Demo")

# Start of virtual enviroment base usage
RMR.vmachine().Start_venv(self, localpath="%PATH TO ENVROMENT FOLDER%", 
                            execution_code="%NAME OF CODE FILE YOU WISH TO EXECUTE%"):

```


### Properties within class
``` python
    def Dev_platform(self):
        """
        :type: string
        """
        return self._dev_platform

    @Dev_platform.setter
    def Dev_platform(self, value):
        """
        :type: string
        """
        self._dev_platform = value

    @property
    def Dev_platform_vers(self):
        """
        :type: string
        """
        return self._dev_platform_vers

    @Dev_platform_vers.setter
    def Dev_platform_vers(self, value):
        """
        :type: string
        """
        self._dev_platform_vers = value

    @property
    def Dev_platform_release(self):
        """
        :type: string
        """
        return self._dev_platform_release

    @Dev_platform_release.setter
    def Dev_platform_release(self, value):
        """
        :type: string
        """
        self._dev_platform_release = value
```
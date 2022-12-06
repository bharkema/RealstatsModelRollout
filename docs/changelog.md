[<- Go back to main page](index.md)

Welcome to the changelog here you will see past versions of the changelog and what the changes were within the package and functionality

Here is a overview of all the released versions: <br>
* [Stable: 0.2.2](#version-022)
* [Development: 0.2.1.dev3](#version-021dev3)
* [Stable: 0.2.1](#version-021)
* [Development: 0.0.1.dev22](#version-001dev22)

# version 0.2.2
Second official release of the modelrollout package. the package has received multiple updates regarding the functionality but also usability of the package 

### New stuff
In this version the official release of the validation functionality has been added and can now be used 
within the system. <br>

The earlier version already had the class added in the system but the functions were not stable and or ready yet in this version they are! For more information please look at the documentation here <br>
* Documentation when the model is running <br>
Because we are using FastAPI to create a model with multiple endpoints it is possible to als get documentation of the requests that you can do and what the model expects to see. you can bring forward the documentation by opening a browser and going to: <br>
```
for local
127.0.0.1:8000/docs
```

* [Validate()](./validate/validate.md)
    * [Start_validation()](./validate/functions/start_validation.md) <br>
    This function starts the validation and training of a model using the data and methods generated my Vmachine and when it is running which will then provide the following values:
        * MAE
        * MAPE
        * R2 
    
    * [Save_validation_results()](./validate/functions/save_validation.md) <br>
    This function will save the result given back by the ML model and save it to a file under the folder generatedby the package

* [Globalfunctions()](./global_functions/globalfunctions.md)
    * [Is_value_string()](./global_functions/functions/) <br>
    This function is used to check parameters written within the package but can be used if wanted outside the package. The function checks if the given value is a string

* [Model()](./model/model.md)
    * [Validate_request()](./model/functions/model_validate_request.md) <br>
    This uses the default validation and training script that will be created when no alternative is found
    * [Load_model()](./model/functions/model_load_request.md) <br>
    This uses the default loading script that will be created when no alternative is found this call can be used when a premade model is given  nad needs to be loaded.

### Updates
the following updates have been made to the following classes and functionality's
* [Generate_structure()](./vmachine/functions/generate_structure_rework.md) <br>
    The functionalitys behind this class is still the same the underlying system and needead files have been updated. for this function you only need to provide the data needed to train the ML model. the data is still a necessary file and MUST be included for the system to work. 
    furthermore all other files are still optional files that if you want to use something else or update the learning code this is still possible. do make sure to look at the documentation en premad code and make sure you use the same setup for the package to use it correctly.


* [Versioning()](./versioning/versioning.md)
    * [Upload_enviroment()](./versioning/functions/upload_enviro.md)
    * [Download_enviroment()](./versioning/functions/download_enviro.md)
    * [Get_file_content()](./versioning/functions/download_file.md)

# version 0.2.1.dev3
This is a update to version 0.2.1 in this update the main focus is a rework to the generation of the virtual enviroment the folder structure was one of the first functions written and has always been an annoyance. in this update the function has been rewritten and does all the work for you now. 

it does have some limitations which can also been seen as helpers to keep your projects clean.

### limitations: 
* Can only go 10 folders deep <br>
The reason is so we don't kill the device we are working on.
* Name limitations to files <br>
There are certain names for the files the system is looking for these can be found in the function documentation.

### plus sides:
* The function is now able to be used with only 3 parameters in the function scope
* Speed has been greatly increased from 0.3 seconds to 0.1 seconds without generating VENV data
* Better expandability
* Cleaner code

for more information on the function please look at the function documentation
* [Generate_structure()](./vmachine/functions/generate_structure_rework.md)


# version 0.2.1
The first official version with all functions currently available created.
please check the information available:
* [Vmachine()](./vmachine/vmachine.md)
    * [Generate_structure()](./vmachine/functions/generate_structure.md)
    * [Start_venv()](./vmachine/functions/start_venv.md)
* [Versioning()](./versioning/versioning.md)
    * [Upload_enviroment()](./versioning/functions/upload_enviro.md)
    * [Download_enviroment()](./versioning/functions/download_enviro.md)
    * [Get_file_content()](./versioning/functions/download_file.md)
* [Auth()](./classes/auth.md)
* [Globalfunctions()](./global_functions/globalfunctions.md)
    * [Find()](./global_functions/functions/find.md)
    * [Path_is_dir()](./global_functions/functions/pathisdir.md)
* [Model()](./model/model.md)
    * [Info_request()](./model/functions/model_info_request.md)
    * [Predict_request()](./model/functions/model_predict_request.md)
    * [Custom_request()](./model/functions/model_custom_request.md)



# version 0.0.1.dev22
The first version of the package ever released this is a dev package and is not supposed to be used by outsiders.

### Functionality added
* Virtual machine setup
    * Capable of starting a virtual enviroment by calling Vmachine().Start_venv("path to generated folder")
* Folder generation
    * System capable of copying Data sets of the types:
        * .pkl
        * .gzip
        * .csv
    * ML model gets copied to .pkl format
    * Custom base path
    * Custom model name

#### Code examples
The system automatically checks the operating system and executes commands accordingly.
```python
import RealstatsModelRollout as RMR

# Generation of virtual enviroment folder base usage
RMR.Vmachine().Generate_structure(model_localpath="%PATH TO MODEL TO COPY%", validation_data_localpath="%PATH TO data TO COPY%", validation_control_localpath="%PATH TO CONTROL DATA TO COPY%", base_path="%PATH TO WHERE YOU WANT TO SAVE FOLDER%", model_name = "Demo")
```

```python
import RealstatsModelRollout as RMR

# Start of virtual enviroment base usage
RMR.Vmachine().Start_venv(self, localpath="%PATH TO ENVROMENT FOLDER%", execution_code="%NAME OF CODE FILE YOU WISH TO EXECUTE%"):
```
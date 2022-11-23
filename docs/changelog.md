---
layout: default
---

Welcome to the changelog here you will see past versions of the changelog and what the changes were within the package and functionality

# version 0.2.1.dev3
This is a update to version 0.2.1 in this update the main focus is a rework to the generation of the virtual enviroment the folder structure was one of the first functions written and has always been an annoyance. in this update the function has been rewritten and does all the work for you now. 

it does have some limitations which can also been seen as helpers to keep your projects clean.

### limitations: 
* Can only go 10 folders deep
The reason is so we don't kill the device we are working on.
* Name limitations to files
There are certain names for the files the system is looking for these can be fount in the function documentation.

### plus sides:
* The function is now able to be used with only 3 parameters in the function scope
* Speed has been greatly increased from 0.3 seconds to 0.1 seconds without generating VENV data
* Better expandability
* Cleaner code

for more information on the function please look at the function documentation
* [Generate_structure()](https://bharkema.github.io/RealstatsModelRollout/functions/generate_structure_rework)


# version 0.2.1
The first official version with all functions currently available created.
please check the information available:
* [Vmachine()](https://bharkema.github.io/RealstatsModelRollout/classes/vmachine)
    * [Generate_structure()](https://bharkema.github.io/RealstatsModelRollout/functions/generate_structure)
    * [Start_venv()](https://bharkema.github.io/RealstatsModelRollout/functions/start_venv)
* [Versioning()](https://bharkema.github.io/RealstatsModelRollout/classes/versioning)
    * [Upload_enviroment()](https://bharkema.github.io/RealstatsModelRollout/functions/upload_enviro)
    * [Download_enviroment()](https://bharkema.github.io/RealstatsModelRollout/functions/download_enviro)
    * [Get_file_content()](https://bharkema.github.io/RealstatsModelRollout/functions/download_file)
* [Auth()](https://bharkema.github.io/RealstatsModelRollout/classes/auth)
* [Globalfunctions()](https://bharkema.github.io/RealstatsModelRollout/classes/globalfunctions)
    * [Find()](https://bharkema.github.io/RealstatsModelRollout/functions/find)
    * [Path_is_dir()](https://bharkema.github.io/RealstatsModelRollout/functions/pathisdir)
* [Model()](https://bharkema.github.io/RealstatsModelRollout/classes/model)
    * [Info_request()](https://bharkema.github.io/RealstatsModelRollout/functions/model_info_request)
    * [Predict_request()](https://bharkema.github.io/RealstatsModelRollout/functions/model_predict_request)
    * [Custom_request()](https://bharkema.github.io/RealstatsModelRollout/functions/model_custom_request)



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
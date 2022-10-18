---
layout: default
---

Welcome to the changelog here you will see past versions of the changelog and what the changes were within the package and functionality

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
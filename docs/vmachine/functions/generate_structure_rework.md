[<- Go back to Vmachine()](../vmachine.md)

## Generate_structure()
The system automatically checks the operating system and executes commands accordingly.
```python
import RealstatsModelRollout as RMR

# Generation of virtual enviroment folder base usage
RMR.Vmachine().Generate_structure(model_save_location="WHERE YOU WANT TO SAVE", model_name="MODEL NAME", model_current_location="PATH OF WHERE PROJECT IS")

```

The functions can handle the following file extensions:
* .csv
* .pkl
* .gzip (parquet)

It will however transform als data sets to a .pkl file for consistancy sake that way we can provide normalized code for execution.

furthermore the system uses the python VENV package finding more information here:
The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

See PEP 405 for more information about Python virtual environments.
[Go to Python documentation ->](https://docs.python.org/3/library/venv.html)

Furthermore this function has been reworked in version 0.2.1dev3 bettering the usability of the function
this does bring some drawbacks of which a clear folder structure is one please use the following naming of files and folder structer for the best experience:
* project root
    * data
        * train_data_model (.gzip, .csv, .pkl)
    * docs
        * documentation.txt
    * model
        * trained_model.pkl (.gz)
    * ms
        * __ init __.py
        * functions.py
        * train_model.py
    * main.py
    * requirements.txt

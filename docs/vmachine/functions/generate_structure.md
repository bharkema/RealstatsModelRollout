[<- Go back to Vmachine()](../vmachine.md)

## Generate_structure()
The system automatically checks the operating system and executes commands accordingly.
```python
import RealstatsModelRollout as RMR

# Generation of virtual enviroment folder base usage
RMR.Vmachine().Generate_structure(model_localpath="%PATH TO MODEL TO COPY%",
                                    validation_data_localpath="%PATH TO data TO COPY%",
                                    validation_control_localpath="%PATH TO CONTROL DATA TO COPY%",
                                    base_path="%PATH TO WHERE YOU WANT TO SAVE FOLDER%",
                                    model_name = "Demo")

# Customization of folder and functions
RMR.Vmachine().Generate_structure(model_localpath="%PATH TO MODEL TO COPY%",
                                    validation_data_localpath="%PATH TO data TO COPY%",
                                    validation_control_localpath="%PATH TO CONTROL DATA TO COPY%",
                                    base_path="%PATH TO WHERE YOU WANT TO SAVE FOLDER%",
                                    model_name = "Demo",
                                    requirements_localpath="%PATH TO WHERE YOUr requirements are%",
                                    documentation_localpath="%PATH TO WHERE YOUR DOCUMENTATION IS",
                                    function_code_localpath="%PATH TO WHERE YOUR FUNCTIONAL CODE IS",
                                    main_code_localpath="%PATH TO WHERE YOUR MAIN CODE FILE IS"):

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
[<- Go back to main page](https://bharkema.github.io/RealstatsModelRollout/)

## start_venv()
The system automatically checks the operating system and executes commands accordingly.
```python
import RealstatsModelRollout as RMR

# Start of virtual enviroment base usage
RMR.Vmachine().Start_venv(self, localpath="%PATH TO ENVROMENT FOLDER%",
                            execution_code="%NAME OF CODE FILE YOU WISH TO EXECUTE%"):
```

The system wil look for the folder and will start the enviroment.

furthermore the system uses the python VENV package finding more information here:
The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

See PEP 405 for more information about Python virtual environments.

[Go to Python documentation ->](https://docs.python.org/3/library/venv.html)
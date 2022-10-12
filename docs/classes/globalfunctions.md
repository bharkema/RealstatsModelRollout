[<- Go back to main page](https://bharkema.github.io/RealstatsModelRollout/)

## Globalfunctions()

### How to use the class
Globalfunctions is a class for internal use but can be accessed from the outside. this class uses standerdized functions and returns certain values

the following functions are available in Versioning():
* [Find()](https://bharkema.github.io/RealstatsModelRollout/functions/find)
* [Path_is_dir()](https://bharkema.github.io/RealstatsModelRollout/functions/pathisdir)

More in depth information can be found in the links above

### Code examples
``` python 
import RealstatsModelRollout as RMR

## Find
string = "C:/virtualenv_Actual/"
ch = "/"
RMR.globalFunctions.find(string, ch)

## Path_is_dir
path = "C:/virtualenv_Actual/"

RMR.globalFunctions.Path_is_dir(path)

```


### Properties within class
``` python

#### There are no properties ####

```
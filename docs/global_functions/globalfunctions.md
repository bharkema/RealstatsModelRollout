[<- Go back to main page](../index)

## Globalfunctions()

### How to use the class
Globalfunctions is a class for internal use but can be accessed from the outside. this class uses standerdized functions and returns certain values

the following functions are available in Versioning():
* [Find()](./functions/find.md)
* [Path_is_dir()](./functions/pathisdir.md)
* [Check_instance()](./functions/check_instance.md)

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

## Check instance
RMR.globalFunctions.Check_instance(check=value, instance_type="string")

```


### Properties within class
``` python

#### There are no properties ####

```
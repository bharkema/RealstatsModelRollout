[<- Go back to Globalfunctions()](../globalfunctions.md)

## Check_instance()

Globalfunctions.Check_instance(check, instance_type = "")

This function checks if the given value is the corresponding instance. The function can check the following:
* string
* float
* int
* list

if the check fails it wil throw an Exception

```python 

import RealstatsModelRollout as RMR

RMR.globalFunctions.Check_instance(check=value, instance_type="string")

```

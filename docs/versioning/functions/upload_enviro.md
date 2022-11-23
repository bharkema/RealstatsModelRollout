[<- Go back to Versioning()](../versioning.md)

## Upload_enviroment()
Versioning.Upload_enviroment(localpath = "")

This function allows you to copy a created Vmachine folder to a github repo where all data gets copied and versioned based on date


```python 
import RealstatsModelRollout as RMR

version = RMR.Versioning()
version.gitaccesstoken = "INPUT ACCESS TOKEN"

version.Upload_enviroment("C:/virtualenv_Actual/")

## Customise repo 
version.repo_name = "INSERT REPO NAME"

```

The function uses Pygithub to upload the data online and uses local systems to do the copying and versioning.

the function only works with string type files and byte files

[Go to PyGithub documentation ->](https://pygithub.readthedocs.io/en/latest/)
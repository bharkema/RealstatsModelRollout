[<- Go back to Versioning()](../versioning.md)

## Get_file_content()

Versioning.Get_file_content()

This function returns the encoded content form the online file

```python 
import RealstatsModelRollout as RMR

version = RMR.Versioning()
version.gitaccesstoken = "INPUT ACCESS TOKEN"
version.model_name = "INPUT FULL ENVIROMENT NAME"
version.model_version = "INPUT VERSION NUMBER"

data = version.Get_file_content()
```

The function uses Pygithub to upload the data online and uses local systems to do the copying and versioning.

the function only works with string type files and byte files

[Go to PyGithub documentation ->](https://pygithub.readthedocs.io/en/latest/)
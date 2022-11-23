[<- Go back to main page](https://bharkema.github.io/RealstatsModelRollout/)

## Download_enviroment()

Versioning.Download_enviroment(localpath = "", generate_venv = True/False)

This function allows you to copy a versioned model setup to your local machine. after which you can start working on it.

This function has no return and will just copy the files to the given directory

```python 
import RealstatsModelRollout as RMR

version = RMR.Versioning()
version.gitaccesstoken = "INPUT ACCESS TOKEN"
version.model_name = "INPUT FULL ENVIROMENT NAME"
version.model_version = "INPUT VERSION NUMBER"

version.Download_enviroment("C:/test/", False)
```

The function uses Pygithub to upload the data online and uses local systems to do the copying and versioning.

the function only works with string type files and byte files

[Go to PyGithub documentation ->](https://pygithub.readthedocs.io/en/latest/)
[<- Go back to main page](../index.md)

## Versioning()

### How to use the class
With versioning you have the ability to upload generated Vmachine folders and corresponding data to the cloud. It has default systems in place wich makes it easier for the user to auto upload the data online

the following functions are available in Versioning():
* [Upload_enviroment()](./functions/upload_enviro.md)
* [Download_enviroment()](./functions/download_enviro.md)
* [Get_file_content()](./functions/download_file.md)

More in depth information can be found in the links above

### Code examples
``` python 
import RealstatsModelRollout as RMR

# Upload full enviroment
version = RMR.Versioning()
version.gitaccesstoken = "INPUT ACCESS TOKEN"

version.Upload_enviroment("C:/virtualenv_Actual/")


# Download full enviroment
version = RMR.Versioning()
version.gitaccesstoken = "INPUT ACCESS TOKEN"
version.model_name = "INPUT FULL ENVIROMENT NAME"
version.model_version = "INPUT VERSION NUMBER"

version.Download_enviroment("C:/test/", False)


# Download content of file
version = RMR.Versioning()
version.gitaccesstoken = "INPUT ACCESS TOKEN"
version.model_name = "INPUT FULL ENVIROMENT NAME"
version.model_version = "INPUT VERSION NUMBER"

data = version.Get_file_content()


```


### Properties within class
``` python
    @property
    def Repo_name(self):
        """
        :type: string
        """
        return self._repo_name

    @Repo_name.setter
    def Repo_name(self, value):
        """
        :type: string
        """
        self._repo_name = value

    @property
    def Gitaccesstoken(self):
        """
        :type: string
        """
        return self._gitaccesstoken
    
    @Gitaccesstoken.setter
    def Gitaccesstoken(self, value):
        """
        :type: string
        """
        self._gitaccesstoken = value

    @property
    def Model_version(self):
        """
        :type: string
        """
        return self._model_version

    @Model_version.setter
    def Model_version(self, value):
        """
        :type: string
        """
        self._model_version = value

    @property
    def Model_name(self):
        """
        :type: string
        """
        return self._model_name

    @Model_name.setter
    def Model_name(self, value):
        """
        :type: string
        """
        self._model_name = value
```
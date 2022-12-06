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
version.Repo_name = "NAME OF GITHUB REPO"
version.Gitaccesstoken = "INPUT ACCESS TOKEN"

version.Upload_enviroment("C:/virtualenv_Actual/")


# Download full enviroment
version = RMR.Versioning()
version.Gitaccesstoken = "INPUT ACCESS TOKEN"
version.Model_name = "INPUT FULL ENVIROMENT NAME"
version.Model_version = "INPUT VERSION NUMBER"

version.Download_enviroment("C:/test/", False)


# Download content of file
version = RMR.Versioning()
version.Gitaccesstoken = "INPUT ACCESS TOKEN"
version.Model_name = "INPUT FULL ENVIROMENT NAME"
version.Model_version = "INPUT VERSION NUMBER"

data = version.Get_file_content()


```


### Properties within class
``` python
    @property
    def Repo_name(self):
        """
        :type: string
        """

    @property
    def Branch_name(self):
        """
        :type: string
        """

    @property
    def Model_version(self):
        """
        :type: string
        """

    @property
    def Model_name(self):
        """
        :type: string
        """
```
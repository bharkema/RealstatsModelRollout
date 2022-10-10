from .settings import settings
from .global_functions import globalFunctions
from github import Github
from datetime import date
import os
import json

class Versioning():
    def __init__(self, repo_name="bharkema/model_test", model_version="1", gitaccesstoken="development"):
        self._repo_name = repo_name
        self._model_version = model_version
        self._gitaccesstoken = gitaccesstoken

    @property
    def repo_name(self):
        """
        :type: string
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, value):
        """
        :type: string
        """
        self._repo_name = value

    @property
    def gitaccesstoken(self):
        """
        :type: string
        """
        return self._gitaccesstoken
    
    @gitaccesstoken.setter
    def gitaccesstoken(self, value):
        """
        :type: string
        """
        self._gitaccesstoken = value

    @property
    def model_version(self):
        """
        :type: int
        """
        return self._model_version

    @model_version.setter
    def model_version(self, value):
        """
        :type: int
        """
        self._model_version = value

    def Upload_enviroment(self, enviroment_localpath="Development"):
        git = Github(self._gitaccesstoken)
        git_repo = ""
        try:             
            git_repo = git.get_repo(self._repo_name)
        except:
            print("Not able to get given repo: " + self.repo_name)
            return

        git_user = git.get_user()
        git_user_data = git_user.get_emails()

        local_envpath = ""
        ### Get directory ###
        print("Looking for directory")
        if enviroment_localpath != "Development":
            if enviroment_localpath[-1] == '/':
                local_envpath = enviroment_localpath
            else: 
                local_envpath = enviroment_localpath + "/"
        else: 
            local_envpath = settings.base_path + "virtualenv_" + settings.enviroment_name + "/"
        
        isDirectory = os.path.isdir(local_envpath)
        if isDirectory == False:
            return "This is not a correct directory"

        indexes = globalFunctions.find(local_envpath, "/")
        max_count = len(indexes) - 1
        env_name = local_envpath[indexes[max_count - 1] + 1:indexes[max_count]]

        ### Collect all data needed in dir ###
        print("Collecting data")
        requirements_file = open(local_envpath + "requirements.txt", "r")
        requirements_string = requirements_file.read()

        model_file = open(local_envpath + "/model/model.pkl", "rb")
        model_file_data = model_file.read()

        validation_data_file = open(local_envpath + "data/data.gzip", "rb")
        validation_data_file_data = validation_data_file.read()

        validation_data_control_file = open(local_envpath + "data/data_control.gzip", "rb")
        validation_data_control_file_data = validation_data_control_file.read()

        main_py_file = open(local_envpath + "main.py", "r")
        main_py_file_data = main_py_file.read()

        function_py_file = open(local_envpath + "code/validate.py", "r")
        function_py_file_data = function_py_file.read()

        ### Generate date version
        print("Generating version data")
        today = date.today()
        Date_string = today.strftime("%d%m%Y")

        version_data = {
            "Upload_date": today.strftime("%d/%m/%Y"),
            "Model_name": env_name,
            "Package_version": settings.package_version,
            "Requirements": requirements_string,
            "uploaded_by": git_user_data[0].email
        }

        ### Upload to Git ###
        print("Uploading to Git")
        gitFilePath =  env_name + "/" + Date_string
        commitMessage = env_name + " - " + Date_string + " published"

        # Create requirements file
        appFilePath =  gitFilePath + "_requirements.txt"
        git_repo.create_file(appFilePath, commitMessage, requirements_string, branch="main")
        print("Requirements... done!")

        # Create main.py file
        appFilePath =  gitFilePath + "main.py"
        git_repo.create_file(appFilePath, commitMessage, main_py_file_data, branch="main")
        print("Main code... done!")

        # Create python custom code file
        appFilePath =  gitFilePath + "function.py"
        git_repo.create_file(appFilePath, commitMessage, function_py_file_data, branch="main")
        print("Custom code... done!")

        # Create Validation data file
        appFilePath =  gitFilePath + "validation_data.gzip"
        git_repo.create_file(appFilePath, commitMessage, validation_data_file_data, branch="main")
        print("Validation data... done!")

        # Create validation control data file
        appFilePath =  gitFilePath + "validation_control_data.gzip"
        git_repo.create_file(appFilePath, commitMessage, validation_data_control_file_data, branch="main")
        print("Validation control data... done!")

        # Create model data file
        appFilePath =  gitFilePath + "model.pkl"
        git_repo.create_file(appFilePath, commitMessage, model_file_data, branch="main")
        print("Model data... done!")

        # Create version data file
        version_info_json = json.loads(version_data)
        appFilePath =  gitFilePath + "version_info.json"
        git_repo.create_file(appFilePath, commitMessage, version_info_json, branch="main")
        print("Model data... done!")
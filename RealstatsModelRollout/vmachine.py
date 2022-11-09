import os
import platform
import subprocess
import pandas as pd
from .settings import Settings
from .global_functions import globalFunctions as GF
import pickle
import gzip


class Vmachine:
    def __init__(self):
        self._dev_platform = platform.system()
        self._dev_platform_vers = platform.version()
        self._dev_platform_release = platform.release()

        print("Platform: " + self._dev_platform)
        print("Platform version: " + self._dev_platform_vers)
        print("Platform release: " + self._dev_platform_release)

    @property
    def Dev_platform(self):
        """
        :type: string
        """
        return self._dev_platform

    @Dev_platform.setter
    def Dev_platform(self, value):
        """
        :type: string
        """
        self._dev_platform = value

    @property
    def Dev_platform_vers(self):
        """
        :type: string
        """
        return self._dev_platform_vers

    @Dev_platform_vers.setter
    def Dev_platform_vers(self, value):
        """
        :type: string
        """
        self._dev_platform_vers = value

    @property
    def Dev_platform_release(self):
        """
        :type: string
        """
        return self._dev_platform_release

    @Dev_platform_release.setter
    def Dev_platform_release(self, value):
        """
        :type: string
        """
        self._dev_platform_release = value

    #### Generates folder structer of the virtual enviroment and copy's data from given locations ####
    def Generate_structure(self, model_save_location, model_name, model_current_location):
        Settings.Base_path = model_save_location
        Settings.Enviroment_name = model_name

        model_current_location = GF.Path_is_dir(model_current_location)
        model_save_location = GF.Path_is_dir(model_save_location)

        print("Searching for needed files...")
        file_pathlist = []
        folder_pathlist = []
        needed_files = ["model", "data_control", "data"]
        collectible_files = [
            {
                "file_name": "main",
                "file_path": "",
                "file_extension": ".py",
                "saving_path": model_save_location + "virtualenv_" + model_name + "/main.py"
            },
            {
                "file_name": "functions",
                "file_path": "",
                "file_extension": ".py",
                "saving_path": model_save_location + "virtualenv_" + model_name + "/ms/functions.py"
            },
            {
                "file_name": "__init__",
                "file_path": "",
                "file_extension": ".py",
                "saving_path": model_save_location + "virtualenv_" + model_name + "/ms/__init__.py"
            },
            {
                "file_name": "documentation",
                "file_path": "",
                "file_extension": ".txt",
                "saving_path": model_save_location + "virtualenv_" + model_name + "/docs/documentation.txt"
            },
            {
                "file_name": "requirements",
                "file_path": "",
                "file_extension": ".txt",
                "saving_path": model_save_location + "virtualenv_" + model_name + "/requirements.txt"
            },
            {
                "file_name": "model",
                "file_path": "",
                "file_extension": "",
                "saving_path": model_save_location + "virtualenv_" + model_name + "/model/model.pkl"
            },
            {
                "file_name": "data_control",
                "file_path": "",
                "file_extension": "",
                "saving_path": model_save_location + "virtualenv_" + model_name + "/data/data_control.gzip"
            },
            {
                "file_name": "data",
                "file_path": "",
                "file_extension": "",
                "saving_path": model_save_location + "virtualenv_" + model_name + "/data/data.gzip"
            }
        ]

        # For loop to go trough first folder and get all files + remaining folders
        for path in os.listdir(model_current_location):
            if path.endswith(".py") or path.endswith(".txt") or path.endswith(".pkl") or path.endswith(".csv") or path.endswith(".gzip"):
                file_pathlist.append(model_current_location + "/" + path)
                for item in collectible_files:
                    if path == item["file_name"] + item["file_extension"]:
                        item["file_path"] = model_current_location + "/" + path
                    elif path == item["file_name"] + ".csv":
                        item["file_extension"] = ".csv"
                        item["file_path"] = model_current_location + "/" + path
                    elif path == item["file_name"] + ".pkl":
                        item["file_extension"] = ".pkl"
                        item["file_path"] = model_current_location + "/" + path
                    elif path == item["file_name"] + ".gzip":
                        item["file_path"] = model_current_location + "/" + path
                        item["file_extension"] = ".gzip"
            elif "." not in path:
                if path == "model" or path == "ms" or path == "docs" or path == "data" or path == "code":
                    folder_pathlist.append(model_current_location + "/" + path)

        # For loop to get fill extra folders and find remaining files
        for folder in folder_pathlist:
            for path in os.listdir(folder):
                if path.endswith(".py") or path.endswith(".txt") or path.endswith(".pkl") or path.endswith(".csv") or path.endswith(".gzip"):
                    file_pathlist.append(folder + "/" + path)
                    for item in collectible_files:
                        if path == item["file_name"] + item["file_extension"]:
                            item["file_path"] = folder + "/" + path
                        elif path == item["file_name"] + ".csv":
                            item["file_path"] = folder + "/" + path
                            item["file_extension"] = ".csv"
                        elif path == item["file_name"] + ".pkl":
                            item["file_path"] = folder + "/" + path
                            item["file_extension"] = ".pkl"
                        elif path == item["file_name"] + ".gzip":
                            item["file_path"] = folder + "/" + path
                            item["file_extension"] = ".gzip"
                elif "." not in path and "activate" not in path:
                    folder_pathlist.append(folder + "/" + path)

        #### Check if needed files are in the system ####
        print("Checking if needed files are found...")
        for item in collectible_files:
            if item["file_name"] in needed_files and item["file_path"] == "":
                raise FileNotFoundError(
                    "Not able to find: " + item["file_name"])

        #### Start copying files to generated folder structure ####
        # vars for saving data
        validation_content = pd.DataFrame()
        validation_control_content = pd.DataFrame()
        function_content = ""
        requirements_content = ""
        documentation_content = ""
        main_content = ""
        ms_init_content = ""
        ms_functions_content = ""

        #### Start generating folder and files within folder ####
        print("Starting folder generation...")
        for file in collectible_files:
            os.makedirs(os.path.dirname(item["saving_path"]), exist_ok=True)
            if file["file_name"] == "main":
                if file["file_path"] == "":
                    main_content = Settings.Premade_main_code_data
                else:
                    main_content = open(file["file_path"], "r")
                with open(file["saving_path"], "w") as f:
                    f.write(main_content)
            elif file["file_name"] == "functions":
                if file["file_path"] == "":
                    ms_functions_content = Settings.Premade_main_code_data
                else:
                    ms_functions_content = open(file["file_path"], "r")
                with open(file["saving_path"], "w") as f:
                    f.write(ms_functions_content)
            elif file["file_name"] == "__init__":
                if file["file_path"] == "":
                    ms_init_content = Settings.Premade_main_code_data
                else:
                    ms_init_content = open(file["file_path"], "r")
                with open(file["saving_path"], "w") as f:
                    f.write(ms_init_content)
            elif file["file_name"] == "documentation":
                if file["file_path"] == "":
                    documentation_content = Settings.Premade_documentation_data
                else:
                    documentation_content = open(file["file_path"], "r")
                with open(file["saving_path"], "w") as f:
                    f.write(documentation_content)
            elif file["file_name"] == "requirements":
                if file["file_path"] == "":
                    requirements_content = Settings.Premade_requirements_data
                else:
                    requirements_content = open(file["file_path"], "r")
                with open(file["saving_path"], "w") as f:
                    f.write(requirements_content)
            elif file["file_name"] == "model":
                if file["file_extension"] == ".gz":
                    model_file = gzip.open(file["file_path"], "rb")
                    model_file_content = model_file.read()
                elif file["file_extension"] == ".pkl":
                    model_file = pd.read_pickle(file["file_path"])
                copy_model_file = open(file["saving_path"], "wb")
                pickle.dump(model_file_content, copy_model_file)
                copy_model_file.close()
                model_file.close()
            elif file["file_name"] == "data":
                if file["file_extension"] == ".csv":
                    validation_content = pd.read_csv(file["file_path"])
                elif file["file_extension"] == ".pkl":
                    validation_content = pd.read_pickle(file["file_path"])
                elif file["file_extension"] == ".gzip":
                    validation_content = pd.read_parquet(file["file_path"])
                validation_content.to_parquet(item["saving_path"])
            elif file["file_name"] == "data_control":
                if file["file_extension"] == ".csv":
                    validation_control_content = pd.read_csv(file["file_path"])
                elif file["file_extension"] == ".pkl":
                    validation_control_content = pd.read_pickle(
                        file["file_path"])
                elif file["file_extension"] == ".gzip":
                    validation_control_content = pd.read_parquet(
                        file["file_path"])
                validation_control_content.to_parquet(item["saving_path"])

        #### Create files needed for the virtual machine ####
        print("Generating VENV Data")
        cmd = 'python -m venv ' + Settings.Base_path + 'virtualenv_' + model_name
        p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
        print(p.stdout.decode())

        #### Finish ####
        print("Virtual machine folder structure created on: " +
              Settings.Base_path + "/virtualenv_" + model_name)
        return True


    #### This function will start the virtual enviroment on a local machine ####
    def Start_venv(self, localpath="", execution_code=""):
        if self._dev_platform == "Windows":
            print("starting virtual machine for Windows")
            # & python code/' + execution_code + ' .py
            cmd = 'pip install virtualenv & cd ' + localpath + ' & virtualenv venv & ' + localpath + \
                '/scripts/activate & cd c:/ & cd ' + localpath + \
                ' & dir & pip install -r requirements.txt & uvicorn main:app'

            # Start the virtual enviroment with the code.
            p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())

        elif self._dev_platform == "Linux":
            print("starting virtual machine for Linux")
            cmd = 'pip install virtualenv ; cd ' + localpath + ' ; virtualenv venv ; ' + localpath + '/scripts/activate ; cd c:/ ; cd ' + \
                localpath + ' ; dir ; pip install -r requirements.txt ; python code/' + \
                execution_code + ' ; uvicorn main:app'

            # Start the virtual enviroment with the code.
            p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())

        elif self._dev_platform == "MacOS":
            print("starting virtual machine for Apple")

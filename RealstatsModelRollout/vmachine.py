import os
import platform
import subprocess
import pandas
import settings

class vmachine:
    dev_platform = ""
    dev_platform_vers = ""
    dev_platform_release = ""

    def __init__(self):
        self.dev_platform = platform.system()
        self.dev_platform_vers = platform.version()
        self.dev_platform_release = platform.release()    

        print("Platform: " + self.dev_platform)
        print("Platform version: " + self.dev_platform_vers)
        print("Platform release: " + self.dev_platform_release)

    def Generate_structure(self, parentfolder="", df_validation_data="", model_file="", df_validation_control="", code_localpath=""):
        settings.folder_localpath = ""
        print("Hello")


    # This function will start the virtual enviroment on a local machine
    def start_venv(self, localpath="", code_filename=""):
        if self.dev_platform == "Windows":
            print("starting virtual machine for Windows")
            cmd ='pip install virtualenv & cd $$LOCALPATH$$ & virtualenv venv & $$LOCALPATH$$/scripts/activate & cd c:/ & cd $$LOCALPATH$$ & dir & pip install -r requirements.txt & python code/$$CODE_FILENAME$$ & uvicorn main:app'

            ## REGEX GENERATION

            # Start the virtual enviroment with the code.
            p = subprocess.run(cmd,shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())    

        elif self.dev_platform == "Linux":
            print("starting virtual machine for Linux")
            cmd ='C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/scripts/activate ; cd c:/ ; cd C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/ ; dir ; pip install -r requirements.txt ; python code/train.py ; uvicorn main:app'

            ## REGEX GENERATION

            # Start the virtual enviroment with the code.
            p = subprocess.run(cmd,shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())    
        
        elif self.dev_platform == "MacOS":
            print("starting virtual machine for Apple")

            
        
    def Generate_cmdline(self, command=""):
        return ""

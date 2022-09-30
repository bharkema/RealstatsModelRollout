from os import system
import platform
import subprocess

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


    def start_venv(self):
        if self.dev_platform == "Windows":
            print("starting virtual machine for Windows")
            cmd ='C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/scripts/activate & cd c:/ & cd C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/ & dir & pip install -r requirements.txt & python code/train.py & uvicorn main:app'

            # Start the virtual enviroment with the code.
            p = subprocess.run(cmd,shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())    

        elif self.dev_platform == "Linux":
            print("starting virtual machine for Linux")
            cmd ='C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/scripts/activate ; cd c:/ ; cd C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/ ; dir ; pip install -r requirements.txt ; python code/train.py ; uvicorn main:app'

            # Start the virtual enviroment with the code.
            p = subprocess.run(cmd,shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())    
            


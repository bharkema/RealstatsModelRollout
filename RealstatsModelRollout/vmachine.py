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


        elif self.dev_platform == "Linux":
            print("starting virtual machine for Linux")


        elif self.dev_platform == "MacOS":
            print("starting virtual machine for MacOS")
            
    def start_windows_env(self):
        process = subprocess.Popen(['echo', 'more output'],
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print(stdout, stderr)


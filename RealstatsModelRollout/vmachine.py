from os import system
import platform

class vmachine:
    dev_platform = ""
    dev_platform_vers = ""
    dev_platform_release = ""

    def init(self):
        self.dev_platform = platform.system()
        self.dev_platform_vers = platform.version()
        self.dev_platform_release = platform.release()    

    def start_venv(self):
        if self.dev_platform == "Windows":
            print("starting virtual machine for Windows")


        elif self.dev_platform == "Linux":
            print("starting virtual machine for Linux")


        elif self.dev_platform == "MacOS":
            print("starting virtual machine for MacOS")
            
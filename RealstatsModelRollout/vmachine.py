from os import system
import platform

class vmachine:
    def init():
        global dev_platform 
        global dev_platform_vers
        global dev_platform_release

        dev_platform = platform.system()
        dev_platform_vers = platform.version()
        dev_platform_release = platform.release()    

    def start_venv():
        if dev_platform == "Windows":
            print("starting virtual machine for Windows")


        elif dev_platform == "Linux":
            print("starting virtual machine for Linux")


        elif dev_platform == "MacOS":
            print("starting virtual machine for MacOS")
            
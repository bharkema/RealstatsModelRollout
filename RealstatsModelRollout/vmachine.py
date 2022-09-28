from .dev_enviroment import dev_enviroment

class vmachine:
    def init():
        global baseURL
        
    def start_venv():
        dev_enviroment.system_scan()


        if dev_enviroment.DEV_PLATFORM == "Windows":
            print("starting virtual machine for Windows")


        elif dev_enviroment.DEV_PLATFORM == "Linux":
            print("starting virtual machine for Linux")


        elif dev_enviroment.DEV_PLATFORM == "MacOS":
            print("starting virtual machine for MacOS")
            
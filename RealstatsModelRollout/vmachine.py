from .dev_enviroment import dev_enviroment

class vmachine:
    def init():
        global baseURL
        
    def start_venv():
        if dev_enviroment.dev_platform == "Windows":
            print("starting virtual machine for Windows")


        elif dev_enviroment.dev_platform == "Linux":
            print("starting virtual machine for Linux")


        elif dev_enviroment.dev_platform == "MacOS":
            print("starting virtual machine for MacOS")
            
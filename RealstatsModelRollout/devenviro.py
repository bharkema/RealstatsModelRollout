from os import system
import platform

class devenviro:
    def init ():
        global dev_platform 
        global dev_platform_vers
        global dev_platform_release

        dev_platform = platform.system()
        dev_platform_vers = platform.version()
        dev_platform_release = platform.release()

        print("Platform: " + dev_platform)
        print("Platform version: " + dev_platform_vers)
        print("Platform release: " + dev_platform_release)

    # def system_scan():
    #     dev_platform = platform.system()
    #     dev_platform_vers = platform.version()
    #     dev_platform_release = platform.release()
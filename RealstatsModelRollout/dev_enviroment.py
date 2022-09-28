from os import system
import platform

class dev_enviroment:
    def init ():
        global DEV_PLATFORM 
        global DEV_PLATFORM_RELEASE
        global DEV_PLATFORM_VERSION

    def system_scan():
        DEV_PLATFORM = platform.system()
        DEV_PLATFORM_VERSION = platform.version()
        DEV_PLATFORM_RELEASE = platform.release()

        print("Platform: " + DEV_PLATFORM)
        print("Platform version: " + DEV_PLATFORM_VERSION)
        print("Platform release: " + DEV_PLATFORM_RELEASE)
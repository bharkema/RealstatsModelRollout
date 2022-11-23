from .settings import settings
import os

# NOTES #


# VARS #
# These are global vars and need to be filled in when you want to test the package. Then also need to be removed when pushing to git
settings
settings.Gitaccesstoken = os.environ["API_KEY"]
settings.Main_path = os.environ["MAIN_PATH"]

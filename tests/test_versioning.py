import pytest
from github import Github
from RealstatsModelRollout import Versioning
from .settings import settings
from datetime import date
import os

def test_Download_enviroment():
    version = Versioning()
    version.Gitaccesstoken = settings.Gitaccesstoken
    version.Repo_name = "bharkema/model_test"
    version.Model_name = "virtualenv_Actual"
    version.Model_version = "11102022"
    assert version.Download_enviroment(settings.Main_path, False) == "Finished downloading"

def test_Get_file_content():
    version = Versioning()
    version.Gitaccesstoken = settings.Gitaccesstoken
    version.Repo_name = "bharkema/model_test"
    version.Model_name = "virtualenv_Actual"
    version.Model_version = "11102022"
    data = version.Get_file_content(["model.pkl", "main.py"])
    assert data[0] == b'\x80\x04\x95\x04\x00\x00\x00\x00\x00\x00\x00C\x00\x94.'

def test_Upload_enviroment():
    version = Versioning()
    version.Gitaccesstoken = settings.Gitaccesstoken
    version.Repo_name = "bharkema/model_test"

    resultvalue = version.Upload_enviroment(settings.Main_path + "/virtualenv_Actual/11102022/")

    git = Github(version.Gitaccesstoken)
    git_repo = ""
    try:
        git_repo = git.get_repo(version.Repo_name)
    except:
        print("Not able to get given repo: " + version.Repo_name)
        return

    ### Generate date version
    print("Generating version data")
    today = date.today()
    versionnumber = today.strftime("%d%m%Y")

    # Check if app with version already exists, if it does, append number
    versionInUse = True
    additional = 1
    while versionInUse:
        try:
            git_repo.get_contents("11102022/" + versionnumber + "/version_info.json")
            if additional == 1:
                versionnumber = versionnumber + "-" + str(additional)
            else:
                versionnumber = versionnumber[:-1]
                versionnumber = versionnumber + str(additional)
            additional+=1
        except:
            versionInUse = False
            pass
            break
    
    charloc = [i for i, ltr in enumerate(versionnumber) if ltr == '-']
    versionnumber = versionnumber[0: charloc[0] + 1]
    versionnumber = versionnumber + str(additional - 2)

    ## If the last digit is a 0 then remove that zero
    if versionnumber[len(versionnumber) - 1] == "0":
            if versionnumber[len(versionnumber) - 2] == "-":
                versionnumber = versionnumber[0 : charloc[0]]

    assert resultvalue == "Saved model data under: " + version.Repo_name + "/11102022/" + versionnumber

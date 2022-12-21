import pytest
from github import Github
from RealstatsModelRollout import Versioning
import RealstatsModelRollout as RMR
from .settings import settings
from datetime import date
import os


def test_Download_enviroment():
    version = Versioning()
    RMR.Settings.Gitaccesstoken = settings.Gitaccesstoken
    version.Repo_name = "bharkema/model_test"
    version.Model_name = "11102022"
    version.Model_version = "21122022-1"
    assert version.Download_enviroment(settings.Main_path, False) == "Finished downloading"

def test_Get_files_content():
    version = Versioning()
    RMR.Settings.Gitaccesstoken = settings.Gitaccesstoken
    version.Repo_name = "bharkema/model_test"
    version.Model_name = "virtualenv_Actual"
    version.Model_version = "11102022"
    data = version.Get_file_content(["functions.py", "main.py"])
    assert data[0] == b'\nimport pandas as pd\nimport numpy as np\nfrom ms import model\nfrom sklearn.metrics import mean_absolute_error\n\ndef predict(X, model):\n    prediction = model.predict(X)[0]\n    return prediction\n\ndef get_model_response(input):\n    X = pd.json_normalize(input.__dict__)\n    prediction = predict(X, model)\n    if prediction == 1:\n        label = "M"\n    else:\n        label = "B"\n    return {\n        \'label\': label,\n        \'prediction\': int(prediction)\n    }\n\ndef percentage_error(actual, predicted):\n    res = np.empty(actual.shape)\n    for j in range(actual.shape[0]):\n        if actual[j] != 0:\n            res[j] = (actual[j] - predicted[j]) / actual[j]\n        else:\n            res[j] = predicted[j] / np.mean(actual)\n    return res\n\ndef mean_absolute_percentage_error(y_true, y_pred):\n    return (1 - np.mean(np.abs(percentage_error(np.asarray(y_true), np.asarray(y_pred))))) * 100\n\n'

def test_Get_file_content():
    version = Versioning()
    RMR.Settings.Gitaccesstoken = settings.Gitaccesstoken
    version.Repo_name = "bharkema/model_test"
    version.Model_name = "virtualenv_Actual"
    version.Model_version = "11102022"
    data = version.Get_file_content("functions.py")
    assert data[0] == b'\nimport pandas as pd\nimport numpy as np\nfrom ms import model\nfrom sklearn.metrics import mean_absolute_error\n\ndef predict(X, model):\n    prediction = model.predict(X)[0]\n    return prediction\n\ndef get_model_response(input):\n    X = pd.json_normalize(input.__dict__)\n    prediction = predict(X, model)\n    if prediction == 1:\n        label = "M"\n    else:\n        label = "B"\n    return {\n        \'label\': label,\n        \'prediction\': int(prediction)\n    }\n\ndef percentage_error(actual, predicted):\n    res = np.empty(actual.shape)\n    for j in range(actual.shape[0]):\n        if actual[j] != 0:\n            res[j] = (actual[j] - predicted[j]) / actual[j]\n        else:\n            res[j] = predicted[j] / np.mean(actual)\n    return res\n\ndef mean_absolute_percentage_error(y_true, y_pred):\n    return (1 - np.mean(np.abs(percentage_error(np.asarray(y_true), np.asarray(y_pred))))) * 100\n\n'

def test_Upload_enviroment():
    rmrversion = Versioning()
    RMR.Settings.Gitaccesstoken = settings.Gitaccesstoken
    rmrversion.Repo_name = "bharkema/model_test"

    git = Github(settings.Gitaccesstoken)
    git_repo = ""
    try:
        git_repo = git.get_repo(rmrversion.Repo_name)
    except Exception as e:
        print(e)
        print("Not able to get given repo: " + rmrversion.Repo_name)
        return

    # Code to get the correct version
    today = date.today()
    version = today.strftime("%d%m%Y")

    # Check if app with version already exists, if it does, append number
    versionInUse = True
    additional = 1
    while versionInUse:
        try:
            git_repo.get_contents(
                "11102022/" + version + "/version_info.json")
            if additional == 1:
                version = version + "-" + str(additional)
            else:
                charloc = [i for i, ltr in enumerate(
                    version) if ltr == '-']
                version = version[0: charloc[0] + 1]
                version = version + str(additional)
            additional += 1
        except Exception as e:
            print(e)
            versionInUse = False
            pass
            break

    settings.versionnumber = version

    # Need to add data file in testing because of download limitations
    os.makedirs(os.path.dirname(settings.Main_path + "11102022/data/train_data_model.pkl"), exist_ok=True)
    with open(settings.Main_path + "11102022/data/train_data_model.pkl", "wb") as fb:
        fb.write(b'')

    # Need to add model file in testing because of download limitations
    os.makedirs(os.path.dirname(settings.Main_path + "11102022/model/trained_model.pkl"), exist_ok=True)
    with open(settings.Main_path + "11102022/model/trained_model.pkl", "wb") as fb:
        fb.write(b'')

    resultvalue = rmrversion.Upload_enviroment(settings.Main_path + "11102022/")
    assert resultvalue == rmrversion.Repo_name + "/11102022/" + version


def test_Delete_saved_model():
    rmrversion = Versioning()
    RMR.Settings.Gitaccesstoken = settings.Gitaccesstoken
    rmrversion.Repo_name = "bharkema/model_test"
    result = rmrversion.Delete_saved_model(model_name="11102022", model_version=settings.versionnumber)
    assert result is True

import requests

# Get latest version release for deployment on Pypi
response = requests.get("https://api.github.com/repos/bharkema/RealstatsModelRollout/releases/latest")
__version__ = response.json()["tag_name"]


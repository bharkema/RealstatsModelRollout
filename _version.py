import requests

response = requests.get("https://api.github.com/repos/bharkema/RealstatsModelRollout/releases/latest"),
__version__ = response.json()["tag_name"]


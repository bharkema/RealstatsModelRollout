import cmd
import os
import subprocess
import requests


# def request_data():
#     respone = requests.get('http://127.0.0.1:8000/')
#     print(respone.content)  


# cmd ='C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/scripts/activate & cd c:/ & cd C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/ & dir & pip install -r requirements.txt & python code/train.py & uvicorn main:app'

# # Start the virtual enviroment with the code.
# p = subprocess.run(cmd,shell=True, stdout=subprocess.PIPE)
# print(p.stdout.decode())    

folders = [ "/virtualenv/code/train.py",
            "/virtualenv/data/dat.csv",
            "/virtualenv/model/model.dat.gz",
            "/virtualenv/requirements.txt",
            "/virtualenv/tests/example_calls.txt",
            "/virtualenv/main.py"
           ]

for item in folders: 
    os.makedirs(os.path.dirname(item), exist_ok=True)
    with open(item, "w") as f:
        f.write("FOOBAR")
import cmd
import os
import subprocess
import requests


def request_data():
    respone = requests.get('http://127.0.0.1:8000/')
    print(respone.content)  


cmd ='C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/scripts/activate & cd c:/ & cd C:/Users/ClappForm/Desktop/model_rollout/tutorialenv/ & dir & pip install -r requirements.txt & python code/train.py & uvicorn main:app'

# Start the virtual enviroment with the code.
p = subprocess.run(cmd,shell=True, stdout=subprocess.PIPE)
print(p.stdout.decode())    


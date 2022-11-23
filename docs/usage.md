[<- Go back to main page](https://bharkema.github.io/RealstatsModelRollout/)

# Usage of the package


## Starting from scratch
``` py
import RealstatsModelRollout as RMR

# get all your data from your model and its corresponding data in one location
# and try to hold the following folder structure
# The files with a MUST behind the line must be available for the system to use
# | project root
#     |__ data
#         |__> data (.gzip, .csv, .pkl)               (MUST)
#         |__> data_control (.gzip, .csv, .pkl)       (OPTIONAL)
#     |__ docs
#         |__> documentation.txt                      (OPTIONAL)
#     |__ model
#         |__> model.pkl (.gz)                        (OPTIONAL)
#     |__ ms
#         |__> __init__.py                            (OPTIONAL)
#         |__> functions.py                           (OPTIONAL)
#     |__> main.py                                    (OPTIONAL)
#     |__> requirements.txt                           (OPTIONAL)

# Please use the naming used in the above folder structure diagram for 
# the files so the system can automatically find the files

# Following the setup of the folder vmachine can be used by calling the following
vmachine = RMR.Vmachine()

vmachine.Generate_structure(model_save_location="WHERE YOU WANT TO SAVE", 
                                model_name="MODEL NAME", model_current_location="PATH OF WHERE PROJECT IS")

# Vmachine will find the files needed if it can and will look in folders as well. 
# Do make sure the files are within a maximum of 10 folders the system will stop the operation when the 
# count is exceeded. When the system is succesful you will see the following logs:

# >>> Looking for directory
# >>> Looking for directory
# >>> Searching for needed files...
# >>> Checking if needed files are found...
# >>> Starting folder generation...
# >>> Generating VENV Data
# >>> 
# >>> Virtual machine folder structure created on: PATH PROVIDED + MODEL_NAME

# by calling Start_venv the enviroment will start
vmachine.Start_venv(self, localpath="%PATH TO ENVIROMENT FOLDER%",
                            execution_code="%NAME OF CODE FILE YOU WISH TO EXECUTE%"):


# You can now start using the model by using either of the following:
model = RMR.Model()
model.Model_URL = "URL"
model.Model_port = "8000"

# To get the information of a model
model.Info_request()

# To get a prediction
json_data = {}
model.Predict_request(json_data=json_data)

# To send a custom request to the model if possible
model.Custom_request(request_type="post", pathing="user/auth", json_data='Development')

# You can also start the validation of the model
validation = RMR.Validate()
validation.MAE_Deviation_percentage = 3 # % (from 0 to 100)
validation.Mae_expected_value = 20
validation.R2_Deviation_percentage = 2 # % (from 0 to 100)
validation.R2_expected_value = 80 # % (from 0 to 100)

validation.Start_validation()

# This wil the start the validation and if the conditions have been met 
# it wil save the model to the default github repo and ready it for online deployment

```
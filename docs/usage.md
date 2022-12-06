[<- Go back to main page](index.md)

# Usage of the package


## Starting from scratch
``` py
import RealstatsModelRollout as RMR

# get all your data from your model and its corresponding data in one location
# and try to hold the following folder structure
# The files with a MUST behind the line must be available for the system to use
# | project root
#     |__ data
#         |__> train_data_model (.gzip, .csv, .pkl)   (MUST)
#     |__ docs
#         |__> documentation.txt                      (OPTIONAL)
#     |__ model
#         |__> trained_model.pkl (.gz)                (OPTIONAL)
#     |__ ms
#         |__> __init__.py                            (OPTIONAL)
#         |__> functions.py                           (OPTIONAL)
#     |__> main.py                                    (OPTIONAL)
#     |__> requirements.txt                           (OPTIONAL)

# Please use the naming used in the above folder structure diagram for
# the files so the system can automatically find the files or supply the files in a single folder.
# The system will also build the venv in the same structure

# Following the setup of the folder vmachine can be used by calling the following
venv_machine = RMR.Vmachine()

venv_machine.Generate_structure(model_current_location="Location of where the data is", model_save_location="Where do you wish to save the data", model_name="the name of the model")

# by calling Start_venv the enviroment will start
venv_machine.Start_venv()

# Vmachine will find the files needed if it can and will look in folders as well. 
# Do make sure the files are within a maximum of 10 folders the system will stop the operation when the 
# count is exceeded.

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

# You can also start the validation of the model and saving og the model
features = []
best_param_values = {}

valid.MAE_Deviation_percentage = 5 # % (from 0 to 100)
valid.MAE_expected_value = 150 # Any value
valid.MAPE_Deviation_percentage = 3 # % (from 0 to 100)
valid.MAPE_expected_value = 90 # % (from 0 to 100)
valid.R2_Deviation_percentage = 10 # % (from 0 to 100)
valid.R2_expected_value = 80 # % (from 0 to 100)

valid.Feature_array = features
valid.Model_parameters = best_param_values
valid.Model_target = "Target name"

RMR.Settings.Gitaccesstoken = "Your personal github access token" 

# Please look at the github documentation for how to use this key. DO MAKE SURE TO USE YOUR OWN. 
# The package uses the access token to write and sign the model when it is uploaded this is for communication sake

valid.Start_validation(repo_name="bharkema/model_test")

# This wil the start the validation and if the conditions have been met, it wil save the model 
# to the default github repo and ready it for online deployment.

# if you do not provide the repo name it will still run the validation and 
# save the results locally but will not save the model and results to Github

```
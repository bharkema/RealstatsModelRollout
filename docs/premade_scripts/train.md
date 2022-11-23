[<- Go back to main page](../index.md)

# ms/train_model.py 
These scripts can be used to edit the functionality of the package
```python
# import general packages
import pandas as pd
import os
import joblib
from datetime import date

# import validation functions
from ms.functions import percentage_error
from ms.functions import mean_absolute_percentage_error

# import model training systems
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import train_test_split

# Class for the model and training
class train_model:
    # General function for calling and training model
    def Execute_training_testing(feature_array, param_values, target):
        # Save locations
        SAVE_MODEL = os.getcwd() + '/model/trained_model.pkl'
        train_data = pd.read_pickle(os.getcwd() + '/data/train_data_model.pkl')

        # Define features
        features = feature_array

        # Zet feature data types goed
        for i in range(len(features)):
            features[i] = features[i].lower()

        # Corrigeer columns namen
        train_data.columns = train_data.columns.str.lower()
        train_data = train_data.loc[:, ~train_data.columns.duplicated()]

        # Defineer target en relevant columns
        target = [target]

        # Train model
        y = train_data[target]
        X = train_data[features]

        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            train_size=0.75, test_size=0.25,
                                                            random_state=10)

        best_param_values = list(param_values.values())

        if best_param_values[0] == 0:
            boosting_type = 'gbdt'
        else:
            boosting_type = 'dart'

        model = LGBMRegressor(
            learning_rate=best_param_values[2],
            num_leaves=int(best_param_values[5]),
            max_depth=int(best_param_values[3]),
            n_estimators=int(best_param_values[4]),
            boosting_type=boosting_type,
            colsample_bytree=best_param_values[1],
            reg_lambda=best_param_values[6],
            random_state=10
        )

        model.fit(X_train, y_train,
                eval_metric='l1',
                eval_set=[(X_test, y_test)],
                early_stopping_rounds=500,
                verbose=0
                )

        # Get results of the test to check the model functionality these get send back to package
        preds = model.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        mape = mean_absolute_percentage_error(y_test, preds)
        r2 = r2_score(y_test, preds)

        # Retrain model with full dataset for versioning and saving
        model.fit(X, y,
                eval_metric='l1',
                verbose=0)
        joblib.dump(value=model, filename=SAVE_MODEL)

        # Return needed values for the package to continue work
        return {
            "mae_value": mae,
            "r2_value": r2,
            "mape_value": mape,
            "features": features
        }


```
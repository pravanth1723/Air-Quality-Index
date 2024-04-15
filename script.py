# script.py

import pickle
import xgboost as xgb
import numpy as np
import pandas as pd
import math
import sklearn
from sklearn.ensemble import BaggingRegressor
from joblib import load

def calculate_result(input_data):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    input_array = input_data.split(",")
    input_array_1= [np.log(float(x)) for x in input_array]
    input_array_1= np.array(input_array_1)
    input_array_reshaped = input_array_1.reshape(1, -1)
    predictions = model.predict(input_array_reshaped)
    denormalized_predictions = np.exp(predictions[0])
    return denormalized_predictions

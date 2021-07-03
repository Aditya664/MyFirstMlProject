import json
import pickle
import sklearn
import numpy as np
import os

#using gloabl variables
__locations = None
__data_columns = None
__model = None


def get_etimated_prices(location, total_sqft,bath, balcony, Bedroom):

    try:
        loc_index = __data_columns.index(location.lower()) # to get column number of location, if other location then zero
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = balcony
    x[3] = Bedroom
    if loc_index >= 0:
        x[loc_index] = 1

    return np.round(__model.predict([x])[0][0],2)

def load_saved_predictors():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    path = os.path.dirname(__file__)
    predictors = os.path.join(path, "predictors"),


    with open(predictors[0] + "/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]  # first 4 columns are sqft, bath, balcony, bhk

    global __model
    if __model is None:
        with open(predictors[0] + "/bangalore_home_price_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():

    return __locations

def get_data_columns():
    return __data_columns

load_saved_predictors()

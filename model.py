"""

    Helper functions for the pretrained model to be used within our API.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Plase follow the instructions provided within the README.md file
    located within this directory for guidance on how to use this script
    correctly.

    Importantly, you will need to modify this file by adding
    your own data preprocessing steps within the `_preprocess_data()`
    function.
    ----------------------------------------------------------------------

    Description: This file contains several functions used to abstract aspects
    of model interaction within the API. This includes loading a model from
    file, data preprocessing, and model prediction.  

"""

# Helper Dependencies
import numpy as np
import pandas as pd
import pickle
import json

def _preprocess_data(data):
    """Private helper function to preprocess data for model prediction.

    NB: If you have utilised feature engineering/selection in order to create
    your final model you will need to define the code here.


    Parameters
    ----------
    data : str
        The data payload received within POST requests sent to our API.

    Returns
    -------
    Pandas DataFrame : <class 'pandas.core.frame.DataFrame'>
        The preprocessed data, ready to be used our model for prediction.

    """
    # Convert the json string to a python dictionary object
    feature_vector_dict = json.loads(data)
    # Load the dictionary as a Pandas DataFrame.
    feature_vector_df = pd.DataFrame.from_dict([feature_vector_dict])

    # ---------------------------------------------------------------
    # NOTE: You will need to swap the lines below for your own data
    # preprocessing methods.
    #
    # The code below is for demonstration purposes only. You will not
    # receive marks for submitting this code in an unchanged state.
    # ---------------------------------------------------------------

    # ----------- Replace this code with your own preprocessing steps --------
    #predict_vector = feature_vector_df[['Pickup Lat','Pickup Long',
    #                                    'Destination Lat','Destination Long']]
    
    #Drop data not available in test, Pickup Time + label = Arrival times
    feature_vector_df = feature_vector_df.drop(['Arrival at Destination - Day of Month', 'Arrival at Destination - Weekday (Mo = 1)', 'Arrival at Destination - Time'], axis=1)

    #Renaming columns (shorten, remove space, standardize)
    new_names = {"Order No": "Order_No", "User Id": "User_Id", "Vehicle Type": "Vehicle_Type",
    "Personal or Business": "Personal_Business", "Placement - Day of Month": "Pla_Mon",
    "Placement - Weekday (Mo = 1)": "Pla_Weekday", "Placement - Time": "Pla_Time", 
    "Confirmation - Day of Month":"Con_Day_Mon", "Confirmation - Weekday (Mo = 1)": "Con_Weekday","Confirmation - Time": "Con_Time", 
    "Arrival at Pickup - Day of Month": "Arr_Pic_Mon", "Arrival at Pickup - Weekday (Mo = 1)": "Arr_Pic_Weekday", 
                "Arrival at Pickup - Time": "Arr_Pic_Time", "Platform Type": "Platform_Type",
     "Pickup - Day of Month": "Pickup_Mon", "Pickup - Weekday (Mo = 1)": "Pickup_Weekday",           
    "Pickup - Time": "Pickup_Time",  "Distance (KM)": "Distance(km)",
    "Precipitation in millimeters": "Precipitation(mm)", "Pickup Lat": "Pickup_Lat", "Pickup Long": "Pickup_Lon", 
    "Destination Lat": "Destination_Lat", "Destination Long":"Destination_Lon", "Rider Id": "Rider_Id",
                            "Time from Pickup to Arrival": "Time_Pic_Arr"
                           }
    feature_vector_df = feature_vector_df.rename(columns=new_names)
    
    #Convert Time from 12H to 24H
    def convert_to_24hrs(feature_vector_df):
        
        for col in feature_vector_df.columns:
            if col.endswith("Time"):
                feature_vector_df[col] = pd.to_datetime(feature_vector_df[col], format='%I:%M:%S %p').dt.strftime("%H:%M:%S")
        return feature_vector_df

    feature_vector_df = convert_to_24hrs(feature_vector_df)

    feature_vector_df[['Pla_Time', 'Con_Time' , 'Arr_Pic_Time', 'Pickup_Time']][3:6]
    
    #Filling Missing Values for temperatures and humidity
    feature_vector_df['Temperature'] = feature_vector_df['Temperature'].fillna(feature_vector_df['Temperature'].mean())
    feature_vector_df['Precipitation(mm)'].fillna(feature_vector_df['Precipitation(mm)'].mean(), inplace=True)
    
    #Since, we have not been given the actual dates & bikes (same day) 
    month_cols = [col for col in full_df.columns if col.endswith("Mon")]
    weekday_cols = [col for col in full_df.columns if col.endswith("Weekday")]

    count = 0
    instances_of_different_days = [];
    for i, row in feature_vector_df.iterrows():
        if len(set(row[month_cols].values)) > 1:
            print(count+1, end="\r")
            count = count + 1
            instances_of_different_days.append(list(row[month_cols].values))
    instances_of_different_days
    
    #Creating Month and Weekday columns
    feature_vector_df['Day_of_Month'] = feature_vector_df[month_cols[0]]
    feature_vector_df['Day_of_Week'] = feature_vector_df[weekday_cols[0]]
    
    #Dropping redundant columns
    feature_vector_df.drop(month_cols+weekday_cols, axis=1, inplace=True)
    feature_vector_df.drop('Vehicle_Type', axis=1, inplace=True)
    
    #Variable Datatypes
    numeric_cols = []
    object_cols = []
    time_cols = []
    for k, v in feature_vector_df.dtypes.items():
        if (v != object):
            if (k != "Time_Pic_Arr"):
                numeric_cols.append(k)
        elif k.endswith("Time"):
            time_cols.append(k)
        else:
            object_cols.append(k)
        
    #Convert an object to numeric (encoding)
    le = LabelEncoder()
    le.fit(feature_vector_df['Personal_Business'])
    feature_vector_df['Personal_Business'] = le.transform(feature_vector_df['Personal_Business'])
    feature_vector_df['Personal_Business'][:2]

    #Feature Selection
    features = numeric_cols + ['Personal_Business']
    predict_vector = feature_vector_df[features]
    
    # ------------------------------------------------------------------------

    return predict_vector

def load_model(path_to_model:str):
    """Adapter function to load our pretrained model into memory.

    Parameters
    ----------
    path_to_model : str
        The relative path to the model weights/schema to load.
        Note that unless another file format is used, this needs to be a
        .pkl file.

    Returns
    -------
    <class: sklearn.estimator>
        The pretrained model loaded into memory.

    """
    return pickle.load(open(path_to_model, 'rb'))

def make_prediction(data, model):
    """Prepare request data for model prediciton.

    Parameters
    ----------
    data : str
        The data payload received within POST requests sent to our API.
    model : <class: sklearn.estimator>
        An sklearn model object.

    Returns
    -------
    list
        A 1-D python list containing the model prediction.

    """
    # Data preprocessing.
    prep_data = _preprocess_data(data)
    # Perform prediction with model and preprocessed data.
    prediction = model.predict(prep_data)
    # Format as list for output standerdisation.
    return prediction[0].tolist()

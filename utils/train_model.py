"""
    Simple file to create a Sklearn model for deployment in our API

    Author: Explore Data Science Academy

    Description: This script is responsible for training a simple linear
    regression model which is used within the API for initial demonstration
    purposes.

"""

# Dependencies
 #%matplotlib notebook
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

# Fetch training data and preprocess for modeling
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")

new = train.drop(['Arrival at Destination - Day of Month',
                  'Arrival at Destination - Weekday (Mo = 1)',
                  'Arrival at Destination - Time', 'Distance (KM)'], 
                 axis=1)
y = np.array(new['Time from Pickup to Arrival']).reshape(-1, 1)
df = pd.concat([new,test])
df_1 = df.fillna(1)

df_2 = df.drop(['Order No', 'User Id', 'Vehicle Type', 'Rider Id','Placement - Weekday (Mo = 1)', 'Confirmation - Day of Month', 'Confirmation - Weekday (Mo = 1)', 'Arrival at Pickup - Day of Month', 'Arrival at Pickup - Weekday (Mo = 1)', 'Pickup - Day of Month','Pickup - Weekday (Mo = 1)', 'Placement - Time', 'Confirmation - Time', 'Arrival at Pickup - Time', 'Pickup - Time'], axis = 1)
df_2 = df_2.fillna(1)
df_2 = pd.get_dummies(df_2, drop_first=True)
X = df_2[:len(train)]
Y = df_2[len(train):]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Fit model
regressor = LinearRegression()
print ("Training Model...")
regressor.fit(X_train, y_train)
pred = regressor.predict(X_test)


def rmse(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

rmse(y_test, pred)

y_pred = regressor.predict(Y)
test = test.fillna(0)

test_1 = test[['Order No']]
test_1['Time from Pickup to Arrival'] = y_pred

# Pickle model for use within our API
save_path = '../trained-models/sendy_simple_lm_regression.pkl'
print (f"Training completed. Saving model to: {save_path}")
pickle.dump(regressor, open(save_path,'wb'))
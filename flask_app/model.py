"""
    Simple file to create a Sklearn model for deployment in our API
    WIP
"""

# Dependencies
import numpy as np
import pandas as pd
import pickle
import requests
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Fetch training data and preprocess for modeling
df = pd.read_csv("https://raw.githubusercontent.com/vyashemang/flask-salary-predictor/master/Salary_Data.csv")

X = df.iloc[:,:-1].values
y = df.iloc[:,-1:].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,
                                                    random_state = 42)

# Fit model
lm_regression = LinearRegression(normalize=True)
lm_regression.fit(X_train, y_train)
orig_pred = lm_regression.predict([[2.2]])

# Pickle model for use in API
pickle.dump(lm_regression, open('assets/trained-models/lm_regression_model.pkl','wb'))

# Restore model for testing
rest_lm_model = pickle.load(open('assets/trained-models/lm_regression_model.pkl','rb'))
new_pred = rest_lm_model.predict([[2.2]])

orig_pred == new_pred

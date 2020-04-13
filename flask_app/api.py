"""

    Simple Flask-based API for Model Serving.

    Author: Explore Data Science Academy.
    Note: Plase follow the instructions provided within the README.md file
    located within this directory for guidance on how to setup this minimal
    Flask Webserver to serve your developed models within a simple API.

"""

# API Dependencies
import pickle
import json
import numpy as np
from model import load_model, make_prediction
from flask import Flask, request, jsonify

# Application definition
app = Flask(__name__)

# Load our model into memory.
# Please update this path to reflect your own trained model.
static_model = load_model(path_to_model='assets/trained-models/lm_regression_model.pkl')

# Define the API interface.
# Here the 'model_prediction()' function will be called when a POST request
# is sent to our interface located at http:{EC2-IP-public-address}:5000/api_v0.1
@app.route('/api_v0.1', methods=['POST'])
def model_prediction():
    # We retrieve the data payload of the POST request
    data = request.get_json(force=True)
    # We then preprocess our data, and use our pretrained model to make a
    # prediction.
    output = make_prediction(data, static_model)
    # We finally package this prediction as a JSON object to deliver a valid
    # response with our API.
    return jsonify(output)

# Configure Server Startup properties.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

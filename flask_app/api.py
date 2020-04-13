"""

    Simple Flask-based API for Model Serving.

    !! WIP !!

    Author: Explore Data Science Academy

"""

# API Dependencies
import pickle
import numpy as np
from flask import Flask, request, jsonify

# Application definition
app = Flask(__name__)

# Load our model
static_model = pickle.load(open('assets/trained-models/lm_regression_model.pkl','rb'))

# Define API Routes
@app.route('/api', methods=['POST'])
def model_prediction():
    data = request.get_json(force=True)
    prediction = static_model.predict([[np.array(data['exp'])]])
    print (prediction)
    output = prediction[0].tolist()
    return jsonify(output)

# Configure Server Startup properties
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

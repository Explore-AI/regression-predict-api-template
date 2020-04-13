"""

    Simple Script for using the POST action to test our API

"""

import requests

url = 'http://127.0.0.1:5000/api_v0.1'
r = requests.post(url, json={"exp":2.2,})
print(r.json())

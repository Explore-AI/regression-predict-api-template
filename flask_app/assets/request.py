"""

    Simple Script for using the POST action to test our API

    WIP

"""

import requests

url = 'http://127.0.0.1:5000/api'
r = requests.post(url, json={'exp':2.2,})
print(r.json())

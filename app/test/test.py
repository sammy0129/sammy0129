import json

import requests


response = requests.post(url='http://localhost:8000/api/v1/admin/user/login', json={'username':'sammy123', 'password': 'sammy123'})

print(response.headers)
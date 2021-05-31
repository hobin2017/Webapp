"""
Aims: adding additional information in HTTP headers.
It is given in P12.
"""
import requests

headers3 = {'user-agent': 'my-app/0.0.1'}
resp3 = requests.get('http://localhost:5000/test3/', headers=headers3)
print(resp3.text)

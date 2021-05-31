"""
This request is equivalent to visiting the link:  http://localhost:5000/test2/?key1=value1&key2=value2&key2=value3
the url contains parameters!
It is given in P9.
"""
import requests

payload2 = {'key1': 'value1', 'key2': ['value2', 'value3']}
resp2 = requests.get('http://localhost:5000/test2/', params=payload2)
print(resp2.url) # http://localhost:5000/test2/?key1=value1&key2=value2&key2=value3
print(resp2.text)


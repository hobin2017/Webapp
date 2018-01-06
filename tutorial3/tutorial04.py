"""
Aims: sending data with requests.post() function;
It is given in P12
"""
import requests
import json

# sending data that is form-encoded which is like HTML form;
payload4_1 = {'key1': 'value1', 'key2': 'value2'}
resp4_1 = requests.post('http://localhost:5000/test4_1/', data=payload4_1)
print(resp4_1.text)

# sending data that is form-encoded which is like HTML form;
payload4_2 = (('key1', 'value1'), ('key1', 'value2')) # Compared with case 1, these two key are the same.
resp4_2 = requests.post('http://localhost:5000/test4_2/', data=payload4_2)
print(resp4_2.text)

# sending data that is JSON-Encoded POST data. In case3, it is serializing the data by ourselves.
data4_3 = {'key1': 'value1', 'key2': 'value2'}
payload4_3 = json.dumps(data4_3) # serializing the dictionary into string.
headers4_3 = {'content-type': 'application/json'} # the Flask.request.get_json() requires doing so.
resp4_3 = requests.post('http://localhost:5000/test4_3/', data=payload4_3, headers=headers4_3)
print(resp4_3.text)

# sending data that is JSON-Encoded POST data. In case4, it is serializing the data automatically.
payload4_4 = {'key1': 'value1', 'key2': ['value2', 'value3']}
resp4_4 = requests.post('http://localhost:5000/test4_4/', json=payload4_4)
# Note: the json parameter is ignored if either data or files parameter is passed.
print(resp4_4.text)


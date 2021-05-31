"""
Aims: uploading file with requests.post() function;
It is strongly recommended that you open files in binary mode;
Another reason why the mode of open() is 'rb', is that the file is picture;
Currently, it dose not support posting large file. However, requests-toolbelt supports doing so.
It is given in P13.
"""
import requests

with open('./Images/tutorial5.jpg', 'rb') as f:
    binary_data = f.read()
    print('The data length of the original file is %s' % len(binary_data))
    files5_1 = {'file5_1': binary_data}
    resp5_1 = requests.post('http://localhost:5000/test5_1/', files=files5_1)
    print(resp5_1.text)


# you can set the filename, binary data, content_type and headers explicitly.
# Be careful of the order and they should consist of a tuple!
with open('./Images/tutorial5.jpg', 'rb') as f:
    binary_data = f.read()
    files5_2 = {'file5_2': ('tutorial5_2.jpg', binary_data, 'image/jpeg', {'Expires': '0'})}
    resp5_2 = requests.post('http://localhost:5000/test5_2/', files=files5_2)
    print(resp5_2.text)


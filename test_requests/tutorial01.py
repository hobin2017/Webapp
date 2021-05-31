"""
After the request, the return value is a Response object (requests.models.Response class).
the 'text' attribute returns a string that should be provided in the browser.
the 'content' attribute returns the binary data which is the same as the 'text' attribute.
the 'headers'attribute returns a dict-like object that contains the information given in the header section.
the 'json()' function returns a list that contains the data.
the 'url' attribute returns a string.
"""

import requests

resp1 = requests.get('http://localhost:5000/test1/')
'''In P18, the call of requests.get() includes two major things.
First, a Request object which will be sent off to a server to request resource, is constructed;
Second, a Response object is generated once we get a response back from the server.
Besides, the Response object contains all of the information returned by the server and also contains te Request object.
'''
print(resp1.text)
print(resp1.content)
print(resp1.headers)
# print(resp1.json()) # It will raise an error since the json data is None.
print(resp1.url) # The url might be different from the  url that you visit since you might be redirected to another url.


# You can also get access to the information of the Request object.
# print(resp1.request.text) # the request object does not have the 'text' attribute.
print(resp1.request.headers)
print(resp1.request.url)




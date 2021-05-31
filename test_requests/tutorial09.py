"""
Aim: using PreparedRequest object and send() to sent the request
Procedure: the requests package firstly constructs a Request object and then turns it to the PreparedRequest.
The PreparedRequest object contains the binary data that will be sent to the server.
P.S.:
the Request object contains those attributes you do not always change;
the PreparedRequest contains those attributes you might change every time;
It is given in P19.
"""
import requests

sess9 = requests.Session()
req9 = requests.Request(method='GET', url='http://localhost:5000/test9')

# the original one
prepped_req9_1 = req9.prepare()  # The first way to prepare the request
resp9_1 = sess9.send(prepped_req9_1)
print(resp9_1.text)


# you change the information of request by using the attribute of request.Request or the attribute of PrepareRequest.
req9.headers = {'key1': 'value1'}
req9.data = 'Hello world!' # The length is 12 which wil be relate to  the 'Content-Length' header.
prepped_req9_2 = sess9.prepare_request(req9)  # The second way, the session-level attribute may take effects in this way
prepped_req9_2.headers['key1'] = 'value2'
prepped_req9_2.body = 'Seriously. send exactly these bytes.'
resp9_2 = sess9.send(prepped_req9_2)
# The data received by server is not complete since the 'Content-Length' header is set to 12 in the preparation.
print(resp9_2.text)

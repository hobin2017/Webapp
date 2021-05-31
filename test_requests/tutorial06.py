"""
Aims: using the history attribute of the Response objects to track redirection;
The history property will return a list of Response objects which is sorted from the oldest to the most recent response;
The redirection actually is another HTTP GET;
It is given in P16.
"""
import requests

resp6_1 = requests.get('http://localhost:5000/test6_1/')
print(resp6_1.url)
print(resp6_1.status_code)
print(resp6_1.history)
print(resp6_1.text)

resp6_2 = requests.get('http://localhost:5000/test6_2/', allow_redirects=False)
print(resp6_2.url)
print(resp6_2.status_code)
print(resp6_2.history) # Since the redirection is abandoned, the list is empty.
print(resp6_2.text)


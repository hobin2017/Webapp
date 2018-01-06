"""
Aim: to avoid that your program might hang indefinitely;
The timeout attribute is not a time limit on the entire response download;
If no bytes have been received on the underlying socket for timeout seconds, the requests do the time out;
It is given in P16-P17.
"""
import requests

resp7_1 = requests.get('http://localhost:5000/test7/', timeout=0.005) # the unit is second
print(resp7_1.text)


try:
    resp7_2 = requests.get('http://localhost:5000/test7/', timeout=0.00001)
    print(resp7_2.text)

except requests.Timeout:
    # The error type is given in P17.
    print('There is an error since you require a tiny time for server')



"""
Aims: using the session object in client;
The session object allows you to store certain parameters and cookies for requests;
The session object can make many requests and each request is made by using urllib3's connection pooling;
The method-level parameters override session parameters which is shown in resp8_2;
Session data will stored on the server temporarily and be encrypted (Flask tutorial1);
It is given in P17.
"""
import requests
# session8 = requests.Session()

# the session is closed as soon as the with block is exited, even if unhandled exceptions occurred.


with requests.Session() as session8:
    session8.auth = ('hobin', '123456')
    session8.headers.update({'key1': 'value1'})
    resp8_1 = session8.get('http://localhost:5000/test8_1/')
    print(resp8_1.text)

    # Be careful that the method-level parameters override session parameters
    resp8_2 = session8.get('http://localhost:5000/test8_2/', headers={'key1': 'value2'})
    print(resp8_2.text)

    # sending session-level cookies
    jar8 = requests.cookies.cookiejar_from_dict({'key3': 'value3'})  # The type is requests.cookies.RequestsCookieJar.
    session8.cookies = jar8
    resp8_3 = session8.get('http://localhost:5000/test8_3/')
    print(resp8_3.text)



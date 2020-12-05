
This tutorial comes from Requests Documentation(Release 2.18.4). 
The link is http://docs.python-requests.org/en/latest/user/quickstart/ 
# Summary:
1. the attribute of the Response obejct;
2. the url can contain parameters which is the same as passing data;
3. adding additional information in HTTP headers;
4. sending data with requests.post() function;
5. uploading file with requests.post() function;
6. using the history attribute of the Response objects to track redirection;
7. to avoid that your program might hang indefinitely;
8. using the session object in client;
9. using PreparedRequest object and send() to sent the request;
10. send data by http-body and query-string

# Notes
1. if the server part in the url is not ip, the DNS query is executed at each http-request. 061220


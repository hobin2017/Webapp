"""
   aim: send json in http-body with get method
   If use query string to send json data, one problem is the maximum length of the url. Sending json in the http-body
does not have this problem. Also, it is not convenient to construct a dictionary or a list in query string.
"""

import requests

__url = 'http://127.0.0.1:8000/service/jenkins_build/update'
__body = {
    'param1': [1, 2, 3],
    'param2': {'1': 1, '2': 2},
}
__qry = {'job_name': 'jenkins_job', 'build_status': '-1', 'msg4print': "success build"}
resp = requests.get(__url, params=__qry, json=__body)
print(resp.text)


"""
The first app of flask
"""
from flask import Flask
app = Flask(__name__) # Flask constructor takes the name of current module (__name__) as argument.


@app.route('/') # app.route(rule, options)
def hello_world():
    return 'Hello world'

if __name__ =='__main__':
    # app.run(host, port, debug, options)
    # host: Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally.
    # port: Defaults to 5000
    # debug: If the application should be restarted manually for each change in the code.
    # To avoid this inconvenience, enable debug support. The server will then reload itself if the code changes.
    # options: To be forwarded to underlying Werkzeug server.
    app.run('172.16.1.71', debug=True)


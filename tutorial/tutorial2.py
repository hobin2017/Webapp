"""
Modern web frameworks use the routing technique to help a user remember application URLs.
It is useful to access the desired page directly without having to navigate from the home page.
"""
from flask import Flask
app = Flask(__name__)

#@app.route('/hello') # the first way to bind the url with a function.
def hello_world():
    return 'Hello world'


if __name__ =='__main__':
    app.add_url_rule('/hello/', view_func=hello_world) # the second way to bind the url with a function.
    app.run('127.0.0.1', debug=True)


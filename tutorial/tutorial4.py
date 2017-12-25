"""
The url_for() function is very useful for dynamically building a URL for a specific function.
It's first argument is the name of a function.
And then one or more keyword arguments(they correspond to the variable part of URL) needs to be specified.
"""
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/user/admin/')
def hello_admin():
   return 'Hello Admin'

@app.route('/user/guest/<guest>/')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>/')
def hello_user(name):
   if name =='admin':
       #print(type(url_for('hello_admin'))) # the data type of return value is string. At is time, the value is /admin/ .
       return redirect(url_for('hello_admin')) #Thus, the redirect function accepts a url as parameter.
   else:
       # the hello_guest function has one key argument, thus it needs to be specified.
       return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)

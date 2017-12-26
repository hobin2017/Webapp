"""
Unlike a Cookie, Session data is stored on the server temporarily.
Session is the time interval when a client logs into a server and logs out of it.
The Session data is encrypted therefore a key is required.
'flask.session' is also a dictionary object containing key-value pairs of session variables and associated values.
"""
from flask import Flask, redirect, url_for, session, request
app = Flask(__name__)

app.secret_key = 'AnyValue' # to encrypt the Session data

@app.route('/')
def index():
    if 'username' in session:
        username = session['username'] # reading the data from the server.
        return """Logged in as %s <br> 
               <a href = '/logout'>click here to log out</a>""" % username
    else:
        return """You are not logged in <br>
        <a href = '/login'>click here to log in</a>"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username'] # storing the data in the server.
        return redirect(url_for('index'))
    return '''
   <form action = "" method = "post">
      <p><input type = text name = username /></p>
      <p><input type = submit value = Login /></p>
   </form>
   ''' # clicking on the button will visit the '/login' 

@app.route('/logout')
def logout():
    session.pop('username', None) # deleting the data on the server
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


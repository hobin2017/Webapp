"""
The redirect() function returns a response object;
The parameters of redirect are location, statuscode(default is 302) and response;
Multiple choices 300; Moved permanently 301; Found 302; User proxy 305; Reserved 306; Temporary redirect 307;
The abort() function has to do with error.
Bad Request 400; Unauthenticated 401; Forbidden 403; Not Found 404; Not Acceptable 406;
"""
from flask import Flask, redirect, url_for, render_template, request, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login(tutorial10).html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['name'] == "admin":
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))


@app.route('/success/')
def success():
    return 'logged in successfully'


if __name__ == '__main__':
    app.run(debug=True)

"""
A cookie is stored on a client’s computer in the form of a text file.
A cookie also stores its expiry time, path and domain name of the ste.
request.cookie is a dictionary object.
"""
from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello(tutorial8).html")

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        resp = make_response(render_template('readcookie(tutorial8).html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome %s </h1>' % name

if __name__ == '__main__':
    app.run(debug=True)

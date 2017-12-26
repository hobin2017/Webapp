"""
By default, the Flask route responds to the GET requests.
step1: creating the html and it is better to save it in the 'templates' directory(tutorial 6);
step2: start running this server;
step3: opening this html file via browser;
step4: entering the data and clicking the button;
"""
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/login/success/<name>/')
def success(name):
    return 'welcome %s' % name

@app.route('/login_division/', methods=['POST', 'GET'])
def login_division():
    if request.method == 'POST':
        # request.form is dictionary object containing a list of pairs of form parameter and its corresponding value.
        user = request.form['name'] # the parameter corresponds to the form element of the first form!
        return redirect(url_for('success', name=user))
    elif request.method == 'GET': # What if you enter the link directly?
        # the GET still can pass data, which is like POST!.
        user = request.args.get('name') # the parameter corresponds to the form element of the second form!
        return redirect(url_for('success', name=user))

# The below binding utilizes the advantage of tutorial6
from flask import render_template
@app.route('/login/')
def login():
    return render_template('login(tutorial5).html')

if __name__ == '__main__':
    app.run(debug=True)


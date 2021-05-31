"""
It is possible to return the value in the form of HTML.
Flask will try to find the HTML file in the 'templates' folder;
The 'templates' folder should go with this python script in the same folder;
by using render_template(), the Jinga2 template engine will turn the initial HTML into the final HTML;
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/')
def hello_world():
    return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/hello/<user>/')
def hello_name(user):
    # the parameter 'param1' corresponds to {{ param1 }} in hello(tutorial6).html;
    return render_template('hello(tutorial6).html', param1=user)


if __name__ == '__main__':
    app.run(debug=True)

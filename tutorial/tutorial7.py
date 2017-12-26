"""
Flask will try to find the JS and CSS file in the 'static' folder;
The 'static' folder should go with this python script in the same folder;
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello(tutorial7).html")

if __name__ == '__main__':
    app.run(debug=True)



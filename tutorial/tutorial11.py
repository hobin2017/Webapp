"""
Each uploaded file is first saved in a temporary location on the server, before it is actually saved to its ultimate location.
It is recommended to obtain a secure version of the file name by using the secure_filename() function
"""
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/upload/')
def upload():
    return render_template('upload(tutorial11).html')


@app.route('/uploader/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file1']  # It belongs to the werkzeug.datastructures.FileStorage class
        f.save(secure_filename(f.filename))
        return '''file uploaded successfully
        '''
    else:
        return ''


if __name__ == '__main__':
    app.run(debug=True)

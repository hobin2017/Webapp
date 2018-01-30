"""
This Flask application is used to verify the information provided by the Requests application;
Even if the type of return value is string, you can make it in json format, which enhances the data exchange for client;
"""
from flask import Flask, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'Any value'  # for test8


@app.route('/test1/', methods=['GET'])
def test1():
    return 'Hello world'


@app.route('/test2/', methods=['GET'])
def test2():
    return '%s, %s' % (request.args.get('key1'), request.args.getlist('key2'))


@app.route('/test3/', methods=['GET'])
def test3():
    return request.headers['user-agent']


@app.route('/test4_<num>/', methods=['POST'])
def test4(num):
    """
    request.get_json() will return none if the 'content-type' in header is not 'application/json'.
    If the 'content-type' in header does is not 'application/json', setting 'force=True' can return the data.
    """
    if num == '1':
        return '%s, %s' % (request.form['key1'], request.form['key2'])
    elif num == '2':
        return '%s' % request.form.getlist('key1')
    elif num == '3':
        return '%s' % request.get_json()
    elif num == '4':
        return '%s' % request.get_json()


@app.route('/test5_<num>/', methods=['POST'])
def test5(num):
    """
    requests.files object is a dict-like object;
    Each key in the requests.files object is the name from <input type='file' name=''> ;
    Each value in requests.files object is a file-like object; has 'save';
    """
    if num == '1':
        file5_1 = request.files['file5_1']
        data_received = file5_1.read()
        return '''The data length of the received file is %s; \nThis binary data is %s; \n
        ''' % (len(data_received), data_received)

    elif num == '2':
        file5_2 = request.files['file5_2']
        return "The headers of the received file are: %s" % file5_2.headers


@app.route('/test6_<num>/')
def test6(num):
    if num == '1':
        return redirect(url_for('test6', num=200))
    elif num == '2':
        return redirect(url_for('test6', num=200))
    elif num == '200':
        return 'You are redirected to a new page successfully.'


@app.route('/test7/')
def test7():
    return 'Your request get response within the timeout.'


@app.route('/test8_<num>/')
def test8(num):
    if num == '1':
        return '''The value of 'key1' is '%s'. Your username is %s and your password is %s.
        ''' % (request.headers['key1'], request.authorization['username'], request.authorization['password'])
    elif num == '2':
        return '''The value of 'key1' is '%s' since the value is replaced!. 
        ''' % request.headers['key1']
    elif num == '3':
        return '''Your cookies are %s
        ''' % request.cookies


@app.route('/test9/')
def test9():
    """The type of request.data is bytes. the default is utf-8"""
    return '''Your headers are: %s \nYour data are: %s
    ''' % (request.headers, request.data.decode())


if __name__ == '__main__':
    app.run(debug=True)

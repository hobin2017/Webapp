"""
It is possible to build a URL dynamically, by adding variable parts to the rule parameter.
This variable part is marked inside the < >.
It is passed as a keyword argument to the function with which the rule is associated.
"""
from flask import Flask
app = Flask(__name__)

@app.route('/<string:param1>/<param2>/<float:param3>/')
def test1(param1, param2, param3):
    # The data type of first variable part is string.
    # The data type of second variable part is string.
    # The data type of third variable part is float.
    return '''This is test 1 and your data are: %s, %s and %s
    '''%(param1, param2,param3)

@app.route('/<path:param1>/') # This variable parts accepts slashes '/' and hence it represents many urls.
def test2(param1):
    return '''This is test 2 and your data is: %s
    ''' %param1

def test3(param1, param2):
    return """This is test 3 and your data are: %s and %s
    """ %(param1, param2)

if __name__ =='__main__':
    app.add_url_rule('/<path:param1>/test3/<path:param2>/',view_func= test3) # the second way to bind the url with a function.
    app.run('127.0.0.1', debug=True)


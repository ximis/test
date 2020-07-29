from flask import Flask


'''
flask run --host=0.0.0.0

$ export FLASK_APP=hello.py
$ flask run

'''
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'



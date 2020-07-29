from flask import Flask
from prometheus_client import start_http_server, Summary, Gauge
import random
import time

'''
flask run --host=0.0.0.0

$ export FLASK_APP=hello.py
$ flask run
this test is failed
'''
app = Flask(__name__)
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
g = Gauge('my_inprogress_requests', 'Description of gauge')


@REQUEST_TIME.time()
@app.route('/')
def hello_world():

    return 'Hello, World!'


@app.route('/metrics')
def name():
    g.set(random.randint(1, 100))
    return g

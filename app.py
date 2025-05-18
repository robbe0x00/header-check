from flask import Flask
from flask import request

app = Flask(__name__)

global_head = {}

@app.route("/")
def hello_world():
    global global_head
    retval = str(global_head)
    global_head =  request.headers
    return retval

@app.route("/api/internal/<path:text>")
def internal(text):
    global global_head
    global_head = request.headers
    return "test"


import time
from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)

@app.route("/")
@cross_origin()
def say_hello():
    return {'time':time.time()}
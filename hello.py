#!python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Vive la Révolution d'Octobre!"

app.run(host='0.0.0.0', port=81)
#!/usr/bin/python3

from flask import Flask
import os

app = Flask(__name__)
@app.route('/', strict_slashes=False)

def hello():
    return 'Hello HBNB!'

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = os.getenv('FLASK_PORT', '5000')
    app.run(host=host, port=int(port))
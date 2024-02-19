#!/usr/bin/python3
"""Start Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)

def hello():
    """
    Routing to root, strict_slashes ensure
    the URL works when it ends both with or without the /
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hello_bnb():
    """
    Routing to root, strict_slashes ensure
    the URL works when it ends both with or without the /
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """Routing to C using Variables"""
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text):
    """Routing to python using Variables"""
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """Routing to numbers only"""
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_number_template(n):
    """Routing to numbers only"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

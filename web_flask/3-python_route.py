#!/usr/bin/python3

"""
a script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display c followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.roote('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace("_", " ")
    return f"Python {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

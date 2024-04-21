#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
	"""Display Hello HBNB! at / """
	return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""Display HBNB at /hbnb"""
	return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
	"""Displaye 'C' followed by the value of
	the text variable"""
	text = text.replace("_", " ")
	return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
	"""
	Displays 'Python' followed by the value of <text>
	"""
	return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
	"""Displays 'n is a number' if
	it's type is integer."""
	return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
	"""Displays an HTML page only if n is an integer."""
	return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
	"""
	Displays an HTML page only if n is an integer.
	H1 tag: Number: n is even|odd inside the tag BODY
	"""
	return render_template("6-number_odd_or_even.html", n=n)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000')

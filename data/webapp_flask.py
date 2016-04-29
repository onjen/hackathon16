# -*- coding: utf-8 -*-
from plotData import get_arrays
"""
    WebApp Viessmann
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Anlage3')
def anlage3():
    print("test")
    arrays = get_arrays('Anlage3.csv', 1)

    return jsonify(arrays=arrays)

if __name__ == '__main__':
    app.run('0.0.0.0')

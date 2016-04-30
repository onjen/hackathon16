# -*- coding: utf-8 -*-
from plotData import get_arrays
from weatherIntegration import getJSON
"""
    WebApp Viessmann
    ~~~~~~~~~~~~~~

    A simple application that shows how Flask and jQuery get along.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, jsonify, render_template, request
import json
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

@app.route('/Anlage1')
def anlage3():
    arrays = get_arrays('Anlage1.csv', 1)
    string = '[' + ', '.join(str(e) for e in arrays['json']) + ']'
    string = string.replace('\'', '\"')
    return string

@app.route('/Temperatures')
def temperatures():
    temperatures = getJSON()
    string = '[' + ', '.join(str(e) for e in temperatures) + ']'
    string = string.replace('\'', '\"')
    return string

@app.route('/Vorhersage')
def vorhersage():
    return render_template('vorhersage.html', title='vorhersage')

@app.route('/Verhalten')
def verhalten():
    return render_template('verhalten.html')

@app.route('/Konfigurator')
def konfigurator():
    return render_template('konfigurator.html')


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')

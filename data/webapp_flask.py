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
    print("test")
    rates = []
    arrays = get_arrays('Anlage1.csv', 1)
#    rates = json.dumps(arrays)

#    print(json.dumps(arrays))
#    outdoordata = json.loads(json.dumps(arrays['outdoor']), parse_float=float)
#    khwdata     = json.loads(arrays['d_kwh'], parse_float=float)
#    targetdata  = json.loads(arrays['d_target'], parse_float=float)

#    rates.append( rdata['outdoor'] )
#    rates.append( rdata['kwh'] )
#    rates.append( rdata['target'] )

#    return jsonify(arrays['json'])
    string = '[' + ', '.join(str(e) for e in arrays['json']) + ']'
    string = string.replace('\'', '\"')
#    return ', '.join(str(e) for e in arrays['json'])
    return string
#    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')

from math import sqrt
from flask import render_template, request, Response, jsonify
from json import dumps
from wsgi import app

__author__ = 'an'


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        a = request.form.get('a')
        b = request.form.get('b')
        c = request.form.get('c')

        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except (TypeError, ValueError):
            data = {
                'msg': 'Input Error'
            }
            return Response(response=dumps(data), status=422, mimetype='application/json')

        if a == 0 and b == 0 and c == 0:
            msg = 'Innumerable root'
        elif a == 0 and b == 0:
            msg = 'No root'
        elif a == 0 and c == 0:
            msg = 'x = 0'
        elif a == 0:
            x = -c / b
            msg = 'x = ' + str(x)
        else:
            d = b ** 2 - 4 * a * c
            if d > 0:
                x1 = (-b * sqrt(d)) / (2 * a)
                x2 = (-b * -sqrt(d)) / (2 * a)
                msg = 'x1 = {}<br>x2 = {}'.format(x1, x2)
            elif d == 0:
                x = -b / (2 * a)
                msg = 'x = ' + str(x)
            else:
                msg = 'No root'

        data = {
            'msg': msg
        }
        return jsonify(data)

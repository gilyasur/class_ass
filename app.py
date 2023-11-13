from flask import Flask, render_template, request, abort
from tools.col import *
from tools.numbers.simp import *
from tools.numbers.comp import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def math():
    return render_template('index.html')

@app.route('/check_pal', methods=['POST'])
def check_pal():
    try:
        number = int(request.json['number'])
        result = ispal(number)
        return {'result': result}
    except KeyError:
        return {'error': 'Invalid request data'}, 400

@app.route('/check_sum', methods=['POST'])
def check_sum():
    try:
        number1 = int(request.json['number1'])
        number2 = int(request.json['number2'])
        result = add_num(number1, number2)
        return {'result': result}
    except KeyError:
        return {'error': 'Invalid request data'}, 400

@app.route('/check_sub', methods=['POST'])
def check_sub():
    try:
        number1 = int(request.json['number1'])
        number2 = int(request.json['number2'])
        result = sub_num(number1, number2)
        return {'result': result}
    except KeyError:
        return {'error': 'Invalid request data'}, 400

@app.route('/calculate_sum_of_digits', methods=['POST'])
def calculate_sum_of_digits():
    try:
        number = int(request.json['number'])
        result = sumofdigits(number)
        return {'result': result}
    except KeyError:
        return {'error': 'Invalid request data'}, 400

if __name__ == '__main__':
    app.run(debug=True)

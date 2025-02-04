from flask import Flask, request, jsonify, Response
import requests
import math
import json
from flask_cors import CORS
from collections import OrderedDict


app = Flask(__name__)
CORS(app)


def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)

    total = sum(int(digit) ** power for digit in num_str)

    return total == num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    
    return True

def is_perfect(num):
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)

    return divisors_sum == num

def get_digit_sum(num):
    return sum(int(digit) for digit in str(abs(num)))

def get_properties(num):
    if num < 0:
        raise ValueError("Negative numbers are not supported.")
    
    properties = []

    if is_armstrong(num):
        properties.append("armstrong")

    if is_prime(num):
        properties.append("prime")

    if is_perfect(num):
        properties.append("perfect")

    if num % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    return properties

def get_fun_fact(num):
    if num < 0:
        return f"{num} is an interesting number, though its properties are not typically defined in mathematical contexts."

    try:
        response = requests.get(f"http://numbersapi.com/{num}/math")
        if response.status_code == 200:
            return response.text
        return f"{num} is an interesting number with various mathematical properties."
    
    except:
        return f"{num} is an interesting number with various mathematical properties."
    

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number', '')

    try:
        number = int(number_str)

        if number < 0:
            raise ValueError("Negative numbers are not supported.")
    
    except ValueError:
        error_response = OrderedDict([
            ("number", number_str),
            ("error", True)
        ])

        return Response(json.dumps(error_response), mimetype='application/json'), 400

    response = OrderedDict([
        ("number", number),
        ("is_prime", is_prime(number)),
        ("is_perfect", is_perfect(number)),
        ("properties", get_properties(number)),
        ("digit_sum", get_digit_sum(number)),
        ("fun_fact", get_fun_fact(number))
    ])
    
    json_response = json.dumps(response)
    return Response(json_response, mimetype='application/json'), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True)
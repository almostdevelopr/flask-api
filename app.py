from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/via_postman', methods=['POST'])
def math_operation_via_postman():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        if operation == 'add':
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'subtract':
            r = num1 + num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = num1 + num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            r = num1 + num2
            result = 'the quotient of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


if __name__ == "__main__":
    print("App is running..")
    app.run()

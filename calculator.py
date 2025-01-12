from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return 'Error: ' + str(e)

if __name__ == '__main__':
    app.run(debug=True)

# app.py
from flask import Flask, render_template, request
from script import calculate_result

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_data0 = request.form['input0']
    input_data1=request.form['input1']
    input_data2 = request.form['input2']
    result = calculate_result(str(input_data0+','+input_data1+','+input_data2))
    return render_template('result.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)

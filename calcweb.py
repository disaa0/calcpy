from flask import Flask, render_template, request
from operations import addNumbers

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = addNumbers(num1,num2)
        return render_template('index.html', result=result, num1=num1, num2=num2)

if __name__ == '__main__':
    app.run(debug=True)
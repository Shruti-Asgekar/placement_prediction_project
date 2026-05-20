from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    data = {
        "cgpa": float(request.form['cgpa']),
        "aptitude_score": int(request.form['aptitude_score']),
        "communication_skill": int(request.form['communication_skill'])
    }

    response = requests.post(
        'http://127.0.0.1:8000/predict',
        json=data
    )

    result = response.json()['prediction']

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
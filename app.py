import requests
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('access_key')
BASE_URL = 'http://data.fixer.io/api/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def conversion():
    base = request.form.get('base')
    target = request.form.get('target')
    amount = request.form.get('amount', type=float)

    url = f"{BASE_URL}latest?access_key={API_KEY}&symbols={target}"

    response = requests.get(url)
    data = response.json()

    rate = data['rates'][target]
    converted_amount = amount * rate

    return render_template('results.html', base=base, target=target, amount=amount, rate=rate, converted_amount=converted_amount)

if __name__ == '__main__':
    app.run(debug=True)
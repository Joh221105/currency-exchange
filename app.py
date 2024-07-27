import requests
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
import os
from currencies import currencies

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv('access_key')
BASE_URL = 'http://data.fixer.io/api/'

@app.route('/')
def home():
    return render_template('index.html', currencies = currencies)

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

    return render_template('results.html', base=base, target=target, amount=amount, rate=round(rate,2), converted_amount=round(converted_amount,2))

if __name__ == '__main__':
    app.run(debug=True)
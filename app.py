import requests
from flask import Flask, render_template
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)

URL = 'http://data.fixer.io/api/'
API_KEY = os.getenv('access_key')

@app.route('/')
def home():
    render_template('index.html')

@app.route('/convert', methods=['POST'])
def conversion():
    pass

if __name__ == '__main__':
    app.run()
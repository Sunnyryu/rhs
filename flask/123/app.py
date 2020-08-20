from flask import Flask, redirect, render_template, request
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/123')
def one():
    print(a)
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True, port="2222")
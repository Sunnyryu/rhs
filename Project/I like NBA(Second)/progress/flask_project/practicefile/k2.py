import pandas as pd
import pymysql
from flask import Flask, request, render_template, redirect, url_for
from k import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', players = ex())

if __name__ =='__main__':
    app.run(debug=True)

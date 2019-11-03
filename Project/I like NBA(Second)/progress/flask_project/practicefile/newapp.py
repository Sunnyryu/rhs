import pandas as pd
import pymysql
from flask import Flask, request, render_template, redirect, url_for
from view import *

app = Flask(__name__)

@app.route('/view')
def index():
    return render_template('a.html', context = get_context_data(self, **kwargs))

if __name__ =='__main__':
    app.run(debug=True)

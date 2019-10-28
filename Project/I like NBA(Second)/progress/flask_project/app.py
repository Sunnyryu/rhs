import pandas as pd
import pymysql
from flask import Flask, request, render_template, redirect, url_for, jsonify
from player import *
from flask_paginate import Pagination, get_page_args
from playersearch import *


app = Flask(__name__)
app.debug = True
rows = playerData()


def get_rows(offset, per_page):
    return rows[offset: offset + per_page]

@app.route('/')
def index():
    page = int(request.args.get('page', 1))
    per_page = 20
    offset = (page - 1) * per_page
    total = len(rows)
    print(page)
    print(per_page)
    print(offset)
    pagination_rows = get_rows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('index.html',
                           rows=pagination_rows,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           #players = playerData(),
                           )

def get_searchrows(offset, per_page):
    return searchrows[offset: offset + per_page]

@app.route('/search', methods=['POST'])
def search():
    fullname = request.form['fullname']
    #print(fullname)
    searchrows = playerSearch(fullname)
    #print(searchrows)
    if searchrows :
        return jsonify(searchrows)
    else:
        return jsonify([])
    page = int(request.args.get('page', 1))
    per_page = 20
    offset = (page - 1) * per_page
    total = len(searchrows)
    #print(searchrows)
    pagination_searchrows = get_searchrows(offset=offset, per_page=per_page)
    print(pagination_searchrows)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    print(pagination)
    return render_template('search.html',
                            searchrows=pagination_searchrows,
                            page=page,
                            per_page=per_page,
                            pagination=pagination,
                            )




if __name__ =='__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)

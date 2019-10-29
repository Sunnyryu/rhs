import pandas as pd
import pymysql
from flask import Flask, request, render_template, redirect, url_for, jsonify
from player import playerData
from flask_paginate import Pagination, get_page_args
from playersearch import playerSearch
import playersearch
import json

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
    fullname = request.args.get('fullname') # get 방식 
    searchrows = playerSearch(fullname)
    return searchrows[offset: offset + per_page]

@app.route('/search', methods=['GET','POST'])
def search():
    fullname = request.args.get('fullname') #검색어 받아오기
    #fullname = request.args.get('fullname') get 방식
    #fullname = request.form['fullname'] post 방식
    #print(fullname)
    searchrows = playerSearch(fullname) # 쿼리 수행
    #print(rows)
    page = int(request.args.get('page', 1))
    per_page = 20
    offset = (page - 1) * per_page
    total = len(searchrows)
    print(page)
    print(per_page)
    print(offset)
    #print(searchrows)
    pagination_searchrows = get_searchrows(offset=offset, per_page=per_page)
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

from flask import Flask, request, render_template, redirect, url_for
from flask_paginate import Pagination, get_page_args
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
#app.template_folder = ''
users = list(range(300))
p1 = os.getenv("PASSWORD")
d1 = os.getenv("DB")
def playerData():
    connection = None
    rows = None
    #current_page = request.GET.page
    #items_per_page = 20
    #start_index = (current_page - 1) * items_per_page
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= p1,
                                 db=d1,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            with connection.cursor() as cursor:
                #total_items = "select count(no) from a"
                #total_pages = round(total_items / items_per_page)
                sql = "select no, id, firstname, lastname, fullname from a limit 0, 20;"
                cursor.execute(sql)
                rows = cursor.fetchall()
                print(rows)
    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
            print('close')
    return rows

def get_rows(offset=0, per_page=20):
    return rows[offset: offset + per_page]


@app.route('/')
def index():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(rows)
    print(total)
    pagination_rows = get_rows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('index3.html',
                           rows=pagination_rows,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


if __name__ == '__main__':
    app.run(debug=True)

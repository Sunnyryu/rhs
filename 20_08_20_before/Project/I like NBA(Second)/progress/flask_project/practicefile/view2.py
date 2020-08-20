from flask import Flask, request, render_template, redirect, url_for
from flask_paginate import Pagination, get_page_args
from player import *

app = Flask(__name__)
#app.template_folder = ''
# users = list(range(300))
rows = playerData()
print(len(rows))


def get_rows(offset=0, per_page=10):
    return rows[offset: offset + per_page]


@app.route('/')
def index():
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
    total = len(rows)
    pagination_rows = get_rows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('index4.html',
                           rows=pagination_rows,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


if __name__ == '__main__':
    app.run(debug=True)

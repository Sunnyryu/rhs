from flask import Flask, render_template, url_for, request, redirect, Blueprint, session, flash, send_file, Response
from io import StringIO
from daebakai import db
import pandas as pd
from flask_paginate import Pagination, get_page_args
import os
from daebakai.revise.database import Database
import datetime
from werkzeug.utils import secure_filename
import csv
revise = Blueprint('revise', __name__,url_prefix='/revise')


@revise.route("/")
def Index():
    #print(Database)
    rows = Database.IndexValueread()
    rows_list = []
    for row in rows:
        if row['title']:
            rows_list.append(row)
    def get_rows(offset, per_page):
        return rows_list[offset: offset + per_page]
    page = int(request.args.get('page',1))
    per_page = 12
    offset = (page -1) * per_page
    total = len(rows_list)
    pagination_rows = get_rows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework="bootstrap4")
    rows_vendor = Database.Vendor_read()
    rows_vendor_list = []
    for i in rows_vendor:
        if i['vendor']:
            rows_vendor_list.append(i['vendor'])

    return render_template('revise-index.html', rows_vendor=rows_vendor_list, rows=pagination_rows, page=page, per_page=per_page, pagination=pagination)

@revise.route("/product")
def Product_list():
    vendor = request.args.get('comment')
    rows = Database.ValueSearch(vendor)
    def get_rows(offset, per_page):
        return rows[offset: offset + per_page]
    page = int(request.args.get('page',1))
    per_page = 12
    offset = (page -1) * per_page
    total = len(rows)
    pagination_rows = get_rows(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework="bootstrap4")
    #print(rows)
    return render_template('revise-product_list.html',rows=pagination_rows, len_rows=len(rows), page=page, per_page=per_page, pagination=pagination)

@revise.route("/product/<handle>")
def Product_revise(handle):

    product_list = Database.HandleSearch(handle)
    return render_template('revise-product.html', product_list=product_list, product_list_value=len(product_list))

@revise.route("/product_update", methods=["POST"])
def Product_update():
    value_id = request.form.getlist('id')
    value_title = request.form.getlist('title')
    value_body_HTML = request.form.getlist('body_HTML')
    value_price = request.form.getlist('price')
    value_option1_value = request.form.getlist('option1_value')
    value_option2_value = request.form.getlist('option2_value')
    revise_times = request.form['revise_times']
    revise_last_time = request.form['revise_last_time']
    #print(type(revise_times))
    #print(type(revise_last_time))
    for num in range(len(value_id)):
        if num == 0:
            value_new_id = value_id[num].strip(' \r\n\t')
            value_new_title = value_title[num].strip(' \r\n\t')
            value_new_body_HTML = value_body_HTML[num]
            value_new_price = value_price[num].strip(' \r\n\t')
            value_new_option1_value = value_option1_value[num].strip(' \r\n\t')
            value_new_revise_times = int(revise_times)+ 1
            value_new_revise_last_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

            #value_new_option2_value = value_option2_value[num].strip(' \r\n\t')
            rows = Database.Update_table_main(value_new_id, value_new_title, value_new_body_HTML, value_new_price, value_new_option1_value, value_new_revise_times, value_new_revise_last_time)#value_new_option2_value)
        else:
            value_new_id = value_id[num].strip(' \r\n\t')
            value_new_price = value_price[num].strip(' \r\n\t')
            value_new_option1_value = value_option1_value[num].strip(' \r\n\t')
            value_new_revise_times = int(revise_times)+ 1
            value_new_revise_last_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    #    value_new_option2_value = value_option2_value[num].strip(' \r\n\t')
            rows = Database.Update_table_etc(value_new_id, value_new_price, value_new_option1_value, value_new_revise_times, value_new_revise_last_time)
    #print(make_csv)
    return redirect('/revise') 
@revise.route("/upload", methods=["GET","POST"])
def Upload():
    print(1)
    if request.method == 'POST':
        file_csv = request.files['file']
        print(file_csv)
        b = file_csv.save(f'./{secure_filename(file_csv.filename)}')
        #a = pd.read_csv(f'./{secure_filename(file_csv.filename)}')
        c = f'./{secure_filename(file_csv.filename)}'
        delete_csv = Database.Delete_value(c)
        print(delete_csv)
        insert_csv = Database.Insert_value(c)
        print(insert_csv)
        return redirect("/revise")
    else:
        return print(2)

@revise.route("/download", methods=["GET"])
def Download():
    vendor = request.args.get('vendor')
    make_csv = Database.Make_csv(vendor)
    file_name = f"../{make_csv}.csv"
    return send_file(file_name,
                     mimetype='text/csv',
                     attachment_filename='이름을 설정하시오.csv',
                     as_attachment=True,
                     cache_timeout=0)  

#@revise.route("/download", methods=["GET"])
#def Downloads():
#    vendor = request.args.get('vendor')
#    output_stream = StringIO()## dataframe을 저장할 IO stream 
#    result = Database.Make_csv2(vendor)
#    result.to_csv(output_stream)## 그 결과를 앞서 만든 IO stream에 저장
#    response = Response(
#        output_stream.getvalue(), 
#        mimetype='text/csv', 
#        content_type='application/octet-stream',
#    )
#    response.headers["Content-Disposition"] = "attachment; filename=name.csv"
#    return response 

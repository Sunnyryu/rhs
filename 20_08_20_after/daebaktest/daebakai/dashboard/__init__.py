# dashboard
from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash
from flask_paginate import Pagination, get_page_parameter
from daebakai import db 

dashboard = Blueprint('dashboard', __name__,url_prefix='/dashboard')
 

@dashboard.route("/", defaults={'page':1})
@dashboard.route("/<int:page>")
def Main(page):
    
    #현재 페이지
    currentpage = page
    #한페이지에 표시되는 리스트수
    pageperitem = 20
    
    
    pageoffset = pageperitem * (currentpage - 1)
    DATA = (pageperitem, pageoffset)
    cursor = db.get_db().cursor()

    cursor.execute("SELECT COUNT(*) AS CNT FROM `TDC-customers`")
    count = cursor.fetchone()
 
    pagination = Pagination(page=currentpage, per_page=pageperitem, total=count['CNT'], css_framework="bootstrap4")

    # 한페이지 리스트 수만큼 게시물 가져오기
    cursor.execute("SELECT id, LastName, FirstName, Email, TotalSpent, TotalOrders  FROM `TDC-customers` ORDER BY id DESC LIMIT %s OFFSET %s" %DATA)
    rows = cursor.fetchall()
    cursor.close()
    
    
    return render_template('dashboard-main.html', ROWS=rows , pagination=pagination )
    
    
 

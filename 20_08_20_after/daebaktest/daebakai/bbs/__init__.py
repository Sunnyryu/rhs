# bbs 
from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash
from flask_paginate import Pagination, get_page_parameter
from daebakai import bcrypt
from daebakai import db 
import pymysql
import html
import math

bbs = Blueprint('bbs', __name__,url_prefix='/bbs')
 
@bbs.route("/", defaults={'page': 1})
@bbs.route("/<int:page>")
def Main(page):
    
    #현재 페이지
    currentpage = page
    #한페이지에 표시되는 리스트수
    pageperitem = 10
    
    
    pageoffset = pageperitem * (currentpage - 1)
    DATA = (pageperitem, pageoffset)
    cursor = db.get_db().cursor()
    cursor.execute("SELECT COUNT(*) AS CNT FROM bbs")
    count = cursor.fetchone()
 
    pagination = Pagination(page=currentpage, per_page=pageperitem, total=count['CNT'], css_framework="bootstrap4")

    # 한페이지 리스트 수만큼 게시물 가져오기
    cursor.execute("SELECT bbs.id, bbs.title, user.name, bbs.date, bbs.count  FROM bbs LEFT JOIN user ON user.id = bbs.author_id ORDER BY bbs.id DESC LIMIT %s OFFSET %s" %DATA)
    rows = cursor.fetchall()
    cursor.close()
    
    
    return render_template('bbs-main.html', ROWS=rows , pagination=pagination )

@bbs.route("/view/<id>", methods=['GET'])
def View(id):
    #글내용보기
    cursor = db.get_db().cursor()

    cursor.execute("SELECT * FROM bbs INNER JOIN user ON user.id = bbs.author_id WHERE bbs.id = %s",str(id))
    row = cursor.fetchone()
    row['title'] = html.unescape(row['title'])
    row['content'] = html.unescape(row['content'])
    
    db.get_db().commit()

    #해당게시물에 대한 덧글 불러오기
    cursor.execute("SELECT * FROM comment LEFT JOIN user ON user.id = comment.author_id WHERE comment.parent_id = %s ORDER BY comment.id DESC ",str(id))
    rowcomments = cursor.fetchall()
    db.get_db().commit()
    
    return render_template('bbs-view.html', ROW = row, ROWCOMMENTS = rowcomments)


@bbs.route("/write", methods=['GET', 'POST'])
def Write():

    if request.method == 'POST':
        title = request.form['title'] 
        title = html.escape(title)
        content = request.form['content']
        content = html.escape(content)
        author_id = session['id']
        DATA = (title,content,author_id)

      
        # 삽입
        cursor = db.get_db().cursor() 
        
        
        cursor.execute("INSERT INTO bbs  (id, title, content, date, count,author_id)  VALUES (NULL, '%s','%s',CURRENT_TIMESTAMP,'0','%s')" %DATA)
        db.get_db().commit()
        
        flash("게시글을  추가하였습니다.")

        return redirect(url_for('bbs.Main') )
        


    return render_template('bbs-write.html')

@bbs.route("/write-comment", methods=['GET', 'POST'])
def Write_comment():

    if request.method == 'POST':
        content = request.form['content']
        content = html.escape(content)


        parent_id = request.form['parent_id']
        author_id = session['id']
        DATA = (content,parent_id,author_id)

     
        # 삽입
        cursor = db.get_db().cursor() 
        
        
        cursor.execute("INSERT INTO comment  (id, content, date,parent_id,author_id)  VALUES (NULL, '%s',CURRENT_TIMESTAMP,'%s','%s')" %DATA)
        db.get_db().commit()
        
      

        return redirect(url_for('bbs.View',id = parent_id))
        


    return  redirect(url_for('bbs.Main') )

@bbs.route("/update/<id>", methods=['GET','POST'])
def Update(id):
    if request.method == 'GET':

         #글내용보기
        cursor = db.get_db().cursor()

        cursor.execute("SELECT * FROM bbs INNER JOIN user ON user.id = bbs.author_id WHERE bbs.id = %s",str(id))
        row = cursor.fetchone()
        row['title'] = html.unescape(row['title'])
        row['content'] = html.unescape(row['content'])
        db.get_db().commit()
        return  render_template('bbs-update.html', ROW = row)
    
    if request.method == 'POST':
        title = request.form['title'] 
        title = html.escape(title)
        content = request.form['content']
        content = html.escape(content)
        ID = id
        DATA = (title,content,ID)

      
        # 수정
        cursor = db.get_db().cursor() 
        
        
        cursor.execute("UPDATE bbs SET title = '%s', content = '%s' WHERE id ='%s'" %DATA)
        db.get_db().commit()
        
        flash(title+" 게시글을  수정하였습니다.")

        return redirect(url_for('bbs.Main') )
                

@bbs.route("/delete/<id>", methods=['GET'])
def Delete(id):

      #삭제
    cursor = db.get_db().cursor()
    
    cursor.execute("DELETE FROM bbs WHERE id = %s",str(id))
    
    db.get_db().commit()

    flash("게시물을 삭제하였습니다.")
   
    return redirect( url_for('bbs.Main'))


    
    
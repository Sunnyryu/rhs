# estimatesheet
# -*- coding: utf-8 -*-
import os
from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash,make_response, current_app
from flask_paginate import Pagination, get_page_parameter
from werkzeug.utils import secure_filename
from daebakai import db 
import pdfkit
from datetime import date
import mimetypes
import urllib


estimatesheet = Blueprint('estimatesheet', __name__,url_prefix='/estimatesheet')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'gif', 'png'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def imagefileupload(name, savename, author_id):

    file = request.files[name]
    if file and allowed_file(file.filename):
        file.filename = savename+"_"+str(author_id)+".jpg"
        filename = secure_filename(file.filename)

        if os.path.isdir(current_app.config['UPLOAD_FOLDER']+"/"+str(author_id)) == False :
            os.mkdir(current_app.config['UPLOAD_FOLDER']+"/"+str(author_id))
           
        filename = os.path.join(current_app.config['UPLOAD_FOLDER']+"/"+str(author_id), filename)
        file.save(filename)
        flash(name+"업로드됨")


@estimatesheet.route("/<name>/<location>")
def Main(name,location):
    options = {'enable-local-file-access': None}
    rendered = render_template('estimatesheet-pdf.html', name=name, location=location )
    pdf = pdfkit.from_string(rendered, False, options=options)

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    
    return response




@estimatesheet.route("/estimatebusinessinfowrite", methods=['GET', 'POST'])
def BusinessInfoWrite():
    author_id = session['id']
    
  


    if request.method == 'POST':
        
        data = request.form.to_dict()
  
        del data['csrf_token']

        columns = '`id`,'+'`a_id`,'
        values = "NULL,"+"'"+str(author_id)+"',"
        columns += ', '.join("`"+str(x).replace('/','_')+"`" for x in data.keys())
        values += ', '.join("'"+str(x).replace('/','_')+"'" for x in data.values())

        flash(columns) 
        sql = "INSERT INTO %s (%s) VALUES (%s)  "%('`user-companyinfo`',columns, values)
        
        # DB 사용
        cursor = db.get_db().cursor() 
        cursor.execute(sql)
        db.get_db().commit()
       
      

   
        imagefileupload('imagelink','business',author_id)
        imagefileupload('accountlink','account',author_id)
        imagefileupload('stamp','stamp',author_id)
        
        return redirect(url_for('estimatesheet.root') )
        


    return render_template('estimatesheet-main.html')


@estimatesheet.route("/estimatewrite", methods=['GET', 'POST'])
def Write():
    author_id = session['id']
    if request.method == 'POST':
        
        data = request.form.to_dict()
  
        del data['csrf_token']

        columns = '`id`,'+'`a_id`,'
        values = "NULL,"+"'"+str(author_id)+"',"
        columns += ', '.join("`"+str(x).replace('/','_')+"`" for x in data.keys())
        values += ', '.join("'"+str(x).replace('/','_')+"'" for x in data.values())

        sql = "INSERT INTO %s (%s) VALUES (%s)"%('`estimatesheet`',columns, values)

  
        # DB 사용
        cursor = db.get_db().cursor() 
        
        
        cursor.execute(sql)
        db.get_db().commit()
       
      
        flash("저장하였습니다")

        return redirect(url_for('estimatesheet.root') )
        


    return render_template('estimatesheet-main.html')

@estimatesheet.route("/estimatelist/", defaults={'page':1})
@estimatesheet.route("/estimatelist/<int:page>")
def list(page):

    author_id = session['id']

    #현재 페이지
    currentpage = page
    #한페이지에 표시되는 리스트수
    pageperitem = 10

    pageoffset = pageperitem * (currentpage - 1)
    DATA = (author_id, pageperitem, pageoffset)
    cursor = db.get_db().cursor()
    cursor.execute("SELECT COUNT(*) AS CNT FROM `estimatesheet`")
    count = cursor.fetchone()
 
    pagination = Pagination(page=currentpage, per_page=pageperitem, total=count['CNT'], css_framework="bootstrap4")



    
    
    #글내용보기
    cursor = db.get_db().cursor()

   
    cursor.execute("SELECT * FROM `estimatesheet`  WHERE `a_id` = %s ORDER BY id DESC LIMIT %s OFFSET %s" %DATA )

    rows = cursor.fetchall()
    db.get_db().commit()

 
    
    return render_template('estimatesheet-list.html', ROWS = rows,  pagination=pagination)



@estimatesheet.route("/register-businessinfo")
def RegisterBusinessinfo():
    author_id = session['id']

    #글내용보기
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM `user-companyinfo`  WHERE `a_id` = %s ORDER BY `id` DESC",author_id)
    row = cursor.fetchone()
    db.get_db().commit()


    return render_template('estimatesheet-register-businessinfo.html', ROW = row)
    


@estimatesheet.route("/view/<id>", methods=['GET'])
def View(id):
    #글내용보기
    cursor = db.get_db().cursor()
    # cursor.execute("SELECT * FROM comment LEFT JOIN user ON user.id = comment.author_id WHERE comment.parent_id = %s ORDER BY comment.id DESC ",str(id))
    sql = "SELECT * FROM `estimatesheet` LEFT JOIN `user-companyinfo` ON `estimatesheet`.a_id = `user-companyinfo`.a_id  where `estimatesheet`.id = "+str(id)+" ORDER BY `user-companyinfo`.id DESC"
    cursor.execute(sql)
    row = cursor.fetchone()
    
    db.get_db().commit()
  
    
    return render_template('estimatesheet-view.html', ROW = row)




@estimatesheet.route("/print/<id>", methods=['GET','POST'])
def Print(id):

    if request.method == 'POST':
        data = request.form.to_dict()
        del data['csrf_token']
        
     

  #글내용보기
    cursor = db.get_db().cursor()
    # cursor.execute("SELECT * FROM comment LEFT JOIN user ON user.id = comment.author_id WHERE comment.parent_id = %s ORDER BY comment.id DESC ",str(id))
    sql = "SELECT * FROM `estimatesheet` LEFT JOIN `user-companyinfo` ON `estimatesheet`.a_id = `user-companyinfo`.a_id  where `estimatesheet`.id = "+str(id)+" ORDER BY `user-companyinfo`.id DESC"
    cursor.execute(sql)
    row = cursor.fetchone()
    
    db.get_db().commit()
  

    if data['inlineRadioOptions'] == 'option1':
        targetfile = 'estimatesheet-pdf-basic.html'
    if data['inlineRadioOptions'] == 'option2':
        targetfile = 'estimatesheet-pdf-simple.html'
    if data['inlineRadioOptions'] == 'option3':
        targetfile = 'estimatesheet-pdf-simple2.html'



 
    options = {'enable-local-file-access': None}
    rendered = render_template( targetfile, ROW = row, DATA = data )
    pdf = pdfkit.from_string(rendered, False, options=options)
    
    file_name = urllib.parse.quote( "견적서.pdf".encode('utf-8'))
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf; charset=utf-8'"
    response.headers["Content-Disposition"] = 'inline;  filename*=UTF-8\'\'%s' % file_name
    
    return response


@estimatesheet.route("/")
def root():

    return render_template('estimatesheet-main.html')
    




@estimatesheet.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'imagelink' not in request.files:
            flash('No file part')
            return RegisterBusinessinfo()
        file = request.files['imagelink']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return RegisterBusinessinfo()
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            flash(filename)
            return RegisterBusinessinfo()
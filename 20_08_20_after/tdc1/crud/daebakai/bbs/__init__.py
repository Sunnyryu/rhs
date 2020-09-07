# bbs 
from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash
from daebakai import bcrypt
from daebakai import db 
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
    lastpage = math.ceil(count['CNT'] / pageperitem)
   
    PAGE = { 
        'currentpage' : currentpage,
        'pageoffset': pageoffset,
        'lastpage' : lastpage,
        'totalitem' : count['CNT']

        }

    print( PAGE )
    cursor.execute("SELECT * FROM bbs ORDER BY id DESC LIMIT %s OFFSET %s" %DATA)
    rows = cursor.fetchall()
    cursor.close()
  
    
    return render_template('bbs-main.html', ROWS=rows , PAGEINFO=PAGE )

@bbs.route("/view/<id>", methods=['GET'])
def View(id):
    #글내용보기
    cursor = db.get_db().cursor()
    
    cursor.execute("SELECT * FROM bbs WHERE id = %s",str(id))
    row = cursor.fetchone()
    
    db.get_db().commit()

    
    return render_template('bbs-view.html', ROW = row)


@bbs.route("/write", methods=['GET', 'POST'])
def Write():

    if request.method == 'POST':
        title = request.form['title'] 
        content = request.form['content']
        author = session['name']
        DATA = (title,content,author)

        # 삽입
        cursor = db.get_db().cursor() 
        
        cursor.execute("INSERT INTO bbs  (id, title, content, author, date, count)  VALUES (NULL, '%s','%s','%s',CURRENT_TIMESTAMP,'0')" %DATA)
        db.get_db().commit()
        
        flash("게시글을  추가하였습니다.")

        print( title + content)
        return redirect(url_for('bbs.Main') )
        


    return render_template('bbs-write.html')

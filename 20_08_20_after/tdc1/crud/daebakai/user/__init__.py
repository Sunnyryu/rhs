# user
from flask import Flask , render_template, url_for, request, redirect, Blueprint,g, session, flash
from daebakai import bcrypt
from daebakai import db




user = Blueprint('user', __name__ ,url_prefix='/user')




@user.route("/main")
def Main():
           
           
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM user WHERE 1 ORDER BY id DESC")
    rows = cursor.fetchall()
    cursor.close()
    

    return render_template('user.html',ROWS=rows)
    

    
    
    

@user.route("/insert", methods=['POST'])
def Insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        DATA = (name,email,phone,pw_hash)

        # 삽입
        cursor = db.get_db().cursor() 
        
        cursor.execute("INSERT INTO user (id, name, email, phone, password) VALUES (NULL, '%s','%s','%s','%s')" %DATA)
        db.get_db().commit()
        flash("사용자 추가하였습니다.")
        if 'loggedin' in session:
            return redirect( url_for('user.Main') )
        else:
            return redirect( url_for('login.Main'))


@user.route("/update", methods=['POST'])
def Update():
    
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        DATA = ( name, email, phone,  id)
        # 수정
        cursor = db.get_db().cursor()  
        cursor.execute("UPDATE user SET name = '%s' , email = '%s', phone = '%s' WHERE id ='%s'" %DATA)
        db.get_db().commit()

        cursor.close()
        flash("사용자 업데이트되었습니다.")
        
   

    return redirect( url_for('user.Main'))

@user.route("/delete/<id>", methods=['GET'])
def Delete(id):
    #삭제
    cursor = db.get_db().cursor()
    
    cursor.execute("DELETE FROM user WHERE id = %s",str(id))
    
    db.get_db().commit()

    flash("사용자 삭제하였습니다.")
   
    return redirect( url_for('user.Main'))

# login 
from flask import Flask , render_template, url_for, request, redirect, Blueprint, session, flash
from daebakai import bcrypt

from daebakai import db 
login = Blueprint('login', __name__,url_prefix='/login')




@login.route("/")
def Main():
    return render_template('login-form.html')

@login.route('/login', methods=["POST"])
def Login():
    email = request.form['email']
    password = request.form['password']
    DATA = (email)
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM user WHERE email = '%s'" %DATA)
    account = cursor.fetchone()
    cursor.close()
    
    flash( account['name'] )
    if account and bcrypt.check_password_hash(account['password'], password) :
        
        session['loggedin'] = True
        session['id'] = account['id']
        session['name'] = account['name']
        
        flash('로그인 되었습니다.!')
        return redirect(url_for('user.Main') )
    else:
        flash('아이디 또는 패스워드가 잘못되었습니다.')
        return redirect(url_for('login.Main') )
    
    

    



@login.route('/logout')
def Logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('name', None)
    flash('로그아웃 되었습니다.')
    return redirect(url_for('login.Main'))
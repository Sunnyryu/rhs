# daebakai 설정
from flask import Flask , render_template, url_for, request, redirect, Blueprint, g
from flask_bcrypt import Bcrypt
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


db = MySQL(cursorclass=DictCursor)
bcrypt = Bcrypt()


def create_app():
        
    app = Flask(__name__)
    app.config['MYSQL_DATABASE_HOST'] = 'tusiworks.iptime.org'
    app.config['MYSQL_DATABASE_PORT'] = 3308
    app.config['MYSQL_DATABASE_DB'] = 'testdb'
    app.config['MYSQL_DATABASE_USER'] = 'test'
    app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
    app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'

    app.config['SECRET_KEY'] = 'thisissecret'

    db.init_app(app)
    bcrypt.init_app(app)


    from daebakai.home import home
    from daebakai.user import user
    from daebakai.login import login
    from daebakai.bbs import bbs
    from daebakai.revise import revise
    
    app.register_blueprint(login)
    app.register_blueprint(home)
    app.register_blueprint(user)
    app.register_blueprint(bbs)
    app.register_blueprint(revise)
    

    return app
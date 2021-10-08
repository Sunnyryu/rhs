# -*- coding: utf-8 -*-
# daebakai 설정
# -*- coding: utf-8 -*-
from flask import Flask , render_template, url_for, request, redirect, Blueprint, g
from flask_bcrypt import Bcrypt
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from flask_wtf.csrf import CSRFProtect
from flask_socketio import SocketIO



db = MySQL(cursorclass=DictCursor)
bcrypt = Bcrypt()
csrf = CSRFProtect()
socketio = SocketIO()
def create_app(debug=False):
    app = Flask(__name__)
    app.debug = True
    app.config['MYSQL_DATABASE_HOST'] = 'tusiworks.iptime.org'
    app.config['MYSQL_DATABASE_PORT'] = 3308
    app.config['MYSQL_DATABASE_DB'] = 'TDC'
    app.config['MYSQL_DATABASE_USER'] = 'test'
    app.config['MYSQL_DATABASE_PASSWORD'] = '1234'

    UPLOAD_FOLDER = '/flask_app/project/crud/daebakai/static/upload_image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SECRET_KEY'] = 'thisissecret'

    db.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)


    from daebakai.home import home
    from daebakai.user import user
    from daebakai.login import login
    from daebakai.bbs import bbs
    from daebakai.revise import revise
    from daebakai.ai_predict import ai_predict
    from daebakai.dashboard import dashboard
    from daebakai.estimatesheet import estimatesheet
    from daebakai.product import product
    from daebakai.blank import blank
    from daebakai.chat import chat
    from daebakai.minichat import minichat

    app.register_blueprint(login)
    app.register_blueprint(home)
    app.register_blueprint(user)
    app.register_blueprint(bbs)
    app.register_blueprint(revise)
    app.register_blueprint(ai_predict)
    app.register_blueprint(dashboard)
    app.register_blueprint(estimatesheet)
    app.register_blueprint(product)
    app.register_blueprint(blank)
    app.register_blueprint(chat)
    app.register_blueprint(minichat)
    socketio.init_app(app)
    return app

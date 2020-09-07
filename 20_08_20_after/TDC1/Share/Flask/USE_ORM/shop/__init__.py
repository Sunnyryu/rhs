from flask import Flask, Blueprint
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os 

load_dotenv(verbose=True)
secret_key = os.getenv("SECRET_KEY")
username = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")
db_name = os.getenv("DB_NAME")
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@localhost:3306/{db_name}'
    db_url = f'mysql://{username}:{password}@localhost:3306/{db_name}'
    db.init_app(app)
    # flask db migrate - 모델을 신규로 생성하거나 변경할때 사용
    # flask db upgrade - 변경된 내용을 적용할때 사용
    from shop import models
    migrate.init_app(app, db)  

    
    from shop.views import question, home, answer, auth, comment, vote
    app.register_blueprint(home.hm)
    app.register_blueprint(question.qa)
    app.register_blueprint(answer.ans)
    app.register_blueprint(auth.auth)
    app.register_blueprint(comment.cm)
    app.register_blueprint(vote.vt)
    from shop.filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app
    

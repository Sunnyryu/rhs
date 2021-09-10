import pymysql
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

db = None

try:
    host = os.getenv('HOST')
    user = os.getenv('USER')
    passwd = os.getenv('PASSWD')
    basicdb= os.getenv('DB')
    charset = os.getenv('CHARSET')
    db = pymysql.connect(
            host = host,
            user = user,
            passwd = passwd,
            db = basicdb,
            charset = charset,
        )
    if db:
        sql = '''
                CREATE TABLE tb_student (
                id int primary key auto_increment not null,
                name varchar(32),
                age int,
                address varchar(32)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        '''
        with db.cursor() as cursor:
            cursor.execute(sql)
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
        print('db 연결 닫기')

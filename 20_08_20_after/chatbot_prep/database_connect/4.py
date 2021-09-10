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
        # 데이터 수정 sql 정의
        id = 1  # 데이터 id (PK)
        sql = '''
            UPDATE tb_student set name="케이", age=36 where id=%d
            ''' % id
        with db.cursor() as cursor:
            cursor.execute(sql)
        db.commit()
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
        print('db 연결 닫기')

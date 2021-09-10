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
        students = [
            {'name': 'Kei', 'age': 36, 'address' : 'BUSAN'},
            {'name': 'Tony', 'age': 34, 'address': 'BUSAN'},
            {'name': 'Jaeyoo', 'age': 39, 'address': 'GWANGJU'},
            {'name': 'Grace', 'age': 28, 'address': 'SEOUL'},
            {'name': 'Jenny', 'age': 27, 'address': 'SEOUL'},
            ]

    # 데이터 db에 추가
        for s in students:
            with db.cursor() as cursor:
                sql = '''
                        insert tb_student(name, age, address) values("%s",%d,"%s")
                        ''' % (s['name'], s['age'], s['address'])
                cursor.execute(sql)
        db.commit() # 커밋

        # 30대 학생만 조회
        cond_age = 30
        with db.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = '''
            select * from tb_student where age > %d
            ''' % cond_age
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)

            # 이름 검색
            cond_name = 'Grace'
            with db.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = '''
                select * from tb_student where name="%s"
                ''' % cond_name
                cursor.execute(sql)
                result = cursor.fetchone()
                print(result['name'], result['age'])

            # pandas 데이터프레임으로 표현
            df = pd.DataFrame(results)
            print(df)
except Exception as e:
    print(e)
finally:
    if db is not None:
        db.close()
        print('db 연결 닫기')

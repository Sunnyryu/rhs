import pandas as pd
import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

p1 = os.getenv("PASSWORD")
d1 = os.getenv("DB")
def TS30():
    connection = None
    rows = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= p1,
                                 db=d1,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            with connection.cursor() as cursor:
                sql = "select fullname, TS30 from TS order by TS30 desc;"
                cursor.execute(sql)
                rows = cursor.fetchall()
    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return rows

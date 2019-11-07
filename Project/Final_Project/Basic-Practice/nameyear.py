import pandas as pd
import pymysql
from sqlalchemy import create_engine

# import cmaps

def Yearname(year2):
    connection = None
    year2row = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= 'acs0214',
                                 db='birthday',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            with connection.cursor() as cursor:
                 sql = '''
                 select
                     value
                 from
                     NewTable
                where
                    year like '%s';
                '''% year2
            cursor.execute(sql)
            year2row = cursor.fetchone()
            print(year2row)
    except Exception as e:
        print('->', e)
        year2row= None
    finally:
        if connection:
            connection.close()
    return year2row

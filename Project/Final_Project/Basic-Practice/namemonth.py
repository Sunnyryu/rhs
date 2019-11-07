import pandas as pd
import pymysql
from sqlalchemy import create_engine

# import cmaps

def Monthname(month):
    connection = None
    monthrow = None

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
                    NewTable2
                where
                    month like '%s';
                '''% month
            print(type(month))
            print(sql)
            cursor.execute(sql)
            monthrow = cursor.fetchone()


    except Exception as e:
        print('->', e)
        monthrow= None
    finally:
        if connection:
            connection.close()
    return monthrow

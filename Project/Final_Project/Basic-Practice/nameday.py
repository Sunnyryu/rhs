import pandas as pd
import pymysql
from sqlalchemy import create_engine

# import cmaps

def Dayname(day):
    connection = None
    dayrow = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= 'acs0214',
                                 db='birthday',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            cursor = connection.cursor()
            #with connection.cursor() as cursor:
            sql = '''
            select
                value
            from
                NewTable3
            where
                day like '%s';
            '''% day
            cursor.execute(sql)
            dayrow = cursor.fetchone()
    except Exception as e:
        print('->', e)
        dayrow= None
    finally:
        if connection:
            connection.close()
    return dayrow

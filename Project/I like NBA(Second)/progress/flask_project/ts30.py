import pandas as pd
import pymysql

def TS30():
    connection = None
    rows = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= 'acs0214',
                                 db='nbaplayerid',
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

import pandas as pd
import pymysql
from sqlalchemy import create_engine

def playerData():
    connection = None
    rows = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= 'acs0214',
                                 db='nbaplayerid',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

        cursor = connection.cursor()
        sql = "select no, id, firstname, lastname, fullname from a where no >= %s limit 10;"

        cursor.execute(sql, (no))
        rows = cursor.fetchall()
        print(rows)
    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
            print('close')
    return rows

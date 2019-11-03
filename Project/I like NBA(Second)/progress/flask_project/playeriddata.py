import pandas as pd
import pymysql
from sqlalchemy import create_engine

def playeridData(playerid):
    connection = None
    playeridrows = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= 'acs0214',
                                 db='nbaplayerid',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            with connection.cursor() as cursor:
                #total_items = "select count(no) from a"
                #total_pages = round(total_items / items_per_page)
                sql =  '''
                select
                    no, id, firstname, lastname, fullname
                from
                    a
                where id = '%s'
                order by
                no asc;
                '''% playerid
                cursor.execute(sql)
                playeridrows = cursor.fetchall()
                #print(playeridrows)
    except Exception as e:
        print('->', e)
        playeridrows= None
    finally:
        if connection:
            connection.close()
    return playeridrows

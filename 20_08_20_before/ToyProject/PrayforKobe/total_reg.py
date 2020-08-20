import pandas as pd
import pymysql
from sqlalchemy import create_engine

def Total_reg():
    connection = None
    total_rows = None
    #current_page = request.GET.page
    #items_per_page = 20
    #start_index = (current_page - 1) * items_per_page
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'nba',
                                 password= '1234',
                                 db='nbadb',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            with connection.cursor() as cursor:
                #total_items = "select count(no) from a"
                #total_pages = round(total_items / items_per_page)
                sql = "select GP, FG_PCT, FG3_PCT, FT_PCT, PTS, REB, AST, STL, BLK, TOV, PF from total_reg;"
                cursor.execute(sql)
                total_rows = cursor.fetchall()
    except Exception as e:
        print('->', e)
        total_rows = None
    finally:
        if connection:
            connection.close()
    return total_rows

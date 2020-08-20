import pandas as pd
import pymysql
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

p1 = os.getenv("PASSWORD")
d1 = os.getenv("DB")
def playerData():
    connection = None
    rows = None
    #current_page = request.GET.page
    #items_per_page = 20
    #start_index = (current_page - 1) * items_per_page
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= p1,
                                 db=d1,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            with connection.cursor() as cursor:
                #total_items = "select count(no) from a"
                #total_pages = round(total_items / items_per_page)
                sql = "select no, id, firstname, lastname, fullname from a order by no asc;"
                cursor.execute(sql)
                rows = cursor.fetchall()
                #print(rows)
    except Exception as e:
        print('->', e)
        rows= None
    finally:
        if connection:
            connection.close()
    return rows

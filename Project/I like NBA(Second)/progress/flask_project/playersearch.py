import pandas as pd
import pymysql
from sqlalchemy import create_engine

def playerSearch(fullname):
    connection = None
    searchrows = None
    #current_page = request.GET.page
    #items_per_page = 20
    #start_index = (current_page - 1) * items_per_page
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
                where fullname like '%%%s%%'
                order by
                no asc;
                '''% fullname
                cursor.execute(sql)
                searchrows = cursor.fetchall()
                #print(searchrows)
    except Exception as e:
        print('->', e)
        searchrows= None
    finally:
        if connection:
            connection.close()
    return searchrows

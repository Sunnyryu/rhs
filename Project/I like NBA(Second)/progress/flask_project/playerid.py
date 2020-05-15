import pymysql
from sqlalchemy import create_engine
import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib._cm_listed import cmaps as cmaps_listed
from matplotlib import colors
from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
from nba_api.stats.endpoints import shotchartdetail
# import cmaps
import os
from dotenv import load_dotenv
load_dotenv()

p1 = os.getenv("PASSWORD")
d1 = os.getenv("DB")
def playerId(playerid):
    connection = None
    playeridrows = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= p1,
                                 db=d1,
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            with connection.cursor() as cursor:
                sql =  '''
                select
                    no, id, firstname, lastname, fullname
                from
                    a
                where id like '%%%s%%'
                order by
                no asc;
                '''% playerid
                cursor.execute(sql)
                playeridrows = cursor.fetchall()
    except Exception as e:
        print('->', e)
        searchrows= None
    finally:
        if connection:
            connection.close()
    return playeridrows

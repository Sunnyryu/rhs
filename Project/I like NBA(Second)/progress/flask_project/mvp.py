import pandas as pd
import pymysql
from sqlalchemy import create_engine
from nba_api.stats.endpoints import leagueleaders

def PredMVP():
    start = leagueleaders.LeagueLeaders()
    startframe = start.get_data_frames()
    df = pd.DataFrame(columns=['no', 'fullname', 'predmvppoint'])
    for no in range(0, 403):
        fullname = startframe[0].PLAYER[no]
        predmvppoint =  round((int(startframe[0].PTS[no])+0.82*int(startframe[0].OREB[no])+0.76*int(startframe[0].DREB[no])+1.07*int(startframe[0].AST[no])+1.1*int(startframe[0].STL[no])
        +1.03*int(startframe[0].BLK[no])-0.7*int(startframe[0].FGA[no])+0.2*int(startframe[0].FG3A[no])-0.4*int(startframe[0].FTA[no])-0.9*int(startframe[0].TOV[no])-0.35*int(startframe[0].PF[no]))/float(startframe[0].GP[no]),2)
        df = df.append(pd.DataFrame([[no, fullname, predmvppoint]], columns=['no', 'fullname', 'predmvppoint']), ignore_index= True)
    df.set_index('no', inplace=True)
    #print(df)
    engine = create_engine("mysql+mysqldb://root:"+"acs0214"+"@localhost/nbaplayerid", encoding='utf-8')
    conn = engine.connect()
    df.to_sql(name='mvp', con=engine, if_exists='replace')
    connection = None
    predrows = None
    try:
        connection = pymysql.connect(host='localhost',
                                 user= 'root',
                                 password= 'acs0214',
                                 db='nbaplayerid',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
        if connection :
            with connection.cursor() as cursor:
                sql = "select fullname, predmvppoint from mvp order by predmvppoint desc;"
                cursor.execute(sql)
                predrows = cursor.fetchall()
    except Exception as e:
        print('->', e)
        predrows= None
    finally:
        if connection:
            connection.close()
    return predrows

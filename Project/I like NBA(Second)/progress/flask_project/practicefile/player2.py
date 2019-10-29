import pandas as pd
import pymysql
from sqlalchemy import create_engine


def playerData():
	try:
		conn = pymysql.connect(
		host='localhost',
		user='root',
		password='acs0214',
		db='nbaplayerid',
		charset='utf8',
		cursorclass=pymysql.cursors.DictCursor
		)
		return conn
	except:
		print("DB connection Error")

		conn = playerData()
		curs = conn.cursor()

		per_page = 20
		#: 전체 페이지 구하기
		total_cnt = "select count(no) from a;"
		float(total_cnt)
		print(total_cnt2)
		total_page = round(total_cnt2 / per_page)

		for page in range(total_page) :
			query = "select id, firstname, lastname, fullname from a Limit %s offset %s;"
			curs.execute(query, (per_page, page * per_page))
		rows = curs.fetchall()

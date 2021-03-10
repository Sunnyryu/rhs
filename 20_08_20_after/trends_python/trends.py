from pytrends.request import TrendReq
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR
import pymysql
from dotenv import load_dotenv
import os
load_dotenv()
import datetime

# use sqlalchemy & pymysql for database connect
id = os.getenv('USER_NAME')
password = os.getenv("PASSWORD")
host = os.getenv("HOST_NAME")
port = os.getenv('PORT_NUMBER')
db = os.getenv("DB")
charset = os.getenv("CHARSET_NAME")
connect_inform = f'mysql+pymysql://{id}:{password}@{host}:{port}/{db}?{charset}'
print(connect_inform)
engine= create_engine(connect_inform, encoding="UTF-8")
conn = engine.connect()
print(conn)


test_list = []
# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq(hl='en-US', tz=360, timeout=(10,40))

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['bts', 'blackpink','maroon 5','beatles'], cat=0, timeframe='today 3-m', geo='US')

# time setting for db insert
make_time = datetime.datetime.today()
make_time = make_time.strftime("%Y%m%d%H%M%S")
db_make_time = make_time[2:12]

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
interest_df = pd.DataFrame(interest_over_time_df)
interest_df.to_sql(name=f'iotd_{db_make_time}', con=engine, if_exists='append')
#print(interest_over_time_df.head())

# Interest by Region
interest_by_region_df = pytrend.interest_by_region()
interest_by_region_df.reset_index().to_sql(name=f'ibrd_{db_make_time}', con=engine, if_exists='append')
#print(interest_by_region_df.head())

# Related Queries, returns a dictionary of DataFrames
related_queries_dict = pytrend.related_queries()
#print(related_queries_dict)
related_queries_df = pd.DataFrame(related_queries_dict)
#print(related_queries_df)
for query_name, query_value_df in related_queries_df.items():
    try:
        query_value_df[0].to_sql(name=f'{query_name}_top_{db_make_time}', con=engine, if_exists='append')
        query_value_df[1].to_sql(name=f'{query_name}_rising_{db_make_time}', con=engine, if_exists='append')
    except AttributeError as error:
        pass

#related_queries_df.to_sql(name=f'rqd_{db_make_time}', con=engine, if_exists='append', dtype={'None':VARCHAR(5)})
#print(related_queries_dict)

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()
trendingsearches_df = pd.DataFrame(trending_searches_df)
trendingsearches_df.to_sql(name=f'trsd_{db_make_time}', con=engine, if_exists='append')
#print(trending_searches_df.head())

# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
todaysearches_df = pd.DataFrame(today_searches_df)
todaysearches_df.to_sql(name=f'tsd_{db_make_time}', con=engine, if_exists='append')
#print(today_searches_df.head())

# Get Google Top Charts
top_charts_df = pytrend.top_charts(2020, hl='en-US', tz=300, geo='US')
topcharts_df = pd.DataFrame(top_charts_df)
topcharts_df.to_sql(name=f'tcd_{db_make_time}', con=engine, if_exists='append')
#print(top_charts_df)

#Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='bts')
suggestions_df = pd.DataFrame(suggestions_dict)
suggestions_df.to_sql(name=f'sd_{db_make_time}', con=engine, if_exists='append')

a_dict = pytrend.categories()
categories_df = pd.DataFrame(a_dict)
categories_df = categories_df.applymap(str)
categories_df.to_sql(name=f'cd_{db_make_time}', con=engine, if_exists='append')

b_dict = pytrend.get_historical_interest(keywords=["bts","blackpink"], year_start=2020, year_end=2020)
historical_interest_df = pd.DataFrame(b_dict)
historical_interest_df.to_sql(name=f'hid_{db_make_time}', con=engine, if_exists='append')
print(b_dict)

print('finish sql')

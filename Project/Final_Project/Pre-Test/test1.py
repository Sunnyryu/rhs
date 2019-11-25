# 해당 파일은 pytrends library가 필수 .. 

# TrendReq => Trend Request / URL을 가져오는 좋은 친구!
from pytrends.request import TrendReq  
import pandas as pd
import csv 
import openpyxl

pytrends = TrendReq(hl='us', tz=360)
#hl은 header language => 사용언어라고 이해하자,  en-US / ko-KR 등 
#tz => timezone => 미국 360 / korea 540 ! 
# proxies => https proxies Google passed ONLY list ['https://34.203.233.13:80','https://35.201.123.31:880', ..., ...] => 굳이 잘안씀
# retries (재시도 횟수/ 연결 /읽기 의 수 )
# backoff_factor 재 시도 후 역류 요인!?
# ex) pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1)

# list 형식으로 확인하고 싶은 것 넣기 !

mylist = ["hyundai motor", "toyota"]
pytrends.build_payload(mylist, cat=0, timeframe='today 5-y', geo='US', gprop='') 
# mylist 는 위의 값 , cat = 카테고리 범주 (Category to narrow results) / timeframe => 일자 지정 (google trends 참조)  - 'today 5-y' => 5년 전부터 지금까지, all => 모두, 'YYYY-MM-DD YYYY-MM-DD' / 
#  'YYYY-MM-DDTHH YYYY-MM-DDTHH'(2017-02-06T10 2017-02-12T07)  (UTC를 기초로 함!) 
#  geo = 데이터를 수집할 코드(국가), gprop = 어느 사이트에서 가져올 지 나타내는 것, 
# image, news, youtube , froggle(구글 쇼핑..!) 을 넣을 수 있으며, 입력하지 않으면 모든 것에서 다 확인함
# pytrends.interest_over_time() => pandas DataFrame으로 출력되옵니다. / Returns pandas.Dataframe

getgaindata = pytrends.interest_over_time()
del getgaindata['isPartial']
getgaindata.to_csv('list.csv', encoding="utf-8") # csv 형식으로 파일을 만들어줌 ! / 인코딩은 utf-8로 해줌
### 추가적인 활용법 










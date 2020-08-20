# requests 라이브러리 가져오기
import requests
# url 요청
url =  'https://api.bithumb.com/public/ticker/btc'

response = requests.get(url)
# requests.get(url).json
print(response)
# print(response).json // json 방식으로 받음
print(response['data']['max_price'])

from flask import Flask, request, render_template, redirect, url_for
import random
import pandas as pd
import pymysql
import requests
from pprint import pprint
from nameyear import *
from nameday import *
from namemonth import *

app = Flask(__name__)

@app.route('/')
def hello():
    name = "World!"
    return f'Hello {name}'

@app.route('/mulcam')
def mulcam():
    return 'Hello Mulcam'

@app.route('/greeting/<string:name>') # <type:변수> type으로 받을지와 이름은 무엇인지 적어줌
def name(name):
    return f'{name} 님 안녕하세요.'

@app.route('/lunch/<int:number>') # 위와 마찬가지로 int 타입의 넘버를 받음
def lunch(number):
    menu = ["자장면", "짬뽕", "라면", "스파게티", "스테이크", "삼겹살"]
    order = random.sample(menu, number)
    #return str(order)
    return render_template('lunch.html', order=order)
@app.route('/lotto/')
def lotto():
    lotto = range(1,46)
    lotto_create = random.sample(lotto, 6)
    return f'{lotto_create}'
    #return str(lotto)

@app.route('/html')
def html():
    multiline = '''
    <h1> This is h1 Tag </h1>
    <p> This is P Tag</p>
    '''
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', name=name)

@app.route('/fake')
def fake_naver():
    return render_template('fake_naver.html')

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('receive.html', name=name, msg=message)

@app.route('/name2')
def name2():
    return render_template('name2.html')

@app.route('/namereceive')
def namereceive():
    year = request.args.get('year')
    year2 = year[3:4]
    month = request.args.get('month')
    day= request.args.get('day')
    year2row= Yearname(year2)
    monthrow= Monthname(month)
    dayrow= Dayname(day)
    return render_template('namereceive.html', year2row=year2row, monthrow=monthrow, dayrow=dayrow)

@app.route('/lotto_num')
def lotto_num():
    num = request.args.get("num")
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url).json()
    print(res)
    # list comprehension
    # [받는 변수 for 받는 변수 in 범위로 된 데이터]]
    wnum = [res[f'drwtNo{i}'] for i in range(1,7)]
    lotto = random.sample(range(1,47),6)
    match = list(set(wnum) & set(lotto))
    count = len(match)
    print(match)
    if count<3:
        msg = '등수 x'
    elif count==3:
        msg = '5등'
    elif count==4:
        msg = '4등'
    elif count==5:
        msg = '3등'
    elif count==6:
        msg = '1등'

    return render_template('lotto_result.html', msg=msg, wnum=wnum, lotto=lotto, num=num)
    #return f'{wnum}'

@app.route('/lotto_get')
def lotto_get():
    return render_template('lotto_get.html')

@app.route('/data')
def data():
    return render_template('data.html')






if __name__ =='__main__':
    app.run(debug=True, port=8003)

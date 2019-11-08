from flask import Flask, render_template, request, url_for, redirect
import requests
from decouple import config
from pprint import pprint
import random

app = Flask(__name__)
token = config('TOKEN')
base_url = f"https://api.telegram.org/bot{token}"

@app.route('/telegram')
def telegram():
    print(token)
    res = requests.get(f'{base_url}/getUpdates').json()
    chat_id = res['result'][0]['message']['chat']['id']
    a = range(1,47)
    lotto = random.sample(a,6)
    base_url2 = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={lotto}'
    print(base_url2)
    # 다른 방법 1
    #lotto = random.sample(range(1,47),6)
    # send_url = f'/sendMessage?chat_id={chat_id}&text={lotto}'
    # res = request.get(base_urL+send_url).json()
    # return '' 
    return redirect(base_url2)

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/send_msg')
def send_message():
    req = request.args.get('chat')
    res = requests.get(f'{base_url}/getUpdates').json()
    chat_id = res['result'][0]['message']['chat']['id']
    send_url = f'/sendMessage?chat_id={chat_id}&text={req}'
    response = requests.get(base_url+send_url)
    return "보내기 완료."

@app.route('/', methods=['POST'])
def tel_web():
    req = request.get_json().get('message')
    C_ID = config('C_ID')
    C_SC = config('C_SC')
    url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": C_ID,
        "X-Naver-Client-Secret": C_SC
    }

   
    

    if req is not None:
        text = req.get('text')
        chat_id = req.get('chat').get('id')
        if "로또" in text:
        #if text == "로또":
            text = random.sample(range(1,47),6)
            text.sort()
            send_url= f'/sendMessage?chat_id={chat_id}&text={text}'
            response =requests.get(base_url+send_url)
            #flask.redirect(flask.url_for('operation'), code=307)
            return redirect(response, code=200)
        elif "/번역" in text:
            re_text = text.replace("/번역", "")
            data = {
                        "source": "ko",
                        "target": "en",
                        "text": re_text
                    }
            res = requests.post(url, headers=headers, data=data).json()
            msg = res.get('message').get('result').get('translatedText')
            print(msg)
            send_url = f'/sendMessage?chat_id={chat_id}&text={msg}'
            response = requests.get(base_url+send_url)
            return redirect(response, code=200)
        else :
            send_url = f'/sendMessage?chat_id={chat_id}&text={text}'
            response =requests.get(base_url+send_url)
            return redirect(response, code=200)



    #pprint(req)

    #return '', 200
    
@app.route('/papago')
def papago():
    C_ID = config('C_ID')
    C_SC = config('C_SC')
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": C_ID,
        "X-Naver-Client-Secret": C_SC
    }

    data = {
        "source": "ko",
        "target": "en",
        "text": "안녕하세요"
    }

    req = requests.post(url, headers=headers, data=data).json()
    pprint(req)
    return "finish"



if __name__ =='__main__':
    app.run(debug=True)

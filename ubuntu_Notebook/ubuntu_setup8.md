## setup8

1. python flask

- install

```
전에 파이썬 가상화 구축을 했기에, 이번에는 flask(파이썬 웹 프레임워크 중 하나!)를 설치해보자면,
pip install flask를 이용해서 flask를 설치함.. 그러면 MarkupSafe, Jinja2, Werkzeug, itsdangerous, click, flask 등의 패키지가 설치가 됨

app.py를 만들어서 헬로우 월드를 테스트 해보자면
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
으로 py파일을 만들면 되옵니다.

그 후에  env FLASK_APP=app.py flask run을 터미널에 입력하면
아래와 같은 그림이 나옴..

```
![1010_01](https://i.imgur.com/7Nnvas2.png)
```
위는 터미널에서 띄운 창 / 아래는 홈페이지를 통해 들어간 창 
```
![1010_02](https://i.imgur.com/mthqee7.png)

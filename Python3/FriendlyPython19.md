## 파이썬 기초 정리 19

#### if i can learn to flask, i more useful python3!!


```
Flask
Django와 더불어 많이 사용하는 파이썬 프레임워크!

route : 페이지를 누가 처리할 것인지 함수와 매칭시키는 역할을 담당, 요청을 분석하여 세부 페이지 값을 얻음
URL 주소에 동적 파라미터도 넣을 수 있어~~

METHOD
GET / POST
Get : 데이터를 header를 통해 전송
Post : 데이터를 body를 통해 전송

ex) @app.route('/', method=[]'GET', 'POST'])
(GET 방식은 /에 들어오면, render_template에 해당하는 html을 불러옴)
(post 방식은 해당하는 부분이 올바르면 진행, 아니면 진행x)
(@app = decorater)

HTML5
(content, structure Yes)

CSS
(Style, design, animation Yes)

JS
(Javascript, interection, event, DOM(동적페이지 구성))

Module
request : get,post 등의 메소드 방식으로 데이터가 전달 시에 들어가는 객체!
render_template : html을 읽고 랜더링하여 브라우저로 전송하는 텍스트 구성(flask에서 사용하는 jinja 2 엔진 구동!)
redirect : 요청을 다른 쪽으로 보내주는 역할을 함
url_for  : 함수명을 통해서 라우트된 주소를 반환하는 함수

html에서 input은 사용자의 입력을 받는 태그이며, name은 데이터 키 속성, form은 전송의 행 담당해줌

render_template으로 전달한 부분을 받을 때에는 {{키}}로 받음
```

```
추후에 추가 정리 예정!
```

## Basic6

#### python Django 5


```
REST
(Representational State Transfer)
Roy Fielding 논문으로 아키텍쳐 발표
 - http 설계의 우수성에 비해 제대로 활용하고 있지 않아 발표함.

HTTP
 - Request/ Response 로 서버와 클라이언트간에 Http로 통신

 웹서버는 웹 리소스를 관리하고 제공을 함.
1. 미디어 타입 : 수천가지 데이터 타입이 존재
MIME(Multipurpose Internet Mail Extensions)
 html : text/html
 jpeg : image/jpeg
 ASCII : text/plain

2. URI (URL + URN)
 URL : 리소스의 위치  (스킴://서버위치/경로) 스킴: 리소스에 접근하기위한 프로토콜
 URN : 위치에 독립적임.

REST 의 구성
자원 - URI
행위 - HTTP Method(GET/POST/PUT/DELETE/PATCH)
표현

(Http Method) (자원)  형식으로 표현.

ex)
GET /boards/1  보드에 있는 1번 글의 정보를 GET해라
PUT /boards/1  보드에 있는 1번 글을 업데이트 해라
DELETE /boards/1 보드에 있는 1번글을 삭제해라.

djagno는 GET/POST만 기본 제공됨.
부득이 하게 uri에 행위를 사용
django는 마지막에 '/'가 필수이므로
부득이하게 마지막에 '/'를 붙여줌.


REST 디자인 가이드
'/'는 계층 관계를 나타내는데 사용
'_' 대신 '-' 를 활용
정보의 자원을 표현해야함.


GET /boards/show/1 show라는 행위가 있기때문에 REST하지 않음.
GET /boards/1

GET /boards/create ( REST X)
POST /boards

GET /boards/1/update ( REST X)
PUT /boards/1
POST /boards/1/edit (django)

GET /boards/1/delete ( REST X)
DELETE /boards/1
POST /boards/1/delete (django)

Django 에서는 Http method 를 GET/POST

/boards/new
 데이터를 생성하기위한 폼을 불러오는거기 때문에 GET
/boards/create
 데이터를 생성을하기때문에 POST

GET /boards/new
POST /boards/new

request.method 를 이용해서 나누어 실행가능.


ex) {% for com in a_set.all %}

```

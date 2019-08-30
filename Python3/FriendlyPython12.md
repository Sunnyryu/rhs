## 파이썬 기초 정리 12


#### imagine Python

```
Network

TCP
IP 위에서 구성
IP는 데이터를 잃어버릴 수 있음 - 데이터를 저장하고 있다가 손실이 일어난 것으로 추청하면 재전송
전송 윈도우를 통해 흐름 제어를 조절, 믿을만한 pipe 역할을 제공

TCP 연결 / 소켓
컴퓨터 네트워킹에서 인터넷 소켓, 또는 네트워크 소켓은
인터넷 프로토콜을 기반으로 한 인터넷 등의
컴퓨터 네트워킹에서 양방향 커뮤니케이션의 끝점!

TCP 포트 번호
포트는 애플리케이션에 대응되거나 프로세스에 대응되는 소프트웨어 커뮤니케이션의 말단
한 서버에 여러 네트워크 애플리케이션이 존재할 수 있게 해줌!

ex) 25(SMTP) : 이메일 수신 / 23 : 로그인 / 80(HTTP), 443(HTTPS - secure) : 웹서버 / 109.110 : 개인 메일(POP) / IMAP(143/220/993) - Mail Retrieval / DNS (53) : Domain name / FTP (21) : 파일 전송

URL에 포트 번호가 있는 경우가 있는데, 이는 웹 서버가 ‘관례적으로 정해진’ 포트에서 돌지않는 경우

파이썬 소켓
파이썬은 내부적으로 TCP 소켓을 지원
ex) import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('abc.dasda.org(호스트)', 80(포트)) )

애플리케이션 프로토콜
메일
월드 와이드 웹(WWW)

HTTP(HyperText Transfer Protocol) - 하이퍼텍스트 전송 프로토콜
인터넷, 애플리케이션 레이어에서 가장 많이 사용되는 프로토콜
웹을 위해 개발 - HTML, 이미지, 문서 등을 가져옴
문서 외에 다양한 데이터에도 확장하여 사용 가능
RSS, 웹 서비스 등
기본 컨셉: 연결 - 문서 요청 - 문서 수신 - 연결 종료
브라우저가 서버로부터 인터넷을 통해 웹 문서를
받는 경우의 규칙을 정한 것

그렇다면 프로토콜은?

규칙의 모음. 모두가 따르므로 서로가 서로의 행동을 예측 가능
서로 충돌하지 않아야 함

http://www.abcde.com/1.htm (프로토콜 + 호스트 + 문서)

서버로부터 데이터 받기
사용자가 ‘href=값’을 가지고 있는 앵커 태그를 클릭해 새로운 페이지로 이동할 때마다 브라우저는 웹 서버와 연결을 만들고 GET 요청을 실행해 페이지 URL에 나타난 값을 수신
서버는 문서를 포맷팅하고 유저에게 보여주는 HTML 문서를 리턴

브라우저를 클릭한 후에 GET 방식으로 웹 서버에 요청 - 웹서버가 응답해줌 - 파싱/ 렌더링 해줌

인터넷 표준
모든 인터넷 프로토콜 기준은 한 기관에 의해 개발
Internet Engineering Task Force (IETF)
www.ietf.org 기준은 “RFCs”라고 부름 - “Request for Comments”

HTTP 요청을 만드는 법
서버에 연결하고 도메인 접속 - 문서 요청 (기본문서 요청) - (ex)GET 방식
```
```
웹 브라우저 만들기
mport socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://adsaddasd.com/1.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
data = mysock.recv(512)
if (len(data) < 1):
break
print(data.decode(),end='')
mysock.close()
```

```
HTTP/1.1 200 OK
Date: Sun, 14 Mar 2010 23:52:41 GMT
Server: Apache
Last-Modified: Tue, 29 Dec 2009 01:31:22 GMT
ETag: "143c1b33-a7-4b395bea"
Accept-Ranges: bytes
Content-Length: 167
Connection: close
Content-Type: text/plain <header>
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief <body>
```

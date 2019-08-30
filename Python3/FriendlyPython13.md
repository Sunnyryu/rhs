## 파이썬 기초 정리 13


#### hahahoho Python

```
network2

ASCII(아스키 코드 - American Standard Code for Information Interchange)

간단한 문자열 표현방법
각 문자는 0~256 사이의 숫자로 대응되어 저장되며, 이는 메모리에서 8비트를 차지
8비트를 메모리에서 "byte"로 정함, ord() ASCII 문자에 대응되는 숫자를 리턴

유니코드
.

여러바이트로 된 문자
UTF-16 – 길이 고정됨 - 2 바이트
UTF-32 – 길이 고정됨 - 4 바이트
UTF-8 – 1-4 bytes
ASCII를 포함하며, 호환, ASCII를 자동으로 감지 가능, UTF-8 은 시스템 간에 데이터를 교환할 때 가장 실용적으로 추천되는 인코딩 형식

파이썬 2와 3의 차이 : u'써니'가 있다고 하면 2버전은 unicode이며, 3버전은 str 이다 . a = t'sunny'가 있다고 할 때 2버전은 str이지만 3버전은 bytes임

파이썬 3의 모든 문자열은 유니코드 형식! / 파일에서 데이터를
가져와 파이썬에서 작업하는 경우 거의 대부분 작동함!

소켓을 통해 네트워크로 데이터를 전송하거나 DB와 연결하는 경우 데이터를
인코딩/디코딩해야 함

파이썬 문자열에서 Byte로 네트워크 소켓 등 외부 자원과 통신하는 경우, 문자열이 아니라 Byte 형식을 사용해야 함. 따라서 파이썬 3에서는 문자열을 Byte로 인코딩 필요

외부에서 데이터를 가져오는 경우 해당 문자셋에 대하여 디코딩을 해야 파이썬3에서 정상적인 문자열으로 사용할 수 있음

파이썬에서의 HTTP 요청

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://dssaada.com/1.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
data = mysock.recv(512)
if (len(data) < 1):
break
print(data.decode())
mysock.close()

소켓 - > Bytes utf-8 - > 문자열 unicode - > Bytes utf-8 -> 소켓
(recv -> decode() -> encode() -> send() )

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://dssaada.com/1.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
while True:
data = mysock.recv(512)
if (len(data) < 1):
break
print(data.decode())
mysock.close()

urllib로 HTTP 요청 간소화
HTTP는 굉장히 많이 쓰이기 때문에 소켓을 다루고 웹 페이지를 불러오는 라이브러리가 있음

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://dssaada.com/1.txt')
for line in fhand:
print(line.decode().strip())

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief (결과)
```
```
mport urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://dssaada.com/1.txt')
counts = dict()
for line in fhand:
words = line.decode().split()
for word in words:
counts[word] = counts.get(word, 0) + 1
print(counts)
```

```
웹 페이지 읽기
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://www.dsadad.com/page1.htm')
for line in fhand:
print(line.decode().strip())
<h1>The First Page</h1>
<p>If you like, you can switch to the <a
href="http://www.dsadad.com/page2.htm">Second
Page</a>.
</p>

```

```
HTML 파싱(웹 스크래핑 이라고 함 )

프로그램이나 스크립트가 브라우저처럼 행동하며 페이지를 살펴보고 정보를 추출하고 조사하는 것을 지칭

검색엔진은 웹 페이지를 스크래핑함 이걸 스파이더링 또는 크롤링이라고도 함

why 스크래핑?

데이터를 가져오기 - 특히 소셜 데이터 - 누가 연결돼 있는지
외부로 내보내는 기능이 없는 시스템에서 데이터 가져오기
사이트를 모니터링하며 새로운 정보 감지
검색엔진의 데이터베이스를 구축하기 위한 스크래핑

웹 페이지 스크래핑은 웹 페이지 내용을 마음대로 빼간다는
점에서 논란의 여지가 있음
copyright된 정보를 다시 출판하는 것은 허용되지 않음
이용약관을 위배하지 않도록 유의
```

```
TCP/IP는 애플리케이션 사이에 파이프/소켓을 구축
• 애플리케이션 프로토콜로 이 파이프를 사용
• HyperText Transfer Protocol(HTTP)는 간단하지만 굉장히
강력한 프로토콜
• 파이썬은 소켓, HTTP, and HTML 파싱을 충실히 지원
```

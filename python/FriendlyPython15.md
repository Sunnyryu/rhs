## 파이썬 기초 정리 15


#### I like Python

```
JavaScript Object Notation(JSON)

자바스크립트의 객체 표현 방식 (Douglas Crockford - 발견)

www.json.org 참조

import json
data = '''{
"name" : "sunny",
"phone" : {
"type" : "intl",
"number" : "+82 xxxx-xxxx"
},
"email" : {
"hide" : "yes"
}
}'''
info = json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

import json
input = '''[
{ "id" : "001",
"x" : "2",
"name" : "sunny"
} ,
{ "id" : "009",
"x" : "7",
"name" : "sunny"
}
]'''
info = json.loads(input)
print('User count:', len(info))
for item in info:
print('Name', item['name'])
print('Id', item['id'])
print('Attribute', item['x'])
```

```
SOA(서비스 지향적 접근)

대부분의 대형 웹 애플리케이션은 서비스를 이용
다른 애플리케이션으로부터 서비스를 사용
ex) 신용카드 청구 / 호텔 예약 서비스
서비스는 애플리케이션이 서비스를 이용하기 위해 따라야하는 “규칙”을 만듦(API)

다수의 시스템
초기에는 두 시스템이 협력하여 문제를 나눔
데이터와 서비스가 유용해지며 다수의 애플리케이션이 정보를 이용하려 함

웹 서비스

응용 프로그램 인터페이스(API)
API는 인터페이스를 지정하고 그 인터페이스의 객체의 행동을 제어한다는 점에서 매우 추상적. API에 명시된 기능을 제공하는 소프트웨어를 API 의 “실행”이라고 하며,
API는 대체로 애플리케이션을 구성하게 되는 언어로 정의됨.

API 보안과 비율 제한

API를 실행하기 위한 계산 자원은 “무료”가 아님
API를 통해 제공된 데이터는 대체로 매우 가치가 높음
데이터의 제공자는 하루 요청량을 제한하여서 API 의 “키”를 요구하거나, 사용료를 부과하기도 함
발전을 거치면서 여러 규칙들이 바뀌기도 함


last
서비스 지향 아키텍쳐 - 애플리케이션이 부분적으로 나뉘어 네트워크 상에 퍼질 수 있게 함
응용 프로그램 인터페이스(API) 상호 작용에 대한 계약/약속
웹서비스는 애플리케이션끼리 네트워크 상에서 협력할 기반을 제공함 - SOAP와 REST는 웹서비스의 두 가지 형태
XML과 JSON은 직렬화 형식
```

## 파이썬 기초 정리 14


#### music Python

```
XML
데이터를 마크업하여 네트워크 상에서 전송

웹 상의 데이터
HTTP 요청과 응답에 대한 이해와 지원을 바탕으로, 이 프로토콜을
이용한 프로그램 간의 정보 교환의 추세

네트워크와 응용프로그램 간의 데이터 표현 방식에 있어서 합의가
필요

가장 널리 사용되는 두 가지 포맷: XML과 JSON

네트워크를 통한 정보 전송
(와이어 프로토콜 : 와이어상으로 보내는 것 )
```

```
ex 1) python dictionary - > Java hashpmap
(직렬화를 한 후에 역직렬화를 하여 와이어 포맷을 합의함)
```

```python
XML 요소들
<animals>
  <animal>
  #단순요소
    <name>panda</name>
    <age>7</age>
  </animal>
  # 복합요소
  <animal>
    <name>bear</name>
    <age>5</age>
  </animal>
</animals>
```

```
extensible markup language = xml
  정보 시스템이 구조화된 데이터를 공유하는 것이 목적
  표준범용교정용어(SGML)의 간소화된 버전으로 시작(인간에게 친숙한 방향으로 디자인)

XML의 기초
  시작 태그 start tag
  끝 태그 end tag
  문자 정보 text element
  속성 attributes
  스스로 닫는 태그 self closing tag

공백
  줄의 끝은 중요하지 않음. 문자 요소에서 공백은 없어짐.
  오직 가독성만을 위해 들여쓰기를 함.
XML용어
  태그 Tags 는 요소의 시작과 끝을 알려줌
  속성 Attributes - XML의 여는 태그에 위치한 키-값 쌍
  직렬화 Serialize / 역직렬화 De-Serialize - 한 프로그램의 데이터를 특정 프로그램 언어에 제한되지 않은 채로 시스템 내에서 저장되고전달되어질 수 있는 형식으로 변환하는 것
XML 트리
  요소와 문자로 이루어짐
```
```
<a>
<b w="5">X</b>
<c>
<d>Y</d>
<e>Z</e>
</c>
</a>

w = 속성
X = 문자 노드
a/b/X | /a/c/d Y | /a/c/e/ Z
```

```
XML 스키마

XML이 받아들이는 형태의 “ 약속 ” 을 설명

문서의 구조와 내용에 대한 제한의 형식으로 표현됨
시스템 간의 “약속”을 표현할 때 주로 사용됨 - “내 시스템은 이
스키마에 맞는 XML만 수용하는 거임"
특정 XML이 스키마의 사항들을 만족할 때 우리는 그것을
“타당하다 (validate)” 라고 함

XML - > XML 검증기 < - XML 스키마 계약서
```
```
<person>
<lastname>sunny/lastname>
<age>26</age>
<dateborn>1994-mm-dd</dateborn>
</person>
# XML 문서
<xs:complexType name=”person”>
<xs:sequence>
<xs:element name="lastname" type="xs:string"/>
<xs:element name="age" type="xs:integer"/>
<xs:element name="dateborn" type="xs:date"/>
</xs:sequence>
</xs:complexType>
# XML 스키마 계약서
```
문서 타입 정의 Document Type Definition (DTD)
표준 범용 교정 용어 (ISO 8879:1986 SGML)
XML 스키마 W3C - (XSD)

XSD XML 스키마 (W3C spec)구조
  W3C 스키마”라고 불리는 이유는 “스키마”가 포괄적인 표현이기 때문
  XSD 라 불리는 이유는 파일 확장명이 .xsd 이기 때문
```

```
XSD 구조

• xs:element
• xs:sequence
• xs:complexType

<xs:complexType name=”person”>
<xs:sequence>
<xs:element name="lastname" type="xs:string"/>
<xs:element name="age" type="xs:integer"/>
<xs:element name="dateborn" type="xs:date"/>
</xs:sequence>
</xs:complexType>

XSD 제한

<person>
<full_name>Sunny</full_name>
<child_name>ryu</child_name>
<child_name>ky</child_name>
<child_name>john</child_name>
<child_name>spio</child_name>
</person>

<xs:element name="person">
<xs:complexType>
<xs:sequence>
<xs:element name="full_name" type="xs:string"
minOccurs="1" maxOccurs="1" />
<xs:element name="child_name" type="xs:string"
minOccurs="0" maxOccurs="10" />
</xs:sequence>

XSD 데이터 타입
<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>
<xs:element name="startdate" type="xs:dateTime"/>
<xs:element name="prize" type="xs:decimal"/>
<xs:element name="weeks" type="xs:integer"/>

<customer>Sunny ryu</customer>
<start>1994-mm-dd</start>
<startdate>aaaa-bb-ccT09:30:10Z</startdate>
<prize>1234.50</prize>
<weeks>40</weeks>
```

```
ISO 8601 날짜/시간 형식
aaaa-bb-ccT09:30:10Z
(년/월/일) (시간/Z(주로 현지 시간대가 아닌 UTC / GMT로 명시)

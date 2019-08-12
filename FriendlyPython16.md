## 파이썬 기초 정리 16


#### enjoy enjoy python

```
파이썬 객체

객체 지향

프로그램은 서로 협력하는 여러 개의 객체로 구성
전체 프로그램이 아닌 각각의 객체가 마치 프로그램 안의 섬같이 서로 협력하여 작동
프로그램은 함께 실행되는 여러 개의 객체로 구성 - 객체는 서로의 기능들을 활용
```

```
객체
객체는 하나의 자족적인 코드와 데이터
객체 지향 접근의 요점은 문제를 이해가능한 작은 문제로 분할하여 접근(분할 정복 divide-and-conquer)
객체는 우리가 필요없는 세부사항들을 무시할 수 있도록 경계를 제공
우리는 객체를 계속 사용해 왔음: 문자열 객체, 정수형 객체, 딕셔너리 객체, 리스트 객체..

입력 - 객체 <-> 딕셔너리
입력 - 객체 <-> 문자열
입력 - 객체 - > 객체 - > 출력

입력 - 코드데이터 <-> 코드데이터 - > 코드/데이터 - >> 출력   
(객체는 코드와 데이터의 집합체)
객체는 세부사항을 감춤 - 프로그램의 나머지 부분의 세부사항을 무시할 수 있게 해줌
```

```
클래스 (Class)  - 하나의 형식, 템플릿
메소드 (Method or Message) - 클래스 내에 정의된 기능
필드/속성 (Field or attribute)- 클래스 내의 데이터
객체/인스턴스 (Object or Instance) - 클래스의 한 인스턴스
```

```
클래스

어떤 물체(객체)의 특징(필드 또는 속성)과 행동(메소드, 연산 등의 기능) 등 추상적인 특성을 정의. 클래스를 어떤 것의 특성을 설명하는 설계도 혹은 공장이라고도 이야기함. 예를 들어, 개 라는 클래스는 품종 또는 털색깔(특성), 혹은 짖거나 앉는 행위(행동) 등 개들이 가지는 특성을 가짐

인스턴스 (객체와 인스턴스는 자유롭게 바꾸어 부를 수 있다 )

클래스 안에서 인스턴스 혹은 특정 객체를 가질 수 있음. 인스턴스란 실행 중 실제로 생성된 객체를 의미. 프로그래머의 용어를 따르면, “래씨"라는 객체는 “개”라는 클래스의 한 인스턴스임. 특정 객체의 특성들을 모아놓은 것을 상태라고 함. 객체는 클래스 안에서 정의된 상태와 행동으로 구성됨.

메소드 (메소드와 메시지는 자유롭게 바꾸어 부를 수 있음)

객체의 능력. 언어로 따지만 메소드는 동사임. 래시는 개로써 짖을 수 있는 능력이 있음. 그래서 bark() “래시”의 한 메소드가 됨. 이것 외에
다른 메소드들도 가질 수 있음. 예를 들면 sit(), eat(), walk() 또는 save_timmy() 등. 프로그램 내에서는 메소드는 하나의 객체에만
영향을 줄 수 있음. 모든 개는 짖을 수 있지만, 실제로 짖는 행위는 수행하는 개는 하나 밖에 없음.
```

```python
#ex1)
>>> x = 'abc'
>>> type(x)
<class 'str'>
>>> type(2.5)
<class 'float'>
>>> type(2)
<class 'int'>
>>> y = list()
>>> type(y)
<class 'list'>
>>> z = dict()
>>> type(z)
<class 'dict'>

>>> dir(x)
[ … 'capitalize', 'casefold', 'center', 'count',
'encode', 'endswith', 'expandtabs', 'find',
'format', … 'lower', 'lstrip', 'maketrans',
'partition', 'replace', 'rfind', 'rindex', 'rjust',
'rpartition', 'rsplit', 'rstrip', 'split',
'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
>>> dir(y)
[… 'append', 'clear', 'copy', 'count', 'extend',
'index', 'insert', 'pop', 'remove', 'reverse',
'sort']
>>> dir(z)
[…, 'clear', 'copy', 'fromkeys', 'get', 'items',
'keys', 'pop', 'popitem', 'setdefault', 'update',
'values']

```

```python
# 클래스 예시

class PartyAnimal:   # PartyAnimal 객체를 만드는 템플릿  / 클래스는 예약어임 !
 x = 0 # 각각의 PartyAnimal = 객체에는 일정량의 = 데이터가 있음
 def party(self) :
 self.x = self.x + 1
 print("So far",self.x)
 an = PartyAnimal()  # PartyAnimal 객체를 생성하여 an 에 저장
 an.party()
 an.party() # PartyAnimal.party(an)
 an.party() # 객체에게 party() 를 실행하라고 알려줌
```

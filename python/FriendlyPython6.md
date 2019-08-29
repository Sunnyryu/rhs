## 파이썬 기초 정리 6


#### cheer Python

- 읽기와 변환
  - 문자열을 통해 데이터를 읽고 파싱하고 필요한 데이터를 변환 하는 것을 선호
  - 이 예시는 에러와 잘못된 사용자 입력에 대한 상황 파악에 좋은
  길잡이
  - 숫자 입력은 문자열에서 변환되어야 함
```Python
name = input('Enter : ')
print(name)
# ex) name input is sunny - > print(name) = sunny
numbername = input('Enter : ')
x = numbername - 20
# numbername is str - > str - int => error
x = int(numbername) - 20
print(x)
# 80
```

- 문자열 파악하기
  - 문자열에 있는 어떤 문자든지 대괄호
안에 지정된 인덱스를 이용해서 가져올
수 있음
- 인덱스 값은 정수이며, 0에서 시작
- 인덱스로 계산 가능한 표현식을 사용 가능

```Python
p y t h o n
0 1 2 3 4 5
comlang = 'python'
letter = comlang[1]
print(letter)
# y
a = 5
b = comlang[a - 1]
print(b)
# o
```

- 범위 밖 문자
  - 문자열 크기를 넘어선 인덱스에 접근하려고 하면 파이썬 에러가 발생
  - 인덱스 값을 계산 하거나 문자열을 자를 때 주의
```python
abc = 'king'
print(abc[6])
# error - 배열 범위를 넘어섬
```

- 내장함수 len은 문자열의 길이를 반환함
- len
  - 함수는 저희가 사용하는 어떤 저장된 코드. 함수는 입력을 받아서
출력
```Python
comlang = 'python'
a = len(comlang)
print(a)
# 6
def len(inp) :
  blah
  blah
  for a in b:
    blah
    blah
```

- 문자열을 통한 루프
  - while 구문, 반복 변수, len 함수를 이용해서 문자열
안에 있는 각 문자를 독립적으로 확인하는 루프를 만들 수 있음
```python
comlang = 'python'
index = 0
while index < len(comlang) :
  letter = comlang[index]
  print(index, letter)
  index = index + 1
 #0 p
 #1 y
 #2 t
 #3 h
 #4 o
 #5 n
 comlang = 'python'
 for letter in comlang :
   print(letter)
#for 구문을 이용하는 유한 루프가 더 깔끔함
#반복 변수는 for 루프에 의해 완벽하게 관리됨
```
- 루프와 개수 세기
  - 문자열에 있는 각 문자에 대해 루프를 실행해서 문자 ‘a’의 개수를 세는 간단한 루프
```python
word = 'python'
count = 0
for letter in word :
  if letter == 'y':
    count = count + 1
print(count)
# letter 반복변수 / word는 문자열 6개로 이뤄진것
# 반복 변수는 시퀀스(순서가 있는 집합)를 통해 “반복”
# 코드의 루프 블럭 (본문)은 시퀀스 안의 각 값에 대해 한번씩 실행
# 반복 변수는 시퀀스 안의 모든 값을 가지고 실행
# 반복 변수 문자열을 통해 “반복”하고 코드 블럭 (본문) 은 시퀀스 안에 있는 값 하나에 대해서 한 번씩 실행
```
- 다른 문자열 연산
  - 문자열 슬라이싱
    - 콜론 연산자를 사용해서 문자열의 연속적인 구간을 가져올 수 있음
    - 두 번째 숫자는 문자열 조각보다 한 글자 너머를 가리킴 - “~까지 이지만 포함하지 않음"
    - 두 번째 숫자가 문자열 마지막 너머를 가리키는 경우 문자열의 마지막에서 멈춤
```Python

A l i k e   P y t h  o  n
0 1 2 3 4 5 6 7 8 9 10 11
ik = 'Alike Python'
>>> print(ik[0:4])
Alike
>>> print(ik[6:7])
P
>>> print(ik[6:30])
Python
print(ik[:3])
Ali
>>> print(ik[7:])
ython
>>> print(ik[:])
Alike Python
```
- 문자열 병합
  - + 연산자가 문자열에  적용되면, “병합”을 의미
    - ex) a = 'hi' b = a + 'K'
    - print(b) = hi K
    - c = a  + ' ' + 'K'
    - print(c) = hi K
- 논리 연산자 in
  - in 키워드는 어떤 문자열이 다른 문자열에 “포함”되는지 확인하기 위해서도 사용
  - in 표현식은 참 또는 거짓값을 반환하는 논리 표현식이며 if 구문에 사용될 수 있음
```python

comlang = 'python'
'n' in comlang
True
'b' in comlang
False
'yth' in comlang
True
if 'a' in comlang :
... print('Found it!')
...
# Found it!

if word == 'python':
print('All right, python.')
if word < 'python':
print('Your word,' + word + ', comes before python.')
elif word > 'python':
print('Your word,' + word + ', comes after python.')
else:
print('All right, python.')
```
- 문자열 라이브러리
  - 파이썬은 여러 개의 문자열 함수를 정의하는 문자열 라이브러리가 존재
  - 이 함수는 모든 문자열에 이미 내장 되어 있음 - 함수를 문자열 변수에 붙임으로써 호출
  - 이 함수는 원본 문자열을 수정하지 않고, 대신 바뀐 새로운 문자열을 반환
```Python
greet = 'Hello sunny'
abo = greet.lower()
print(abo)
#hello sunny
print(greet)
#Hello sunny
print('Hi There'.lower())
#hi there

# 문자열 라이브러리의 예
str.capitalize()
str.center(width[, fillchar])
str.endswith(suffix[, start[, end]])
str.find(sub[, start[, end]])
str.lstrip([chars])
str.replace(old, new[, count])
str.lower()
str.rstrip([chars])
str.strip([chars])
str.upper()
```

- 문자열 탐색
  - find() 함수를 이용해서 하위 문자열을 다른 문자열에서 탐색 가능
  - find() 하위 문자열의 첫 번째로 나타나는 위치를 검색
  - 하위 문자열을 찾지 못하면, find()는 -1을 반환
  - 문자열 좌표는 0에서 시작한다는 것에 주의

```Python
  p y t h o n
  0 1 2 3 4 5
  comlang = 'python'
  pos = comlang.find('yt')
  print(pos)
  # 1
  aa = comlang.find('z')
  print(aa)
  #-1
```
- 모든 문자를 대문자로 만들기
  - 문자열의 복사본을 모두 You can make a copy of a string in 소문자 또는 대문자로 치환 가능
  - find()를 이용해서 문자열을 탐색할 때, 문자열을 먼저
  소문자로 바꾼 뒤 탐색하면 대소문자와 관계 없이 문자열을
  탐색 가능
```Python

greet = 'Hello sunny'
ooo = greet.upper()
print(ooo)
# HELLO sunny
www = greet.lower()
print(www)
# hello sunny
```
- 공백 제거
  - 종종 문자열의 끝과 마지막에 남아있는 공백을 제거
  - lstrip() 과 rstrip()은 각각 문자열 왼쪽과 오른쪽에 있는
공백을 제거
  - strip() 문자열 시작과 끝에 있는 모든 공백을 제거
```python
greet = '
Hello sunny
greet.lstrip()
'Hello sunny '
greet.rstrip()
'Hello sunny'
greet.strip()
'Hello sunny'
```
- 접두사
```Python
line = 'Nice Game'
line.startswith('Nice')
True
line.startswith('n')
False
```

- 파싱과 추출
```Python

From hisunny.nicelike@abc.de.fg Mon Jan
5 09:14:16 2014
data = 'From hisunny.nicelike@abc.de.fg Mon Jan 5 09:14:16 2014'
atpos = data.find('@')
print(atpos)
21
sppos = data.find(' ',atpos)
print(sppos)
31
host = data[atpos+1 : sppos]
print(host)
abc.de.fg
```

- 두 종류의 문자열
```Python
#Python 3.5.1
>>> x = '써니'
>>> type(x)
<class 'str'>
>>> x = u'써니'
>>> type(x)
<class 'str'>

```

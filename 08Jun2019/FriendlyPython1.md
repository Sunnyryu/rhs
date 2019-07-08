## 파이썬 기초 정리 1


#### Hello Python

- 파이썬은 귀도 반 로섬이라는 분께서 만듬!
- Month Python`s Flying에서 이름을 따옴.
- 문법 에러가 뜨는 것은 컴터에게 사랑 표현을 잘 못하는 것!
- cmd를 이용해서 편하게 사용 가능


- 문법 에러에 대한 대처
  - 처음에는 실수가 있을 수 밖에 없음
  - 그래서 문법 에러가 발생하면 감정적으로 받아드리지 말기
  - 우리가 파이썬을 배우는 것이 컴퓨터가 우리 언어를 배우는 것보다 빠름

- 파이썬의 요소
  - 단어
  - 문장 구조
  - 이야기 구조


```Python
x = 10
print(x)
---output 10
x = x + 10
print(x)
20
exit()
# 파이썬 덧셈의 예
```

- 문장 / 줄
  - x = 2 (대입문/ x는 변수 / 2는 상수 / =은 연산자)
  - x = x +2 (대입문 + 표현식)
  - print(x) (출력문 / print() = 함수 )

- 대화식과 스크립트
  - 대화식
    -  파이썬에 한 줄을 입력하면 바로 반응
  - 스크립트
    - 텍스트 에디터를 사용해 파일에 명령을 적고 파이선이 파일에 있는 명령을 실행

- 예약어와 문장 이용 (ex)
  - 예약어
    - 파이썬이 정한 의미로만 쓰이는 아이!
  ```
    and / del / global / not / with / as / elif / if /or / else / import
    break/ raise / finally / continue 등
  ```
- 순차문 과 조건문
``` Python
  x = 77
  print(x) # 77
  x = x + 23
  print(x) # 100
  # 순차문은 레시피나 설명문과 같이 진행 순서를 가짐
  # 프로그램은 순차적으로 진행 / 프로그램의 흐름을 결정
  y = 22
  if y < 25:
      print('Young') # Young을 출력
  if y > 25 :
      print('Old') # Old를 출력

  print('hello')
  # 조건문은 건너 뛸 수 있음
  # Young과 hello를 출력
```
```python
- 반복문
# 반복무은 반복돼 실행함.
a = 10
while a > 0 :
  print(a)
  a = a - 2
  print('goodbye')
  # 10 / 8 / 6 /4 / 2 /goodbye로  끝
  # 반복 변수는 루프 한번을 돌떄마다 변함.
```

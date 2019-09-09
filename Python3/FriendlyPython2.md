## 파이썬 기초 정리 2


#### WoW Python

- 상수(constants)
  - 값이 변하지 않아 숫자, 글자, 문자열과 같은 고정값을 상수 !!
  - 숫자 상수
  - 문자열 상수는 작은따옴표나 큰따옴표로 표시
``` Python
print(100) # 100을 출력
print(22.2) # 22.2를 출력
print('WOW Python') # WOW Python을 출력 (WOW Python가 상수)
```

- 변수(variables)
  - 변수를 통해 메모리를 할당하고 이름을 지어 변수 이름을 통해 데이터를 저장하고 검색 가능
  - 프로그래머가 변수 이름을 지정
  - 대입문 을 통해 변수값을 변경 가능
  - 예약어를 변수 이름/식별자로 사용할 수 없음
  ```Python
  x = 22.0
  print(x) # 22.0을 출력
  y = 19.9
  print(y) # 19.9을 출력
  x = 2932
  print(x) # 2932을 출력함 / 다시 x값을 선언하면 바뀜
  ```

  파이썬 변수 이름 규칙
  ```Python
  글자나 밑줄로 시작  (첫자리는 숫자는 안됨)
  대소문자를 구분함
  이름에 **.** 같은 기호로 시작하는 것은 지으면 안됨.

  # ex 1 (Worst - 실행에는 문제가 없지만 어려운 이름은 좋지 않음)
  adsadadadas = 39
  zcxzvwqrvzx = 77
  bsbadasawraw  = adsadadadas * zcxzvwqrvzx
  print(bsbadasawraw)

  # ex 2 (Bad - 이해하기 쉬운 이름이 더 좋음 )
  a = 39.0
  b = 17.0
  c = a * b
  print(c)
  # ex 3 (Good -이해하기가 좋음 )
  hours = 77.0
  rate = 16.0
  pay = hours * rate
  print(pay)
  ```

  - 대입문
    - 오른쪽 결과를 왼쪽 변수에 저장하는 것으로 구성됨.
    - 대입문( = )으로 변수 값을 지정
  ```Python
  x = 0.5
  x = 4.2 * x * (1-x)
  print(x) # 1.05가 출력됨.
  x = 4.2 * x * (1-x)
  print(x) # -0.2205가 출력됨
  ```
  - 표현식(숫자)
    - 컴퓨터 키보드에 수학 기호가 부족하기 때문에 computer-speak를 사용해 연산
    - +(더하기), - 빼기, * 곱하기, / 나누기 ** 거듭제곱, % 나머지로 쓰임
    - 일반적으로 괄호 -> 거듭제곱 -> 곱셈,나눗셈,나머지  -> 덧셈,뺼셈 -> 왼쪽에서 오른쪽
  ```Python
  #ex 1)
  #x = 5 + 4 * 3 / 2 ** 1 이 있다면 어떤 것을 먼제해야하나?
  # 2**1 -> 4 *3 -> 4*3/2 -> 앞의 더하기
  print(x) # 11
  ```

  - Type(타입 - 자료형)
    - 변수, 문자, 상수라는 자료형이 있음
    - 문자열 + 1은 안되요.. (어떤 연산은 금지 되어있음)
    - type() 함수를 써서 자료형을 알 수 있음
  ```python
    #ex
    spotv = 103 + 4
    print(spotv) # 107로 출력됩니다.

    ogn = 'hello ' + ' ogn'
    print(ogn) # hello ogn로 출력됩니다.

    ogn = ogn + 1 # 문자열 타입과 정수형 타입을 더하려 했기 때문에 에러가 발생합니다.

    #타입 소개

    itv = 'hello' + ' world'
    print(itv) # hello world

    type(itv) # class 'str' 문자열 클레스 타입
    type(1) # 정수 클레스 타입 - int!

    #타입 예시와 변환 소개
    v = 999
    type( v ) # int 타입
    r = float( v ) # float 타입으로 변환
    print( r ) #999.0으로 출력
    type( r ) # float 타입
    # int는 정수 타입이며, float는 부동 소수점 수 타입(실수 타입)
    # 부동 소수점은 3123.02 , 999.44 같은 것

    broadcast = '777' # '777'은 777과 다름!
    type(broadcast) # str 타입
    print(broadcast + 1) # 문자열(str)과 int를 더한 것이므로 오류

    seoul = int(broadcast)
    type(seoul) # int 타입
    print(seoul + 111) # int 타입 간 연산이기 때문에 오류 발생하지 않는다. 888로 출력됨

    #입력을 해보기
    nm = input('Who are you? ') #Who are you? 라고 물어 볼 것이고 사용자는 입력값을 넣습니다.
    print('Welcome', nm) # 해당 입력값을 nm이라는 변수에 할당한 다음 Welcome이라는 문자열과 함께 출력합니다. ex) sunny를 치면 Welcome sunny라고 나옴

    # #은 주석임 java의 //와 같음
  ```


  ```Python
  # 연습해보기
  nm = input('what`s your name?')
  print("hello", nm)

  hourxh = input(" enter hours: ")
  ratexr = input(" enter rate: ")
  payxp = float(hourxh) * float(ratexr)
  print(" pay:", payxp)
  # 시간과 금액을 적으면 합당한 임금이 나옴
  # 예를 들어 시간이 60 요금이 10000이면 600000원이 나옴.

  a = 22 % 7
  print(a) # 1이 나옴
  ```

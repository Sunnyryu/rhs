## 파이썬 기초 정리 5


#### nice Python

- 함수
  - 재사용 가능한 코드 조각을 함수라고 함!
- 파이썬에는 두종류의 함수가 존재
  - 내장함수
    - 파이썬의 한부분으로 제공
      - ex) print(), input(), type 등
      - 새로운 예약어라고 생각 / 변수명 사용 X
  - 우리가 정의하고 사용하고 있는 함수

- 함수
  - 함수는 인자를 입력 받고, 계산도 하고 결과를 반환하는 재사용 가능한 코드
  - 정의할 때 def 예약어 이용
  - 함수이름, 괄호, 인자 이용 함수 호출
    - ex) big = max('Hi wall')
    - print(big) = > w
    - small = min('Hi wall')
    - print(small) => 공백을 출력함 공백없이 하면 H출력
- max 함수
  - 함수는 우리가 사용할 저장된 코드임
  - 함수는 입력값을 받아서 출력값을 생산
- 자료형 변환
  - 정수형과 실수형을 표현식에 동시에 사용할 때 정수는 암시적으로 실수형으로 변환됨
  - 내장 함수인 int()과 float()을 이용해 조정 가능
```Python
print(float(55)/100)
#0.55
i = 33
type(i)
#class 'int'
f = float(i)
print(f)
#33.0
type(f)
#class 'float'
print(5 + 4 * float(3) / 2 - 1)
#10.0
```

- 문자열 변환
  - int()와 float()를 문자열에서 정수형으로 변환할 때도 사용할 수 있음
  - 문자열이 숫자를 포함하지 않으면 에러
```Python

abc = '123'
type(abc)
#class 'str'
print(abc +1)
# error int+str !
def = int(abc)
#class int
print(def + 1)
124
ghi = 'hi sunny'
mno = 'int(ghi)'
# error 문자를 int화 하려고함
```

- def 키워드, 괄호, 매개 변수를 적어서 새로운 함수를 만들 수 있음
  - 함수 본문은 들여쓰기를 해야함.
  - 함수의 본문을 실행하지는 않음
- 정의와 사용
  - 함수를 한 번 정의하면, 원하는 만큼 호출(또는 실행) 가능
  - 저장과 재사용 패턴
- 인자
  - 함수를 호출 할 때 입력값으로 전달하는 값
  - 함수가 다른 조건에서 호출 되었을 때 각각 다른 일을
    수행할 수 있도록 지시하는 역할
  -  함수 이름 다음의 괄호 안에 씀
- 매개변수
  함수 정의에 사용되는 변수 / 특정함수 호출에서 함수 안의 코드가 인자에 접근하기 위한 손잡이 역할
- 반환값
  - 함수는 종종 인자를 받아서 계산을 하고 함수 호출 구문이 사용할 수 있도록 값을 반환. 이를 위해 return 키워드를 사용
```Python

def greet(lang):
if lang == 'sks':
return 'Hola'
elif lang == 'dkd':
return 'Bonjour'
else:
return 'Hello'
>>> print(greet('aka'),'Glenn')
Hello Glenn
>>> print(greet('sks'),'Sally')
Hola Sally
>>> print(greet('dkd'),'Michael')
Bonjour Michael
>>>

big = max('Hello Sunny')
print(big)
w
# 'Hello Sunny' - 인자
# def(inp)가 있다면 inp가 매개변수 / w 가 결과

#함수 정의에서 한 개 이상의 매개 변수를 정의할 수 있음
#단순히 함수를 호출 할 때 인자를 추가
#숫자는 인자의 순서에 따라 매개변수와 매칭
```

- void (non-fruitful) 함수
  - 함수가 값을 반환하지 않으면, “void” 함수라고 함
  - 값을 반환하는 함수를 “fruitful” 함수라고 함
  - Void 함수는 “not fruitful” 함수
```
함수를 쓰느냐 마느냐?
코드를 한 “문단”으로 정리 - 완전한 아이디어를 저장해두고
“명명”
번복하지 말기 - 한 번에 작동하도록 만들어서 재사용
코드가 너무 길어지거나 복잡해지면, 논리 상 나누어서 각 조각을
함수 안에 집어 넣어넣기
일반적으로 자주 사용 하는 것은 라이브러리화 - 동료와 공유해도
좋음
```

```Python
# ex) Enter Hour : 50 / Enter Rate : 15
def computepay(hour, rate):
  if hour > 40 :
    commonpay = rate * hour
    overtimepay = (hour-40.0) * (rate * 0.5)
    pay = commonpay + overtimepay
  else :
    pay = hour * rate
    return pay

inputhour = input("Enter Hour")
inputrate = input("Enter Rate")
floathour = float(inputhour)
floatrate = float(inputrate)

compay = computepay(floathour, floatrate)

print("Pay: ", compay)
```



```

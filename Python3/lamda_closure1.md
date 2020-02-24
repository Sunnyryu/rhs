## lamda 2

```
lambda 매개변수1, 매개변수2: 반환값                    # 람다 표현식으로 함수를 만듦
(lambda 매개변수1, 매개변수2: 반환값)(인수1, 인수2)    # 람다 표현식 자체를 호출
 
lambda 매개변수1, 매개변수2: 식1 if 조건식 else 식2    # 람다 표현식에서 조건부 표현식 사용
lambda x: str(x) if x % 3 == 0 else x
 
lambda 매개변수1, 매개변수2: 식1 if 조건식1 else 식2 if 조건식2 else 식3  # if를 여러 개 사용
lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10

x = 10    # 전역 변수
 
def foo():
    global x   # 전역 변수 x를 사용하겠다고 설정
    y = 10     # foo의 지역 변수

def 함수이름1():
    코드
    def 함수이름2():
        코드

def A():
    x = 10        # A의 지역 변수 x
    def B():
        nonlocal x    # 현재 함수에서 바깥쪽에 있는 지역 변수를 사용
        x = 20        # A의 지역 변수 x에 20 할당

def calc():    # calc 함수 안에 mul_add 함수를 만듦
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환
 
c = calc()    # c에 저장된 함수가 클로저
print(c(1), c(2), c(3), c(4), c(5))    # 8 11 14 17 20

def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환


```

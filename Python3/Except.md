## Rewind


```

try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드

try:
    실행할 코드
except 예외이름:            # 특정 예외가 발생했을 때만 처리 코드를 실행
    예외가 발생했을 때 처리하는 코드
 
try:
    실행할 코드
except 예외이름 as 변수:    # 발생한 예외의 에러 메시지가 변수에 들어감
    예외가 발생했을 때 처리하는 코드

try:
    raise Exception(에러메시지)    # 예외를 발생시킴
except Exception as e:             # 예외가 발생했을 때 실행됨
    print(e)                       # Exception에 지정한 에러 메시지가 e에 들어감

def 함수A():
    try:
        raise Exception(에러메시지)    # 예외를 발생시킴
    except Exception as e:             # 함수 안에서 예외를 처리함
        raise                          # raise만 사용하면 현재 예외를 다시 상위 코드 블록으로 넘김
 
try:
    함수A()
except Exception as e:                 # 하위 코드 블록에서 예외가 발생해도 실행됨
    print(e)

class 예외이름(Exception):    # 예외 만들기
    def __init__(self):
        super().__init__('에러메시지')
 
raise 예외                    # 예외 발생 시키기


이터레이터 = 반복가능한객체.__iter__()    # 반복가능한 객체에서 이터레이터를 얻음
이터레이터.__next__()                     # 반복 가능한 객체의 요소를 차례대로  꺼냄
 
이터레이터 = iter(반복가능한객체)         # iter 함수 사용
next(이터레이터)                          # next 함수 사용

class 이터레이터이름:
    def __iter__(self):
        return self
 
    def __next__(self):
        값 생성 코드, 반복을 끝내려면 StopIteration 예외를 발생시킴
 
이터레이터객체 = 이터레이터()    # 이터레이터 객체 생성
이터레이터.__next__()            # 이터레이터에서 값을 차례대로 꺼냄
next(이터레이터)                 # next 함수 사용
 
for i in 이터레이터():    # 이터레이터를 반복문에 사용
    pass

class 이터레이터이름:
    def __getitem__(self, index):
        인덱스에 해당하는 값을 반환하는 코드, 지정된 범위를 벗어났다면 IndexError 예외를 발생시킴
 
이터레이터객체 = 이터레이터()    # 이터레이터 객체 생성
이터레이터객체[인덱스]           # 인덱스로 접근

변수1, 변수2, 변수3 = 이터레이터()

def 제너레이터이름():     # 제너레이터 함수를 만듦
    yield 값              # yield로 값을 발생시킴
 
제너레이터객체 = 제너레이터()    # 제너레이터 객체 생성
제너레이터객체.__next__()        # __next__ 메서드를 호출하면 yield에 지정한 값이 반환값으로 나옴
next(제너레이터)                 # next 함수 사용
 
for i in 제너레이터():           # 제너레이터를 반복문에 사용
    pass

yield from 반복가능한객체
yield from 이터레이터
yield from 제너레이터객체

(식 for 변수 in 반복가능한객체)
(i for i in range(100))

def 코루틴이름():
    while True:
    변수 = (yield)    # 코루틴 바깥에서 값을 받아옴
 
코루틴객체 = 코루틴()
next(코루틴객체)          # 코루틴 안의 yield까지 코드 실행(최초 실행), __next__ 메서드도 같음
코루틴객체.send(값)       # 코루틴에 값을 보냄

def 코루틴이름():
    while True:
    변수 = (yield 변수)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
 
코루틴객체 = 코루틴()
변수 = next(코루틴객체)        # 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 반환
변수 = 코루틴객체.send(값)     # 코루틴에 값을 보내고 코루틴에서 나온 값 반환

def 코루틴이름():
    try:
        실행할 코드
    except GeneratorExit:    # 코루틴이 종료될 때 GeneratorExit 예외 발생
        예외가 발생했을 때 처리하는 코드
 
코루틴객체 = 코루틴()
next(코루틴객체)
코루틴객체.close()    # 코루틴 종료

def 코루틴이름():
    try:
        실행할 코드
    except 예외이름 as e:    # e에는 throw 메서드에 지정한 에러 메시지가 들어감
        yield 값             # except에서 yield에 지정한 값은 throw 메서드의 반환값으로 나옴
 
코루틴객체 = 코루틴()
next(코루틴객체)
코루틴객체.throw(예외이름, 에러메지시)    # 코루틴 안에 예외를 발생시킴

def 코루틴A():
    변수 = (yield)    # 코루틴 바깥에서 값을 받아옴
    return 값         # return으로 값을 반환, raise StopIteration(값)과 동작이 같음
 
def 코루틴B():
    변수 = yield from 코루틴A()    # 코루틴A의 반환값을 가져옴

```

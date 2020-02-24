## Python


### class

```

class 클래스이름:
    속성 = 값

class Person:
    bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)

['책', '열쇠']
['책', '열쇠']

클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유합니다.

class Person:
    def __init__(self):
        self.bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)

['책']
['열쇠']

즉, 인스턴스 속성은 인스턴스별로 독립되어 있으며 서로 영향을 주지 않습니다.

클래스 속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용

class Knight:
    __item_limit = 10    # 비공개 클래스 속성
 
    def print_item_limit(self):
        print(Knight.__item_limit)    # 클래스 안에서만 접근할 수 있음
 
 
x = Knight()
x.print_item_limit()    # 10

클래스 밖에서는 프린트 불가!!!

class 클래스이름:
    @staticmethod
    def 메서드(매개변수1, 매개변수2):
        코드

먼저 정적 메서드입니다. 정적 메서드는 다음과 같이 메서드 위에 @staticmethod를 붙입니다. 이때 정적 메서드는 매개변수에 self를 지정하지 않습니다.

@staticmethod처럼 앞에 @이 붙은 것을 데코레이터라고 하며 메서드(함수)에 추가 기능을 구현할 때 사용합니다. 데코레이터는 'Unit 42 데코레이터 사용하기'에서 자세히 설명하겠습니다.

그럼 간단하게 덧셈과 곱셈을 하는 클래스를 만들어보겠습니다.

class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출

Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출

이번에는 정적 메서드와 비슷하지만 약간의 차이점이 있는 클래스 메서드를 사용해보겠습니다.

클래스 메서드는 다음과 같이 메서드 위에 @classmethod를 붙입니다. 이때 클래스 메서드는 첫 번째 매개변수에 cls를 지정해야 합니다(cls는 class에서 따왔습니다).

class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
 
james = Person()
maria = Person()
 
Person.print_count()    # 2명 생성되었습니다.







```

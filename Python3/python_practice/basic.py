fruit = ["사과", "바나나", "레몬", "바나나", "딸기", "키위", "복숭아", "복숭아", "복숭아"]

bucket = {}

for f in fruit:
    if f in bucket:
        bucket[f] += 1
    else:
        bucket[f] = 1

print(bucket) #=> {'사과': 1, '바나나': 2, '레몬': 1, '딸기': 1, '키위': 1, '복숭아': 3}
# value가 추가 될 때 key도 같이 들어감!

from animal import dog
from animal import cat

d = dog.Dog() #instance
d.hi()

c = cat.Cat()
c.hi()

from animal import *

d = Dog()
c = Cat()

d.hi()
c.hi()

x = 222
y = 333
z = 444

if x > y:
    print("x가 더커!")
else:
    print("x가 더 작어!")

for i in range(5):
    print(i)
    print("만세")

z = 0
while z < 10:
    print("김치찌개")
    z += 1

x = {}
y = {}

x[0] = "sunny"
x[1] = "jenny"
x[2] = "john"
x["age"] = 27

class ID:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self, to_name):
        print("안녕"+to_name+" 나는 "+ self.name)
    def introduce(self):
        print("내 이름은"+self.name+"그리고 나는"+str(self.age)+" 살이야")
# self는 만들어진 변수 활용시 쓰임!
class Firefighter(ID):
    def fire(self, to_fire):
        print("불이 났어, 나는 불을 끌테니, 너는 피해야해! "+to_fire)
class Pythondeveloper(ID):
    def python(self, to_python):
        print("파이썬으로 오늘은 뭘 만들어볼까?"+ to_python)

jinny = ID("지니", 28)
danny = ID("다니", 29)
john = Firefighter("존", 40)
john.fire("danny")
sunny = Pythondeveloper("써니", 27)
sunny.python("Django Framework")

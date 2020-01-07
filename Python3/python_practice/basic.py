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

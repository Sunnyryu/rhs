# animal package
# dog, cat modules
# dog, cat modules can say "hi"

from animal import Dog # animal 패키지에서 Dog라는 모듈을 가져와줘
from animal import Cat # ``에서 Cat이라는 모듈을 가져와줘용!

# from animal import * # animal package에서 갖고 있는 모든 모듈을 가져옴 !
d = dog.Dog() # instance화 시킴
d.hi()
c = cat.Cat()
c.hi()

# d = Dog()
# d.hi()
# c = Cat()
# c.hi()

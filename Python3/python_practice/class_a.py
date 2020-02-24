#class 클래스이름:
#    def __init__(self):
#self.속성 = 값
# self 자기 자신!! 
class Person():
    def __init__(self):
        self.hello = '안녕'

    def greeting(self):
        print(self.hello)

sunny = Person()
sunny.greeting()


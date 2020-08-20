class Person : #클래스는 함수와 변수들의 합이라고 생각하기!
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def sayhello(self, to_name) :
        print("hi!"+to_name+"I`m "+self.name)

    def myintroduce(self) :
        print("my name is " +self.name + " and i`m "+str(self.age)+" old") # self.age가 int 이기 떄문에 여기서는 str로 형변환을 한 후에 써야 +가 적용이 되용


    # def sayhello(self) :
        # print("hi!, I`m "+self.name)


#sunny = Person("Sunny") # init에 self와 name 만 있을 때 !!
#sunny.sayhello("Sunny")
#tony = Person("tony")
#tony.sayhello("tony")
#tomi = Person("tomi")
#tomi.sayhello("tomi")
#ray = Person("ray")
#ray.sayhello("ray")

#sunny.sayhello() # init 이 없이 sayhello에 self만 넣고 받을 때에 위에 sunny = Person(Sunny)와 같이 쓰임
#tony.sayhello()
#tomi.sayhello()
#ray.sayhello()


sunny = Person("sunny", 26)
sunny.myintroduce()

class Police(Person) : # Police라는 클래스가 Person을 상속함 !
    def arrest(self, to_arrest) :
        print("you arrested " + to_arrest)
class Programmer(Person):
    def program(self, to_program) :
        print("next, i will be make that new program " + to_program)

sandy = Person("sandy", 22)
john = Police("john", 36)
kobe = Programmer("kobe", 27)

kobe.myintroduce() # Programmer가 Person을 상속하므로 Person에서 쓰이는 것을 이용할 수 있으므로 !! 사용가능
john.myintroduce()
john.arrest("sandy")
kobe.program("gcp")

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
 
maria = Person('sunny', 27, '인천')
maria.greeting()
 
print('이름:', maria.name)       
print('나이:', maria.age)        
print('주소:', maria.address)    

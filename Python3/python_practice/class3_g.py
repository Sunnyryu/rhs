class Animal:
    def eat(self):
        print('먹다')
 
class Wing:
    def flap(self):
        print('파닥거리다')

class Bird(Animal, Wing):
    def fly(self):
        print('날다!')

sunny_bird = Bird()
sunny_bird.eat()
sunny_bird.flap()
sunny_bird.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))


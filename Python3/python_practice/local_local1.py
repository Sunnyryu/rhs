def hello():
    hello = 'hello, sunny!'
    def hello_message():
        print(hello,'a')
    hello_message() 

hello()

def A():
    x = 100
    def B():
        x = 200
    B()
    print(x)

A()

def C():
    x = 100
    def D():
        nonlocal x
        x = 200
    D()
    print(x)

C()



def chat(n1, n2, age) :
    print("%s: hello? how old are you?" % n1) #n1을 %s에 넣음
    print("%s: me? I`m %d" % (n2, age)) #n2를 %s에 넣고 %d에 age를 넣음

chat("annie", "sunny", 26)
chat("sunny", "annie", 30)


def sums(a, b) :
    result = a + b
    return result
    # print(result)

c = sums(2, 4)
print(c)
# print(result)로 나오면 none 으로 나오고 return result로 하면 2+4 = c가 되어 6이 출력됨


def hello(name, age) :
    if age < 20 :
        print("hello " + name)
    elif age >= 20 and age <= 49 :
        print("hello sir " + name)
    else :
        print("hello grandfather " + name)

hello("jenny", 19)
hello("sunny", 26)
hello("justin", 54)

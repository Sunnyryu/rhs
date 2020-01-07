## 파이썬 기초를 다시 한번 정리해보는 파일입니다.
### 머리에서 바로 바로 하나씩 나오지 않으면 반성하는 시간을 가져야 함!

```
x = 1 (x를 변수라고 함)

x라는 값에는 1이 정리가 되옵니다. => print(x) => 1 !!

y = "hello"
print(y) => hello

type은 숫자, 문자, boolean

x = 1
y = 2
z = 1.3
사칙연산은 모두 제공!!
**(제곱), %(나머지) )

x = "hello"
y = "bye"

z = """
안녕하세요
써니예유!
"""

print(z) => 안녕하세요 써니예유!

print("너 혹시 몇 살이야?" + 27) => 숫자와 문자는 더할 수 없어서 에러 발생!!
=> 이 떄는 27을 str(27)로 바꾸거나 "27"로 해서 문자열로 바꿔줌!

x = 3
y = "3"
print(str(x) + y) => "33"

boolean => 참 거짓으로만 나눔!

조건문

if / elif / else로 나눔

x = 100
if x > 101:
   "101보다 커"
else:
   "101보다 작어!"

a = 77
b = 78

if a % 2 == 0 or b % 2 == 0:
    print("a나 b 중에 하나는 짝수구나!")
else:
    print("둘다 짝수가 아니구나?")

함수

def chat():
   print("hi jenny")
   print("hi sunny")

chat()
chat()
chat()
chat()

chat 4번을 반복 할 수 있음!

def chat(name1, name2, age):
   print("%s: 안녕? 너는 몇살이양?" % name1)
   print("%s: 안녕 나는 %d?" % (name2,age))

 chat("써니","제니", 26)
 chat("조이","케니", 23)


def dsum(a, b):
    result= a + b
    return result

d = dsum(1,2)
print(d) => 3

e = dsum(99, 22)
print(e) => 121

def esum(a,b):
    result = a + b
    print(result)

f = esum(1,2)
print(f) => none <return 되는 것이 없음>

def introduce1(name, age):
    if age < 10:
        print("안녕" + name)
    elif age >= 10 and age < 20:
        print("안녕하세요," + name)
    else:
        print("안녕하십니까," + name)

introduce1("써니", 26)
introduce1("제니", 18)
introduce1("지니", 9)

반복문 (for, while)

for i in range(10):
    print("hi sunny")
    print("hi jenny")

10번 반복해서 나옵니다.(0부터 9) => 1부터 시작하는 언어가 있지만 python은 0부터 시작함!

a = 0
while a < 3:
    print("hi sunny")
    print("hi jenny")
    a += 1

while은 범위까지 반복시킴!! (0,1,2) => 총 3번

-> 개인적으로 while은 무한루프를 제외하곤 for이 더 편한거 같음!

k = 0
while True:
   print("배고파")
   print("나도")
   k += 1
   if k > 3:
       break

배고파 나도가 4번 반복하고 끝남!
(break는 루프를 끝내는 아이)
만약에 continue가 있다면 그 이후는 하지 않는 다는 뜻임!!

List

x = list()
y = []

x와 y는 같음 !! => list는 대괄호 인가?
list에는 숫자와 문자열 모두 들어갈 수 있음
list는 덧셈이 가능함!

x = [99, 98, 97, 96]
o = ["hello", "sunny"]
print(x[0]) => 99 (99, 98, 97, 96에서 99가 0번자리 96이 3번자리임 => 여기서도 인덱스는 0부터 시작)
x[3] = 100 => 96이 100으로 바뀜!!
리스트는 mutable => 바꿀수 있음!
len(x) => 개수를 알수 있음! 여기선 4임
y = sorted(x)
y => [96,97,98,99]
z = sum(x)
z => 99+98+97+96 => 390
k = x.append(95)
k => [99,98,97,96,95]

for n in x:
   print(x)

n에 x의 list 요소가 다 들어가게 됌! => 문자나 숫자 모두 마찬가지!!

print(x.index(96))
print(o.index("hello"))
=> 있다면 True 없다면 False

if "hello" in o:
    print("hello가 있지 말이예요!")

Tuple

x = tuple()
y = ()

x = (1,2,3)
y = ('sunny', 'jjang')
z = (1,2,'hello')

튜플도 더하는 것도 가능하고 있는 지 확인도 가능하고 자리수 확인도 가능함

print(x+y)
print('sunny' in y)
print(z.index(0))

tuple은 append가 안됨!

x[0] = 11 => 튜플은 만들어 놓은 것을 못바꿔서 에러가 남! (immutable)

dictionary

x = dict()
y = {}

x = { "name": sunny, "age": 27}

print(x["name"])
print(x["age"])

x = { 0:"sunny", 1: "hi", age: "27"}

print("age" in x)
print(0 in x) => True & False로 나오는데 있으면 True 없으면 False 이므로 여기엔 있으니까 True

for key in x:
    print("key" + str(key))
    print("value" + x[key])

key와 value를 보여줌!

x[0] = "써니" = > 바꿀 수 있음
x["school"] = "학점은행" => append도 가능함!!

class, object !
(함수와 변수들의 합이라고 띵킹 해야지유!)
오브젝트 => 인스턴스!

class Person:
#    name = "sunny"
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def hello(self, to_name):
        print("안녕! +to_name +" 나는" + self.name)
    def introduce(self):
        print("내 이름은 "+self.name+"그리고 나는"+str(self.age) + " 살이야")
self는 만들어진 변수를 활용할 때 쓰임!

p = Person()
p.hello()
sunny = Person("sunny")
jenny = Person("jenny")
denny = Person("denny")

sunny.hello("리키")
jenny.hello("토니")
denny.hello("페리")

class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포 되었음!"+ "to_arrest")

class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? 아 이걸 만들어야 겠다:" to_program)

sunny = Person("써니", 27)
jenny = Police("제니", 33) => Person을 상속해서 Person이 쓸 수 있는 것을 쓸수 있음!
Person이 없이 쓰려면 person에 있는 것을 넣어서 해야하는데 이것을 간편하게 person을 상속 받는 것으로 해결 가능!

jenny.introduce()
jenny.arrest("써니")
sun = Programmer("썬", 27)

sun.program("파이썬 서버")

```

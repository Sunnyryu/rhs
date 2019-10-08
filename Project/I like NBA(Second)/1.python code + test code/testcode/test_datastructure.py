# list = [], tuple = (), dictionary = {}
# List
x = [1,2,3,4]
y = ["hi", "teacher"]
z = ["hi",1,2,3]

print(x + y)
print(x[3])
x[3] = 19
print(x)
print(x[3])
num_es = len(x)
print(num_es)
x = [4,3,1,2]
num_es = sorted(x)
print(num_es)
z = sum(x)
print(z) # 10

for n in x :
    print(n)

for k in y :
    print(k)

print(x.index(3)) # 3이라는 요소가 몇 번째 위치에 있는 지 가르쳐줌
print(y.index("hi")) # hi가 어디에 몇 번째 위치에 있는 지 알려줌
print("hi" in y) # hi가 y에 있으면 True 없으면 False

if "hi" in y :
    print("y have hi")
# list는 mutable
# Tuple

x = (1,2,3)
y = ('s', 'o', 'n')
z = (1,'b','a','n',2)

print(x+y)
print('s' in y)
print(z.index(2))
# x[0] = 10 # error 발생 - 튜플은 오소에 있는 것을 못바꿈 !!!!! / mutable vs immutable => immutable function = tuple

# dictionary

x = dict()
y = {}
x = {
    0 : "god sunny",
    "name" : "sunny",
    "age" : 26,
}
print(x[0])
print(x["name"])
print(x["age"])
print("0" in x)
print(x.keys()) #dictionary의 키를 출력함
print(x.values()) # ditionary의 value 출력

for key in x :
    print(key)
    print(x[key])

x[0] = "eddy"
print(x)

x["school"] = "korea"
print(x)
# 딕셔너리는 값을 바꾸거나 추가할 수 있음

# [1, 2, 3, 4, 'hi', 'teacher']
#4
#[1, 2, 3, 19]
#19
#4
#[1, 2, 3, 4]
#10
#4
#3
#1
#2
#hi
#teacher
#1
#0
#True
#y have hi
#(1, 2, 3, 's', 'o', 'n')
#True
#4
#god sunny
#sunny
#26
#False
#dict_keys([0, 'name', 'age'])
#dict_values(['god sunny', 'sunny', 26])
#0
#god sunny
#name
#sunny
#age
#26
#{0: 'eddy', 'name': 'sunny', 'age': 26}
#{0: 'eddy', 'name': 'sunny', 'age': 26, 'school': 'korea'}

fruit = ["grape", "banana", "apple", "grape", "strawberry", "banana", "strawberry", "peach", "peach", "mango", "apple", "banana", "grape"]

b = {}

for f in fruit :

    print(f)
    if f in b : # b에 해당하는 값이 있다면?
        b[f] = b[f] + 1 # 해당 식으로 품
    else : # 만약 없다면 ?
        b[f] = 1 # 그 것을 1로 바꿔줌 !

print(b)

## Rewind2

#### Python

```python

# 파이썬 스타일 코드 => 파이썬 스타일의 코드 작성 기법 !

colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)
#redbluegreenyellow

# 인간의 시간이 컴퓨터의 시간이 중요하다는 개념 때문에 파이썬 스타일 코드를 사용함 / split(0, join(), 리스트 컴프리헨션, enumerate(), zip() 이나 map(), reduce() 등을 사용함 !!)

# 문자열의 분리 및 결합 

# 문자열 분리 split() !! 
a = '김치,라면,사랑'
a.split(",")
['김치','라면','사랑']
# , 단위로 나눈 다는 것임 , 없으면 공백 단위로 나눔!

b = 'abc.def.gh'
c,d,f = b.split('.')
print(c,d,f)
# abc def gh 

# 문자열의 결합 join()

result = '-'.join(colors)
# 'red-blue-green-yellow'

#  리스트 컴프리헨션 
result = []
for i in range(10):
    result.append(i)


result = [i for i in range(10)]
# for i in range에서 i를 뽑아내는 식 !

result = [i for i in range(10) if i % 2 == 0]
result
# [0,2,4,6,8] 
result = [i if i% 2 == 0 else 10 for i in range(10)]
# [0, 10, 2, 10,4, 10,6, 10,8, 10]
#if else문을 쓰는 경우 for 문 보다 앞에서 쓴후 i가 받는 형식으로 할 수 있다 ! 
# 중첩 반복문의 경우 [i+j for i in a for j in b] 이런식으로 사용하면 됩니다.
# 중첩 반복문에서 필터를 을 쓰고 싶다면 ㅂ반복문 끝에 if문을 사용하면 되옵니다! 
# 이차원 리스트 
words = 'i like you and i always gain the your smile'.split()
print(words)
# ['i','like','you','and','i','always','gain','the','your','smile']
gain = [[w.upper(), w.lower(), len(w)] for w in words]
#[['I', 'i', 1], ['LIKE', 'like', 4], ['YOU', 'you', 3], ['AND', 'and', 3], ['I', 'i', 1], ['ALWAYS', 'always', 6], ['GAIN', 'gain', 4], ['THE', 'the', 3], ['YOUR', 'your', 4], ['SMILE', 'smile', 5]]
for i in gain:
    print(i)
#['I', 'i', 1]
#['LIKE', 'like', 4]
#['YOU', 'you', 3]
#['AND', 'and', 3]
#['I', 'i', 1]
#['ALWAYS', 'always', 6]
#['GAIN', 'gain', 4]
#['THE', 'the', 3]
#['YOUR', 'your', 4]
#['SMILE', 'smile', 5]

iteration_max = 10000

vector = list(range(iteration_max))
scalar = 2

for _ in range(iteration_max):
    [scalar * value for value in range(iteration_max)]


#enumerate() 리스트 값에 인덱스를 붙여 출력 ! / 리스트의 값을 추출 시 인덱스를 붙여 함께 출력하는 방법 !! 
for i,v in enumerate(['a','b','c']):
    print(i,v)

0 a
1 b
2 c  

# zip 리스트 값을 병렬로 묶어 출력 
a = [1,2,3]
b = [4,5,6]
for x,y in zip(a,b):
    print(x,y)
#1 4
#2 5
#3 6
a,b,c = zip((9,8,7),(6,5,4),(3,2,1))
print(a,b,c)
# (9, 6, 3) (8, 5, 2) (7, 4, 1)
[sum(x) for x in zip((9,8,7),(6,5,4),(3,2,1))]
#[18, 15, 12]

# 람다 함수 

# 람다 함수는 함수의 이름 없이 함수 처럼 사용할 수 있는 익명 함수 ! ㅇ
f = lambda x, y : x +y 
print(f(1,4)) # 5  
#print((lambda x: x +1 )(5))

## mapreduce / 빅데이터를 처리하기 위한 기본 알고리즘 

#map() 함수  - 연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용 / 리스트나 튜플처럼 요소가 있는 시퀀스 자료형에 사용된다. 사용 방법은 간단함 !!

a = [1,2,3,4,5]
f = lambda x:x ** 2 
print(list(map(f,a)))
#[1,4,9,16,25]

# 제네레이터의 사용 / 제너레이터가 생겼기에 반드시 list 같은 것을 .. 사용해야함 !!

# 리스트 컴프리헨션과의 비교 
# 람다 함수나 map() 함수보다 리스트 컴프리헨션이 더 좋을 수 있음 
a = [1,2,3,4,5]
[x ** 2 for x in a]
# 1,4,9,16,25
# 한 개 이상의 시퀀스 자료형 데이터처리  / map() 함수의 또 다른 특징은 2개 이상의 시퀀스 자료형 데이터를 처리하는데 문제가 없음 
a = [1,2,3,4,5]
f = lambda x, y: x + y
list(map(f, a,a))
#[2,4,6,8,10]
[x + y for x,y in zip(a,a)]
# [2,4,6,8,10]

# 필터링 기능이 있음 -> else문을 반드시 작성해야함 !!
list(map(lambda x:x ** 2 if x % 2 == 0 else x, a))
#[1,4,3,16,5]

# reduce 함수 !! 
from functools import reduce
print(reduce(lambdax, y: x+y, [1,2,3,4,5]))
# 15 

# 별표의 사용 (아스트리크) => 곱하기 기호 ! 그런데.. 별표는 기본연산자지만.. 가변 인수 앞에서는 *를 붙인다느 것이다.
def asterisk_test(a, *args):
    print(a,args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)
# 1 (2,3,4,5,6)
# <class 'tuple'>

def asterisk_test2(a, **kargs):
    print(a,kargs)
    print(type(kargs))

asterisk_test2(1, b=2, c=3, d=4, e=5, f=6)
#1 {'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
# <class 'dict">

# 별표의 언패킹 기능  - 함수에서 별표는 변수 앞에 붙어 여러 개의 변수를 한 번에 넣을 수 있는 컨테이너 역할을 하고 리스트 , 튜플 ,딕셔너리와 같은 자료형에서 언패킹 해주는 역할을 함 !!

def asterisk_test(a, *args):
    print(a,*args)
    print(type(args))

asterisk_test(1,(2,3,4,5,6))
# 1 (2, 3, 4, 5, 6)


def asterisk_test(a, *args):
    print(a,*args)
    print(type(args))

asterisk_test(1,*(2,3,4,5,6))
# 1 2 3 4 5 6

data = ([1,2],[3,4],[5,6])
print(*data)
#[1, 2] [3, 4] [5, 6]

def asterisk_test(a,b,c,d):
    print(a,b,c,d)

data ={"b":1, "c":2, "d":3}
asterisk_test(10,**data)
# 10 1 2 3 

# 선형 대수학 

# 벡터 ( 크기와 방향을 가지는 거)
# R^n 으로 사용 됨!

#행렬 - 1개 이상의 벡터 모임 ! / 행 또는 열은 하나의 대상에 대한 정보를 표현 

# 파이썬 스타일 코드로 표현한 벡터 
vector_a = [1,2,10]
vector_b = (1,2,10)
vector_c = {'x':1, 'y':1, 'z':10}

u = [2,2]
v = [2,3]
z = [3,5]
result = [sum(t) for t in zip(u,v,z)]
# [(2,2,3),(2,3,5)]
print(result)
# [7, 10]
# 개수가 많아지면 위의 함수에서 *args를 이용하면 매우 좋음 그러면 개수가 많아지더라도 충분히 이지하게 할 수 있음 ! 
def vector_addition(*args):
    return [sum(t) for t in zip(*args)]
vector_addition(u,v,z,k,y)
# 15 20 

# 스칼라 벡터 값을 쓸경우 계산이 가능 !!

# 파이썬 스타일 코드 행렬 

m_a = [[3,6],[4,5]]
m_b = [(3,6), (4,5)]
m_c = {(0,0):3, (0,1):6 , (1,0):4, (1,1):5}
m_d = [[5,8],[6,7]]
result = [[sum(row) for row in zip(*t)] for t in zip(m_a, m_d)]
print(result)
# [[8, 14], [10, 12]]
[t for t in zip(m_a, m_d)]
# [([3, 6], [5, 8]), ([4, 5], [6, 7])]

#  전치 행렬 

m_a = [[1,2,3], [4,5,6]]
result = [[element for element in t] for t in zip(*m_a)]
result
# [[1, 4], [2, 5], [3, 6]]
[t for t in zip(*m_a)]
# [(1, 4), (2, 5), (3, 6)]

new_m_a = [[1,1,2], [2,1,1]]
new_m_b = [[1,1],[2,1],[1,3]]
result = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*new_m_b)] for row_a in new_m_a]
result
# [[5, 8], [5, 6]]
#처음에 for row_a in matrix_a에서 행 값이 뽑히고 for column_b in zip(*new_m_b)에서는 열의 값이 뽑힘 .. 다음으로 sum(a *  b for a,b in zip(row_a, column_b))를 통해서 인덱스 값을 뽑고 합을 구할 수 있음 !!


```

## 파이썬 기초 정리 10


#### enjoy Python (revision for error)

튜플
  - 튜플은 리스트와 비슷한 기능을 하는 시퀀스 / 0부터 시작하는 인덱스에 항목을 저장

```python
x = ('sunny', 'kenny', 'jenny')
print(x[1])
>>> kenny
y = (1,2,3)
print(y)
>>> (1,2,3)
print(max(y))
>>> 3
for p in y :
  print(p)

1
2
3
```

  - 튜플은 리스트와 다르게 저장된 내용을 변경 불가 !!
  - 튜플은 sort(), append(), reverse() 불가능
```Python
>>> l = list()
>>> dir(l)
['append', 'count', 'extend', 'index', 'insert', 'pop',
'remove', 'reverse', 'sort']
>>> t = tuple()
>>> dir(t)
['count', 'index']
```

  - 튜플의 장점
  파이썬은 튜플을 수정 가능하지 않게 저장하기 때문에 리스트와 비교하여 메모리 사용량과 성능 측면에서 훨씬 단순하고 효과적
  그러므로, 임시 변수를 선언할 때는 리스트를 쓰는 것보다 튜플을 쓰는 것이 좋음

  - 튜플의 선언
    - 튜플을 좌변에 놓는 것으로 선언문에서 사용 가능
    - 괄호는 생략 가능
```python
>>> (x, y) = (9, 'sunny')
>>> print(y)
sunny
>>> (a, b) = (99, 11)
>>> print(a)
99
```

튜플과 딕셔너리
  - 딕셔너리의 items(), 메소드는 (키, 값)를 튜플의 형태로 리턴

```Python
>>> d = dict()
>>> d['sunny'] = 2
>>> d['hunny'] = 4
>>> for (k,v) in d.items():
        print(k, v) #key , value
sunny 2
hunny 4
>>> tups = d.items()
>>> print(tups)
dict_items([('sunny', 2), ('hunny', 4)])
```

- 튜플의 비교
    - 튜플에서 다른 시퀀스와 비교 연산자를 사용할 수 있음. 만약 첫번째 요소가 같다면, 파이썬은 다음 요소를 비교하고, 다른 요소가 있을 때까지 비교를 계속함
```Python
>>> (3, 1, 2) < (5, 1, 2)
True
>>> (0, 2, 2000000) < (0, 6, 1)
True
>>> ( 'Jones', 'Say' ) < ('Jones', 'Sunny')
True
>>> ( 'Sunny', 'Sam') > ('Adams', 'Sam')
True
```

 - Tuple로 된 Lists의 Sorting
   - 딕셔너리를 정렬 하기 위해 튜플로 이루어진 리스트를 사용할 수 있음
   - items() 메소드를 통해 키와 값를 얻은 후 sorted() 메소드로 딕셔너리를 정렬하면 !!
```python
>>> tp = {'a':44, 'b':66, 'c':88}
>>> tp.items()
dict_items([('a', 44), ('b', 66), ('c', 88)])
>>> sorted(tp.items())
[('a', 44), ('b', 66), ('c', 88)]
```

  - sorted 함수
    - 내장된 sorted 메소드는 시퀀스를 인자로 받아 정렬된 시퀀스를 리턴. 활용도가 높고 편리

```Python
>>> st = {'a':10, 'b':11, 'c':12}
>>> t = sorted(d.items())
>>> t
[('a', 10), ('b', 11), ('c', 12)]
>>> for k, v in sorted(st.items()):
... print(k, v)
...
a 10
b 11
c 12
```

  - 값을 이용한 정렬
    - (키, 값) 형태의 튜플로 이루어진 리스트를 만들면 값를 기준으로 정렬할 수 있듬!
    - for 반복문를 사용하여 튜플로 이루어진 리스트를 만들 수 있음!
```Python
>>> li = {'a':33, 'b':11, 'c':22}
>>> tmp = list()
>>> for k, v in li.items() :
... tmp.append( (v, k) )
...
>>> print(tmp)
[(33, 'a'), (11, 'b'), (22, 'c')]
>>> tmp = sorted(tmp, reverse=True)
>>> print(tmp)
[(33, 'a'), (22, 'c'), (11, 'b')]
```

  - 가장 많이 쓰이는 단어 열 개 찾기
```Python
fhand = open('abc.txt')
counts = {}
for line in fhand:
 words = line.split()
 for word in words:
 counts[word] = counts.get(word, 0 ) + 1

lst = []
for key, val in counts.items():
newtup = (val, key)
 lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
 print(key, val)
```

 - 리스트 컴프리헨션
```python
lc = {'a' : 55, 'b' : 5555, 'c' : 555}
print( sorted( [ (v,k) for k,v in lc.items() ] ) )
# 리스트 컴프리헨션은 동적인 리스트를 생성. 이 경우 역으로 이루어진 튜플로 리스트가 만들어지고 정렬.
 ```

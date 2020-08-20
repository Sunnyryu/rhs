## lamda

```
람다 표현식: 식 형태로 되어있음!

ex: def a(x):
        return x + 1
a(1)
2

a = lambda x: x + 1
a(1)
2

(lambda x: x + 1)(1)

list(map(lambda x: x+1, [1,2,3])
[2,3,4]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))
[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]
list(map(lambda x, y: x * y, a,b))
[2, 12, 30, 56, 90]

def f(x):
    return x > 5 and x<10

a = [11,0,9,1,7,15,10,2,3,8]
list(filter(f,a))
[9,7,8]

list[filter(lambda x: x>5 and x<10, a)]

def f(x,y):
    return x + y
a = [1,2,3,4,5]

from functiools import reduce
reduce(f,a)
15


```

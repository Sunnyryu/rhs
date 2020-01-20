## Python Rewind2 

#### Python !

```python
#input 함수 

enter_name = input("what`s your name?")

print_name = print("name")

celsius = input()
fahrenheit = (float(celsius)*1.8)+32

print(celsius, fahrenheit)

colors_list = ['red', 'blue', 'green']

# color[0] = red, [1] = blue [2] = green / len(colors_list) => 3

fruits = ['사과','자몽', '키위', '참외', '수박', '배', '바나나']

# fruits[0:3] => ['사과','자몽','키위'] , fruits[5:] => ['배', '바나나'], fruits[-7:-3] => ['사과','자몽','키위','참외']
# fruits[::2] => ['사과','키위','수박','바나나'] => 변수명[시작 인덱스:마지막 인덱스: 증가값]

#list 연산 
color_1 = ['yellow','pink']
color_2 = ['green', 'blue']
print(color_1+color_2) # ['yellow','pink','green','blue']
len(color_1+color_2) # 4

# 곱하기 2면 반복 2회 !!
# 'yellow' in color_1 => 있다면 True 없으면 False

# 리스트 추가는 append / extend / insert 가 쓰임 !

# append는 리스트 맨 뒤에 새로운 값을 추가 가능하며 extend는 리스트의 덧셈 연산과 같음, insert는 특정 위치에 값을 추가할 수 있음 !

fruits_1 = ['banana', 'apple', 'orange', 'peach']
fruits_1.append('strawberry')

print(fruits_1) # ['banana', 'apple', 'orange', 'peach','strawberry']

Ham = ['bulgogi', 'chicken', 'beef']
Ham.extend(['rice', 'bacon'])

print(Ham) => ['bulgogi', 'chicken', 'beef', 'rice', 'bacon']

ramen = ['samyang', 'jin', 'shin']
ramen.insert(0, 'ggoggo')
print(ramen) # ['ggoggo', 'samyang', 'jin', 'shin']

#리스트 제거는 remove , del

ramen.remove('ggoggo')
print(ramen) #['samyang', 'jin', 'shin']
ramen[0] = 'nuguri'
del ramen[2] 
print(ramen) # ['nuguri', 'jin']


t = [1,2,3]

a,b,c = t 
print(t,a,b,c) #[1,2,3] 1 2 3 

# 이차원 리스트 

a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [100,200,300,400,500]

abc = [a,b,c]
print(abc) # [[1,2,3,4,5], [6,7,8,9,10], [100,200,300,400,500]]
print(abc[0][2]) # 3  

#= == 값 비교 is는 메모리 주소 비교  / 리스트 안에 리스트를 입력 가능 !!
print(a,b) #[1,2,3,4,5][6,7,8,9,10]
```

```python

```

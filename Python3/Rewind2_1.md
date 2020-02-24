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
#조건문 (조건에 따라 특정 동작을 하도록 하며, if문을 사용함 !)
#if <조건>:
#   <명령 1>
#   <명령 2>
#else:
#   <명령 1>
#   <명령 2>
age = int(input())
if age < 30:
    print("30 이상")
else:
    print('30 이하")

# x<y / x>y / x == y / x is y (메모리 주소가 같은 지), x !=y , x is not y (메모리 주소가 같지 않은 지), x>= y , x <=y 

# and / or / not 

#if  / elif / else 문 !

year = int(input('what`s your age'))
age = (2020 - year + 1)
if age <= 26 and age >= 20:
    print('대학생')
elif age < 20 and age >= 17:
    print('고등학생')
elif age < 17 or age => 14:
    print('중학생')
elif age < 14 or age => 8:
    print('초등학생')
else:
    print('학생 x')

# 반복문 ( loop / for이나 while 이 쓰임 )

# for - 기본적인 반복문으로 반복 범위를 지정하여 반복 수행 
for loop_1 in range(0,5):
    print('hi')
# hi 
# hi 
# hi 
# hi 
# hi 
# hi 
# for 변수 in range(시작번호, 마지막번호, 증가값 )

for loop_2 in '가나다라마':
     print(loop_2)
#가
#나
#다
#라
#마
for loop_3 in ['banana', 'apple', 'peach']:
    print(loop_3)

#banana
#apple 
#peach 

for loop_4 in range(10, 1, -2):
    print(i)
# 10
# 8
# 6
# 4
# 2 

#while 문 / 어떤 조건이 만족하는 동안 명령 블록 수행 / 거짓시 반복 명령문 수행 x 

a = 1
while a < 3:
    print(a)
    a += 1
# 1 
# 2

# 반복문의 제어 
# break (논리적으로 반복 종료 가능 )
for i in range(10):
     if i == 3:
         break
     print(i)
print("end")
# 0
# 1
# 2
# end 

# continue 문 
for i in range(5):
     if i == 3:
         continue
     print(i)
print("end")
# 0
# 1
# 2
# 4
# end  

# 반복문에서 else문 => 어떤 조건이 완전히 끝났을 때 한번더 실행시ㅕ주는 역할을 함 ! break 가 되고 else를 쓰면 else문은 생략되니 확인하기 위한 코드임 !
for i in range(5):
    print(i)
else:
   print('end')
# 0
# 1
# 2
# 3
# 4
# end

sentence = "hello sunny"
reverse_sentence = ''
for ala in sentence:
    reverse_sentence = ala + reverse_sentence

print(reverse_sentence)
# ynnus olleh

decimal = 10
result = ''
while (decimal >0):
    reminder =decimal % 2
    decimal = decimal // 2 
    result = str(reminder) + result
    print(result)


print(result)
# 1010
# 0
# 10
# 010
# 1010 

import random

solve_number = random.randint(1,100)
user_input = int(input('값 선택 1~ 100 까지'))
while (user_input is not solve_number):
    if user_input > solve_number:
        print('너무커')
    else:
        print('너무 작아')
    user_input = int(input('새로운 수'))


else:
   print('정답')
```

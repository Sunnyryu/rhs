## 파이썬 기초 정리 3


#### fighting Python

- 조건문
```Python
# ex)
x = 9
if x < 10 : # if는 예약어이며, 컴퓨터는 if 다음에 나오는 조건문의 True, False를 판단함.
  print('Smaller') #만약 True인 경우 :(콜론) 아래로 들여쓰기 된 부분을 실행함.
                       #여기서는 Smaller가 출력됨.
# if 뒤에 :(콜론) 꼭 써줘야함

#비교연산자에 대해서도 소개하자면 ,
# x>y - x가 y보다 큼, 만약 아니라면 false
# x<y - x가 y보다 작음, 만약 아니라면 false
# x>=y // x<=y - x가 y보다 크거나 같음과 x가 y보다 작거나 같음, 아니라면 false
# == , != / ==은 같은 경우에 쓰이고 !=은 다른 경우에 쓰임, 아니라면 false

#들여쓰기
#ex)
x = 7
if x < 10:
print('small')  #print가 들여쓰기 되지 않아 에러발생... 들여쓰기 안지키면 에러뜨니 주의!

#ex)
x = 17

if x < 15 :
    print('small')
else :
    print('big')
#여기서는 17가 15보다 크니까 if가 아닌 else로 쓰임, 따라서 big으로 출력함.
#ex)

x = 100

if x < 10 :
    print('E')
elif x < 30 :
    print('D')
elif x < 50 :
    print('C')
elif x < 70 :
    print('B')
elif x < 90 :
    print('A')
else :
    print('MASTER')

# MASTER가 출력될 것임 그리고 만약에 x<70과 x<90이 반대로 되어있다면 Large는 절대 볼수 없으니 주의할 것!
```
- try / except
  - 에러를 대처하기 위한 좋은 예약어
```Python
kkk = "999"

try:
    print("Hello")
    kkkInt = int(kkk)
    print("World")
except:
    kkkInt = "Integer로 변환할 수 없습니다."

print('Done', kkkInt)
# Hello
# World
# Done 999이 순서대로 출력됩니다.
# 올바른 값이 아니라면 에러가 발생하는데 except를 코드에 넣으면 해당 문구가 나옴
```

```Python
# ex)
sh = input("enter hours: ") # 시간 입력
sr = input("enter rate: ") 	# 요금 입력
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input") # 에러 발생을 예방하기 위함
    quit() # 끝내는 예약어

print(fh, fr)
if fh > 40 : #40시간이 넘은 경우 초과수당을 받을 때 사용함.
    reg = fr * fh
    otp = (fh- 40.0) * (fr * 0.5)
    xp = reg + otp
else: # 40이 안된다면 else로 적용되어 식이 계산될 것임.
    xp = fh * fr
print("Pay:", xp)

#ex2)
score = input("Enter Score: ") # 점수 입력

try:
    score = float(score)
except:
    print("Error, please enter numeric input") # 애러 대비 except
    quit()

if score > 1.0 :
    print("that`s out of range.") #1.0보다 크면 학점을 평가할 수 없음.
elif score >= 0.9 :
    print("A")
elif score >= 0.8 :
    print("B")
elif score >= 0.7 :
    print("C")
elif score >= 0.6 :
    print("D")
else:
    print("F") #0.6보다 낮으면 무조건 f임..
```

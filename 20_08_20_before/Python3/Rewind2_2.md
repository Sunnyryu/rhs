##Python

#### Rewind2_2

```Python

# 함수  - 어떤 일을 수행하는 덩어리, 또는 코드의 묶음이라고 표현할 수 있음 / 도형의 넓이를 구하는 프로그램에서 사각형의 넓이를 구하는 과업이라고 생각하자 !

# def 함수 이름 (변수1 ...):
#     수행문1
#     수행문2
#     return(반환값)

# ex1)
def a(x,y):
    return x * y

def a_1(x,y):
    return x*y 
a_x = 10
a_y = 20
print('x:',a_x)
print('y:',a_y)
print('넓이:',a_1(a_x, a_y))

# ex2)

def f(x):
    return 2 * x + 3
def g(x):
    return x ** 2
x = 2
print(f(x)+ g(x) + f(g(x)) + g(f(x)))
# 71 

# 함수의 형태 
# 반환값 있음 - 매개변수 있음 => 매개변수를 없이 수행문을 수행 -> 결과값 반환 
# 반환값 있음 - 매개변수 없음 => 매개변수 없이 수행문 수행 -> 결과값 반환
# 반환값 없음 - 매개변수 있음 -> 매개변수 사용하여 수행문만 수행 
# 반환값 없음 - 매개변수 없음 -> 함수안 수행문만 수행 

# 값에 의한 호출 => 함수에 인수를 넘길 때 값만 넘김 / 함수 안의 인수값 변경 시, 호출 된 변수에 영향을 주지 않음 
# 참조 호출 => 함수에 인수를 넘길 때 메모리 주소를 넘김 / 함수 안의 인수값 변경 시 , 호출 된 변수 값도 변경 !

# 변수의 사용범위 -> 지역변수 : 함수 안에서만 사용 / 전역변수 - 프로그램 전체 사용 가능 !
#재구 ㅣ함수 = 함수가 자기 자신을 다시 부르는 함수 ! 

# 함수의 인수 - 키워드 함수 / 디폴트 인수 / 가변 인수 / 키워드 가변 인수 

# 키워드 인수 = 함수에 입력되는 매개변수의 변수명을 사용하여 함수의 인수 지정 ! 

#  디폴트 인수 = 매개변수에 기본값을 지정하여 사용 !/ 아무런 인수를 넘기지 않으면 지정된 기본 값을 주는 경우 !
#  가변 인수 - *(아스터리스크)라고 하며 가변인수로 만들어준다고 함 / 함수의 인터페이스에 지정된 변수 이외에 추가 변수를 함수에 입력하게끔 지원 ! *args 

# z키워드 가변 변수  가변 인수는 변수의 순서대로 튜플 형태로 지정 .. 변수의 이름을 지정할 수 없는 단점이 있어 키워드 가변 인수로 대체 .. 매개 변수의 이름을 따로 지정하지 않고 입력하는 방법으로 .. *를 2개 사용하여, 함수의 매개변수 사용 / 
#  입력된 값은 딕셔너리 자료형으로 사용할 수 있음 !!  

# 들여쓰기는 4 스페이스 / 한 줄은 최대 79자 / 불필요한 공백은 피함 

# 함수 이름은 가능하난 짧게 작성 / 함수의 역할 의도 드러낼것 / 공통으로 사용되는 코드를 함수로 변환할 때 / 복잡한 로직이 사용되었을 때 식별가능한 이름의 함수로 변환 시 사용 !

#  .isdigit() => 문자열이 숫자이면 True 아니면 false / .isalaph() => 문자열이 문자이면 True 아니면 False


# 문자열 

# 어플리케이션을 만들거나 데이터를 분석할 때 매우 중요하게 다루는 자료형 중 하나이며, 시퀸스 자료형 (리스트와 같이 데이터를 순차적으로 메모리에 저장하는 형식의 데이터)

# sys를 사용하면 문자열의 메모리 크기를 알 수 있다 .. 

#  문자열의 인덱싱 

# hello 라는 단어가 있다면 h가 0 , o가 4가 되며 h가 -5 o가 -1이 된다.
# 문자열의 슬라이싱 

k = "king of fighter"
print(k[0:5])
#king (공백 하나 있음 )

#  문자열의 연산에서 *도 지원되는데 *2이면 2번 반복 이라고 생각하면 되옵니다.! (r그리고 문자열은 정수형과 덧셈 연산이 불가능!!)

# 문자열 함수 
#len() => 문자열의 문자 개수 반환 / upper() 대문자 변환 / lower() 소문좌 변환/ title() 첫번째 글자 대문자로 변환 / count('문자열') => 문자열이 몇개 들어있는지 확인 / find('문자열') =? 문자열이 왼쪽 끝부터 시작하여 몇번째에 있는지 반환 
# rfind('문자열') => 오른쪽 부터 몇번째에 있는 지 반환 / startswith('문자열') / endswith('문자열') => 문자열이 시작하는 지 여부 / 끝나는 여부 반환 / strip() , rstrip(), lstrip() => 좌우 공백 삭제/ 오른쪽 공백 삭제/ 왼쪽 공백 삭제
# split() =-> 문자열을 공백이나 다른 문자로 나누어 리스트로 반환 / isdigint() =? 문자열이 숫자인지 여부 반환 / islower() , isupper() => 문자열이 소문자인지 / 대문자인지 여부 반환 / isalpha()=> 문자열이 문자인지 여부 확인 

# 문자열 서식 지정 

# % / format 
print("%d %d %d" % (1,2,3)) #1 2 3 
print("{} {} {}".format("a","b","c")) # a b c 
print('%s %s' % ('abc', 'def')) # abc def
# %s 문자열 , %c 문자 1개 , %d 정수 , %f 실수 / %o 8진수 %x 16진수 / %% 문자 % 자체 

# "{자료형}".foormat(인수)
print("I`m sunny {0}. and i like {1}.".format(26,5)) # I`m sunny 26. and i like 5

# 패딩 - 여유공간을 지정하고 글자 배열을 맞추고 소수점 자리수를 맞추는 기능 

print("%10d" % 12) # 12가 나오면 10자리의 공간을 확복하고 우측정렬로 12를 출력하라는 것이며 -10d 면 좌측 정렬로 출력하라는 소리이다. 10.2f라면 10자리 확보 소수점 2째짜리 까지라는 것이다.

# format 에서는 <나 >로 사용해서 >는 우측정렬 , <는 좌측정렬인 것이다. 

# 자료구조의 이해 !

# 스택- 나중에 들어온 값을 먼저 나갈 수 있게 해주는 구조 lifo / 큐는 반대 임 first in first out (fifo) / 튜플(리스트와 같지만 데이터 변경을 허용하지 않는 자료구조)/ 세트 (데이터 중복을 허용하지 않고 수학의 집합 연산을 지원하는 자료구조)
# 딕셔너리 (키와 값 형태의 데이터를 저장하는 자료구조 !/ colloctions 모듈 => 위에 열거된 여러 자료구조를 효율적으로 사용할 수 있도록 지원하는 파이썬 내장 모듈 ! )

#스택 

# 마지막에 들어간 데이터가 가장 먼저 나오는 형태 
a = [1,3,5,7,9]
a.append(200)
a.append(500)
a.pop()
a.pop()
# 500 / 200

# 큐 
a.pop(0)
# pop(0)은 첫번째 들어간 숫자를 추출해주느 값

# 튜플 / 세트 

# 값을 변경하는 것이 불가능함 ! /(튜플 ()형태로 되어있음 )

# 세트는 값을 순서 없이 저장하면서 중복을 불허한 자료형임 ! 
s = set([1,2,3,1,2,3])
s # {1,2,3}

# 더 할때는 add, 한개를 삭제할 떄는 remove(), discard() , update는 새로운 리스트를 그대로 추가하는 것! / 모든 변수를 지우는 clear() 

# union | => 합집합 / intersection & => 교집합 / difference / - => 차집합 !! 

# 딕셔너리 

# 파이썬에서 제일 많이 쓰는 자료구조 이며, 키 , 벨류로 되어 있음 !!, 딕셔너리 함수 !!
# keys() => 키출력 / values()=> 값추출 / items() => 키- 쌍 추출 / 
country_code = {"america":1, "korea":22, 'china':50, 'japan':122}
for k, v in country_code.items():
    print("Key:", k)
    print("value:", v)
#Key: america
#value: 1
#Key: korea
#value: 22
#Key: china
#value: 50
#Key: japan
#value: 122

# collections 모듈 

#deque, OrderedDict, defaultdict, Counter, namedtuple

# deque 모듈은 스택, 큐를 모두 지원하는 모듈 리스트 형식 같은 것에 데이터르 저장해야함 !/ append 사용 가능 !
# OrderedDict / 이름 그대로 순서를 가진 딕셔너리 객체 / 순서를 보장하지 않는 객체 !!
# defaultdict => 딕셔너리 변수를 생성할 때에 키에 기본 값을 지정하는 방법 !/ 

from collections import *

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

print(d.items())
# dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [1])])
[('blue', [2,4]), ('red', [1]), ('yellow', [1,3])]

# Counter 모듈 / 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조 !  개수를 세준다고 생각하자!
# Counter()를 이용하여 사용 !

# namedtuple => 튜플의 형태로 데이터 구조체를 저장하는 방법 / 특정 데이터는 저마다 규정된 정보가 있으면 .. 이러한 정보를 하나의 리스트로 만들어 이차원 리스트로 구성될 수 있어... 튜플형태로 하여 구하려고 함 ! 

text = """ A press releas is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. """.lower().split()

word_count = defaultdict(lambda:0)
for word in text:
    word_count[word] += 1

for i, v in OrderedDict(sorted(word_count.items(), key = lambda t: t[1], reverse=True)).items():
    print(i,v)
```
```
and 3
to 3
a 2
press 2
can 2
you 2
releas 1
is 1
the 1
quickest 1
easiest 1
way 1
get 1
free 1
publicity. 1
if 1
well 1
written, 1
release 1
result 1
in 1
multiple 1
published 1
articles 1
about 1
your 1
firm 1
its 1
products. 1
that 1
mean 1
new 1
prospects 1
contacting 1
asking 1
sell 1
them. 1


```


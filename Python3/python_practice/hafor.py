# 1번 문제
from collections import Counter
word_input = input('input word')
counter_word = Counter(word_input) # Counter를 이용하여 알파벳 갯수 확인!

# 차집합을 이용하기 위해 set으로 변환
count_1 = set(counter_word.most_common(1))
count_2 = set(counter_word.most_common(2))
count_3 = count_2 - count_1 

# dict로 변환하여 2번쨰로 나오는 알파벳을 추출
for key, values in dict(count_3).items():
    print(key)

#2번 문제

# 값을 먼저 받는다.
num_input = input().split()
num_list = list(map(int, num_input)) # str 형태로 되어있는 것을 int로 바꾼다.

# sorted를 이용해서 짝수와 홀수를 각각 왼쪽, 오른쪽으로 분리하여 출력한다.
answer_list = sorted((num for num in num_list if num % 2==0), reverse=True) + \
    sorted((num for num in num_list if num % 2==1), reverse=True)

# 3번문제 

# MDD는 (기간 동안의 최저점 - 기간 동안의 최고점) / 기간 동안의 최고점이다. 
t = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
price = [10, 11, 12, 13, 12, 10, 9, 13, 14, 15, 18, 19, 20, 22, 23, 20, 17, 16, 19, 24, 23]


def MDD(data):
    mdd = 0
    len_1 = 0
    # t 값을 세우기 위한 것임!
    for i in range(1, len(data)-1):
        #s_t = i
        maxv = max(data[:i])
        calcMdd = (maxv - min(data[i:])) / maxv
        print(calcMdd)
        if calcMdd > mdd:
            mdd = calcMdd
            #len_1 = s_t
    return mdd

MDD(price) # 위의 함수를 이용하면 MDD를 구할 수 있다! 
# (t가 4일 때인 (13-9)/13 = 0.3076923076923077 으로 제일 높으며, 그 다음에는 t가 14일 때인 (23-16)/23인 0.30434782608695654가 두 번째로 높다!)

# 4번문제
n = int(input('input num'))
# n이 양의 정수가 아닐 경우 아니라는 문구를 리턴시킴!
def answer_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n>2:
        return answer_fibonacci(n - 1) + answer_fibonacci(n - 2)
    else:
        return 'n은 양의 정수가 아닙니다.'

answer_fibonacci(n)

# 5번 문제 


num_input2 = input().split()
list_a = list(map(int, num_input2))

# 리스트의 값들의 개수가 홀수 인지 짝수 인지 구분 
# 6개 인경우 3번째와 4번째 사이의 값이 중위값에 해당!
if len(list_a) % 2 == 0:
    num_1 = int(len(list_a)/2)
    num_2 = num_1 + 1
    print(int((list_a[num_1] + list_a[num_2])/2))
else:
    i = int((len(list_a))/2)
    print(list_a[num_1])

# 6번 문제


def Max_Prime_Number(n):
    prime_factor = 1 
    num_1 = 2 # 소수의 가장 작은 값은 2
    while num_1 <= n / num_1:
        if n % num_1 == 0:
            prime_factor = int(num_1)
            n /= num_1
        else:
            num_1 += 1
    if prime_factor < n:
        prime_factor = int(n)
    return prime_factor
    # prime_factor가 가장 큰 prime number가 됩니다.

n = int(input())
print(Max_Prime_Number(n))

# 101번 문제
# 파이썬 math 함수를 이용하기.. (factorial을 이용하기 위해서!)
import math 

def answer_exp(x, n):
    answer = 0
    # 답을 구하기 위한 변수 선언

    # 반복문을 이용하여 x**1/1! + x**2/2 + ... x**n/n을 만들어준다.
    for num in range(n):
        answer += x**num/math.factorial(num)
    return answer

answer_exp(7,10)

# 105번 문제 

# 풀지 못하였습니다.

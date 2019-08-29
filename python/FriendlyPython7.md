## 파이썬 기초 정리 7


#### happy Python

- 파일
  - 텍스트 파일
    텍스트 파일은 연속적으로 연결되어 있는 줄글의 집합이라고 생각하면 됌.
  - 파일의 내용을 읽기 전에 파이썬에게 작업할 파일과 파일로 어떤 작업을 할지 알려줘야 함
- open
  - 파일 핸들”을 반환 - 파일에 대한 작업을 수행하기 위해 사용하는 변수
  - 워드 프로세서에서 “File -> Open” 과 비슷함
  - 핸들 = open(파일명, 모드)
  - 파일을 조작하는데 쓰는 핸들을 반환함
  - 파일명에는 문자열이 들어감
  - 모드에 매개 변수를 넣는 것은 선택 사항이며 파일을 읽으려면 ‘r’을, 파일에 쓰려면 ‘w’를 입력
```Python
#ex
fhand = open('123.txt', 'r')
print(fhand)
# fhand의 관련 부분이 출력됨.
# 존재하지 않을 경우 파일을 찾을 수 없다는 에러가 나옴
```
- 개행문자
  - \n이라고 하며, 행을 바꾸는 문자임. 파이썬에서 \n은 하나의 문자임
  - 각 줄이 끝날 때 이를 알리기 위해 “개행 문자”라고 부르는 특수한 문자를 사용함
  - 한 글자 임 !!! 두글자 아님 !!
```Python

#ex1)
a1 = 'Hi Ryu!'
print(a1) # Hi Ryu!
print(len(a1)) # 7
a2 = 'Hello\nSunny!'
print(a2)   # Hello
				    # Sunny!
print(len(a2)) # 12
```
- 파일 처리
  - 텍스트 파일은 일련의 줄이 나열된 것으로 여길 수 있음
  - 텍스트 파일은 각 줄 끝에 개행 문자가 있음
- 파일 핸들
  - 시퀸스
    - 읽기용으로 열린 파일 핸들은 파일의 각 줄에 대한 문자열의 시퀀스로 볼 수 있음
    - for 문을 사용하여 시퀀스를 반복하여 돌 수 있음
    - 시퀀스는 정렬된 집합임을 기억하기
- 파일의 줄세기
  - 파일을 읽기 모드로 열기
  - for 문을 이용하여 각 줄을 읽기
  - 줄을 세고 줄의 수를 출력하기
- 파일의 전체를 읽기
  - 파일 전체(개행 문자 포함 전체)를 하나의 문자열로 읽을 수 있음
- 파일 내용 탐색
  - for 문에 if 문을 넣어서 특정 조건을 만족하는 줄만 출력
- 파일 내용 탐색
  - 문자열 라이브러리에 있는 rstrip()을 이용하여 오른쪽에서부터 공백을 지울 수 있음
  - 개행 문자는 “공백”으로 취급되어 제거됨
  - continue 문을 사용하여 편리하게 줄을 넘길 수 있음
  - in을 사용하여 설정한 선택 기준에 맞춰 줄 안 어디에서든 문자열을 찾을 수 있음
```Python
#ex1)
fhand = open('abc.txt')

for line in fhand :
    print(line)

# 다음을 출력하게 되면 한줄씩 띄워져서 출력되게 됨.
#ex2)
fhand = open('def.txt')
count = 0

for line in fhand :
    count = count + 1
print('Line Count: ', count)

# 만약에 line Count가 35라면 Line Count:  35로 출력됨.
#ex3)
fhand = open('ghi.txt')
inp = fhand.read()
print(len(inp))
# 만약에 inp의 길이가 94646라면 94646으로 출력됨.
print(inp[:20])
# ex) From stephen.marquar으로 출력됨.

#ex4)
fhand = open('ghi.txt')
for line in fhand:
    line = line.rstrip() # 오른쪽 공백 제거
    if line.startswith('From:') :
        print(line)
   #만약에 개행문자가 있다면 rstrip으로 인해 제거 되어 출력됨.
#ex5)
fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)

# There were 27 subject lines in mbox-short.txt와 같이 출력됨. 그리고 위에서는 에러를 방지하기 위해 try, except를 사용함
```

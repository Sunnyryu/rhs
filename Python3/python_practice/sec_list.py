a = [[10, 20], [30, 40], [50, 60]]

print(a[0][1])
print(a[1][0])

a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]

print(a)

from pprint import pprint
a = [[10,20], [100,200], [1000,2000]]
pprint(a, indent=4, width=20)
# indent는 들여쓰기 칸수, width = 가로폭

for x,y in a:
    print(x,y)

for i in a:
    for j in i:
        print(j, end=' ')

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')

i = 0
while i < len(a):
    x, y = a[i]
    print(x ,y)
    i += 1

i = 0
while i < len(a):           # 세로 크기
    j = 0
    while j < len(a[i]):    # 가로 크기
        print(a[i][j], end=' ')
        j += 1              # 가로 인덱스를 1 증가시킴
    print()
    i += 1                  # 세로 인덱스를 1 증가시킴

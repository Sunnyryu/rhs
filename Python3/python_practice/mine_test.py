row, col = map(int, input().split())


matrix = []
for i in range(row):
    matrix.append(list(input()))
# 지뢰와 아닌 곳을 필요하기 위해 만든 matrix 리스트

for i in range(row):
    for j in range(col):
        if matrix[i][j] == "*":
            continue
        else:
            matrix[i][j] = 0
# * 이 없는 곳을 0으로 만들어서 시작하기 위한 반복문 

for i in range(row):
    for j in range(col):
        if matrix[i][j] == 0:
            for x in range(i-1,i+2):
                if x<0 or x>=row:
                    continue
                for y in range(j-1, j+2):
                    if y<0 or y>=col:
                        continue
                    elif matrix[x][y] == "*":
                        matrix[i][j] = matrix[i][j]+1
# 값이 0이라면 주변에 *가 있는 곳에 +1을 하기 위한 반복문

for i in matrix:
    for j in i:
        print(j, end="")
    print()

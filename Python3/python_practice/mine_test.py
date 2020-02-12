row, col = map(int, input().split())


matrix = []
for i in range(row):
    matrix.append(list(input()))


for i in range(row):
    for j in range(col):
        if matrix[i][j] == "*":
            continue
        else:
            matrix[i][j] = 0

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


for i in matrix:
    for j in i:
        print(j, end="")
    print()

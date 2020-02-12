row, col = map(int, input().split())

metrix = []



for i in range(row):

    metrix.append(list(input()))

    for j in range(col):

        if metrix[i][j] == "*":

            continue

        elif metrix[i][j] == ".":

            cnt = 0

            for y in range(i-1, i+2):

                for x in range(j-1, j+2):

                    try:

                        if metrix[i+y][j+x] == "*":

                            cnt += 1

                    except Exception as e:

                        pass

            metrix[i][j] = str(cnt)

            

print(metrix)



for i in metrix:

    print("".join(i))



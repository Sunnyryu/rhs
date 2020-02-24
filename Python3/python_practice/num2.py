result = 0
for i in range(5, -5, -2):
    if i < -3:
        result += 1
    else:
        result -= 1


print(result)

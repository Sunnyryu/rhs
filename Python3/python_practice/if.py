x = int(input())
y = input()

if type(x) == int:
    if y == 'Cash3000':
        x = x-3000
    elif y == 'Cash5000':
        x = x-5000
    else:
        print(x)

print(x)

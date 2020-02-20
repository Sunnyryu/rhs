def calc():
    result = 0
    while True:
        expressions = (yield result)
        a, expression , b = expressions.split()
        if expression == '+':
            result = int(a) + int(b)
        elif expression == '-':
            result = int(a) - int(b)
        elif expression == '*':
            result = int(a) * int(b)
        else:
            result = int(a) / int(b)


expressions = input().split(', ')

c = calc()
next(c)

for e in expressions:
    print(c.send(e))

c.close()

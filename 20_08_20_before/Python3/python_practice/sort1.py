money_1 = input()
money_2 = money_1.split(';')
money_3 = list(map(int,money_2))
money_3.sort(reverse=True)
for i in money_3:
    k = format(i, ',')
    k = '{:>9}'.format(k)
    print(k)

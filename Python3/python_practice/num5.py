a = '246'
b = '462'

strike = 0
ball = 0

for number in a:
    if b.count(number) > 0:
        if b.find(number) == a.find(number):
            strike += 1
        else:
            ball += 1

print('s:',strike, 'ball:', ball)

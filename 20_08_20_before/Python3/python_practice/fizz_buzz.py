num_1, num_2 = map(int, input().split())

for i in range(num_1, num_2+1):
    print('Fizz'*(i % 5 == 0)+'Buzz'*(i % 7 == 0) or i)

c , d = map(int, input().split())
a = {i for i in range(1, c + 1) if c % i == 0}
b = {i for i in range(1, d + 1) if d % i == 0}
divisor = a & b
 
result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)

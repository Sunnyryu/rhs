def prime_number_generator(start, stop):
    for i in range(start, stop):
        for j in range(2, i + 1):
            if i == j:
                yield i
            if i % j == 0:
                break

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')

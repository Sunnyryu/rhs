a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

#list(map(함수, 리스트))
#tuple(map(함수,튜플))


b = map(int, input().split())

tuple_a = (38, 21, 53, 62, 19, 53)

tuple_a.index(53)
tuple_a.count(53)
print(tuple_a.count(53))
for i in tuple_a:
    print(i, end='')

b = tuple(i for i in range(10) if i % 2 ==0)
print(b)


min(b)
max(b)
print(sum(b))

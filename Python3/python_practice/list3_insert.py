a = [99, 88, 77, 66, 55]

for index, value in enumerate(a):
    print(index, value)
    # print(index+1, value)

# enumerate에 리스트를 넣으면 for 반복문에서 인덱스와 요소를 동시에 꺼내 올 수 있습니다.

i = 0
while i < len(a):
    print(a[i])
    i += 1


smallest = a[0]

for i in a:
    if i < smallest:
        smallest = i

print(smallest)

largest = a[0]

for i in a:
    if i > largest:
        largest = i

print(largest)

print(min(a), max(a))

print(sum(a))

from collections import deque

a = deque([10, 20, 30])
a.append(500)
print(a)

a.popleft()
print(a)

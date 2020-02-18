def countdown(n):
    i = n
    def count():
        nonlocal i
        new_i = i
        i -= 1
        return new_i
    return count

n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end='')

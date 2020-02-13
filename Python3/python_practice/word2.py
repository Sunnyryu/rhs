f = open('word2.txt', 'r')
f_1 = f.read()
f_2 = f_1.split()
for i in f_2:
    if i == ''.join(reversed(i)):
        print(i)

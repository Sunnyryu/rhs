word = open('words.txt', 'r')
word_1 = word.read()
word_1 = word_1.split()

for i in word_1:
    if 'c' in i:
        k = i.strip(',.')
        print(k)

## project를 위한 반복문 연습

for i in range(3) :
    # print(i)
    print("jenny: hello sunny, what are you doing?")
    print("sunny: i play the game!")

j = 0
while j < 4 :
    print(j)
    print("jenny: hello sunny, what are you doing?")
    print("sunny: i walk the park!")
    j += 1

k = 0
while True :
    print(k)
    print("jenny: hello sunny, what are you doing?")
    print("sunny: i watching TV!")
    k += 1

    if k > 2:
         break

l = 0
for l in range(3) :
    print(l)
    print("jenny: hello sunny, what are you doing?")
    print("sunny: i see the animal.")

    if l == 1 :
        continue
    print("lin: hello, j&s!")

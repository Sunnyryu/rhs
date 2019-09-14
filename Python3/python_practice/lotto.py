import random

num = input("게임수")

for i in range(0, int(num)):
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    print(lotto)

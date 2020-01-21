import random

solve_number = random.randint(1,100)
user_input = int(input('값 선택 1~ 100 까지'))
while (user_input is not solve_number):
    if user_input > solve_number:
        print('너무커')
    else:
        print('너무 작아')
    user_input = int(input('새로운 수'))


else:
   print('정답')

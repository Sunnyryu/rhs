x = input().split()
x = list(map(int, x))
python_test = x[0]
java_test = x[1]
c_test = x[2]
linux_test = x[3]
total = python_test + java_test + c_test + linux_test
if 0 < python_test <= 100 and 0 < java_test <= 100 and 0 < c_test <= 100 and 0 < linux_test <= 100:
    if total/4 >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')

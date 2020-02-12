s = 'Hello, world!'
s = s.replace('world!', 'Python')
print(s)

table = str.maketrans('aelp', '1234')
k = apple
k2 = k.translate(table)
print(k2)

hello_1 = ''.join(['hello', 'my', 'name', 'is', 'sunny'])
hello_2 = '-'.join(['hello', 'my', 'name', 'is', 'sunny'])
print(hello_1)
print(hello_2)

python_1 = '  python  '
python_1.lstrip()
python_1.rstrip()
python_1.strip()

python_2 = ' _python '
python_2 = python_2.strip('_')
print(python_2)

#ljust, rjust는 각각 왼쪽 정렬, 오른쪽 정렬로 예를들어 ljust(10)이면 길이를 10으로 만들고 왼쪽 정렬 후에 남는 공간이 있다면 공백으로 채운다는 것임 
#center는 가운데 정렬로 남는 양 옆을 공백으로 채움!

#zfill(길이)는 지정된 길이에 맞춰서 문자열에 0을 채우는 것임, 예를 들어 '99'.zfill(5) 이면 '00099'가 됨!



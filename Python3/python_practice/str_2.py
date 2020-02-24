name = 'sunny'
'I`m %s.' % name

'I`m %d years old.' % 27

'%.3f' % 9.9
'%10s' % 'python'
#'    python' %10s는 문자열의 길이를 10으로 만든 뒤 지정된 문자열을 넣고 오른쪽 정렬!

t_1 ='Today is %d %s.' % (12, 'Feb')
print(t_1)

f_1 ='Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
print(f_1)
#'Hello, Python 3.6 Script'

f_2 = 'Hello, {language} {version}'.format(language='Python', version=3.7)
print(f_2)

lan = 'Python'
ver = '3.7'
f_3 = f'Hello, {lan} {ver}'
print(f_3)

f_4 = '{{ {0} }}'.format('Python')
print(f_4)

f_5 =  '{0:<10}'.format('python')
print(f_5)
# 인덱스 뒤에 콜론을 붙이고 정렬할 방향과 길이를 지정해주면 됨 ! <는 왼쪽 정렬후 남는 것을 공백으로 채운다는 의미!

# '%0개수d' % 숫자
#'{인덱스:0개수d'}'.format(숫자)

#'%0개수.자릿수f' % 숫자
#'{인덱스:0개수.자릿수f'}.format(숫자)


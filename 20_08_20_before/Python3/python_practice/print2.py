def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)


personal_info('sunny', 27, '인천')

personal_info(name='sunny', age=27, address='인천')

x = {'name': 'sunny', 'age': 27, 'address': '인천'}

personal_info(**x)

def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ':', arg, sep='')

personal_info(name='sunny')
personal_info(name='sunny', address='인천')



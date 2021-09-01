try:
    a = 10
    b = 0
    #b = 'zero'
    c = a / b
    print(c)
except Exception as e:
    print(e)
except TypeError as e:
    print(e)

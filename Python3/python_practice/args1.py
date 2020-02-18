def var_args(*args, **kwargs):
    print(args)
    print(kwargs)
    args = list(args) + [*kwargs.values()]
    return sum(args)

a =var_args(1,10,100,1000, a=100, b= 1000, c=10000)
print(a)


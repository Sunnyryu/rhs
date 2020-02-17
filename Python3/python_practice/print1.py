def print_numbers(a, *args):
    print(a)
    print(args)

print_numbers(1)

print_numbers(1, 10, 20)

print_numbers(*[10,20,30])

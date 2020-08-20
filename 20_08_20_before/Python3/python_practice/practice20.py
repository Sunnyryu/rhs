def easy_unpack(elements: tuple) -> tuple:

    return elements[0], elements[2], elements[-2]

if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')

#def easy_unpack(elements: tuple) -> tuple:
#    a = elements[0]   # first element of the tuple.
#    b = elements[2]   # third element of the tuple.
#    return (a, b, c)  # tuple to return.
#from operator import itemgetter
#def easy_unpack(elements: tuple) -> tuple:
#    return (itemgetter(0,2,-2)(elements))

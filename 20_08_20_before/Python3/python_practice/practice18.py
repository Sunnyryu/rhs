def checkio(numbers_array: tuple) -> list:
    return tuple(sorted(numbers_array, key = abs))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(checkio((-20, -5, 10, 15))))

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#def checkio(numbers_array: tuple) -> list:
#    m = list(numbers_array)
#    m = sorted(m, key = lambda x: abs(x))
#    return m
#   def checkio(numbers_array: tuple) -> list:
#    return sorted(numbers_array, key=abs)
# checkio = lambda numbers_array: sorted(numbers_array, key=abs)

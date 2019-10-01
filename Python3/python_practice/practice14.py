def index_power(array: list, n: int) -> int:
    if n < len(array) :
        # len() 은 길이를 나타내는 함수로 len(array) => 배열의 길이!!
        return array[n] ** n
        # ex n = 0 이면 0번째 index의 값의 제곱을 리턴함(** = 거듭제곱) => 파이썬에서 index는 0부터 시작~~
    else :
        return -1


if __name__ == '__main__':
    print('Example:')
    print(index_power([1, 2, 3, 4], 2))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

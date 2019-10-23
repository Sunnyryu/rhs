def checkio(number: int) -> int:
    fornumber = 1
    #fornumber는 1이라고 선언

    for Z in str(number) :
    # Z는 문자열로 변환한 number 안에서 가져온다면
        if int(Z):
            #int(Z)가 0 이 아니라면
            fornumber *= int(Z)
            #fornumber는 int(Z)를 곱한 것과 같음
    return fornumber



if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

#def checkio(number: int) -> int:
#product = 1
#while number:
#if number % 10:
#product *= number % 10
#    number //= 10
#    return product
#from functools import reduce
#def checkio(number: int) -> int:
#    return reduce(lambda x, y: x * y, [int(num) for num in str(number) if num != '0'])
#   numberStr = str(number)
#    result = 1
#    for i in numberStr:
#        if i != "0":
#            result = result * int(i)
#    return result

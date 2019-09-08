def say_hi(name: str, age: int) -> str:

    return "Hi. My name is {} and I'm {} years old".format(name, age)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert say_hi("Sunny", 26) == "Hi. My name is Sunny and I'm 26 years old", "First"

    assert say_hi("Sam", 29) == "Hi. My name is Sam and I'm 29 years old", "Second"
    print("Done, It`s finish")


# def = 함수 정의, return은 이걸로 해주라!,
# format 문자열의 format 함수를 사용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.
# assert는  assert(가정 설정문)은 단순하게 프로그램의 특정 지점에서 항상 참이어야 하는 문장입니다.
# assert의 조건을 확인하여 참이면 다음 문장으로 넘어가고,거짓이면 프로그램을 정지시킵니다. Python에서는 assert의 조건이 거짓인 경우 AssertionError를 발생시킵니다.

# from string import Template

#def say_hi(name, age):
#    """
#        Hi!
#    """
#    t = Template("Hi. My name is $name and I'm $age years old")
#return t.substitute(name=name, age=age)
# 다른 사람 풀이(template)이라는 것을 처음 봄...
# template 메소드는 동일한 기능은 상위 클래스에 정의하고 추상 메소드를 선언 후에 서브 클래스에서 메소드 구현을 통해 필요한 부분만 구현 가능
# 중복 최소화, 재사용 용이!!

# 오늘의 한마디! : 더 열심히 함께 파이썬 가즈아!!

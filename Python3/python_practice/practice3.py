def first_word(text: str) -> str:
    text = text.replace(",", " ").replace(".", " ").replace("_", " ").strip()
    text = text.split()
    # your code here
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")

    print(first_word("hello,world")) # hello가 나옴 !!

    # replace(a,b)는 a를 b로 바꿔주는 것이다. strip은 lstrip과 rstrip도 있는데 아무것도 안 넣으면
    # 공백을 제거 해주고 lstrip은 왼쪽만, rstrip은 오른쪽만 strip은 양쪽임!
    # split은 나눠주는 것인데 여기서는 공백단위로 나눠줌
    # 예시는 밑의 first_word에 있으니 확인해보면 이해가 될 거얌!!

    # import re 정규화 모듈을 사용한 것!


    # def first_word(text: str) -> str:
    # return re.search("([\w']+)", text).group(1)
    # 특정 문자열을 검색하여 처음 맞는 문자열을 리턴하는 search() 메서드를 사용
    # 객체로부터 실제 결과 문자열을 얻기 위해서는 group() 메서드를 사용
    # \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
    # \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
    # \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
    # \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
    # \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
    # \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.

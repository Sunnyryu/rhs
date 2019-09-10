def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]

    if not text.endswith('.') :
        text += '.'
    # your code here
    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")


# def = 함수 정의, return은 이걸로 해주라!,
# text = text[0].upper() +text[1:] => 첫 문자는 대문자로 하고 나머지 문자열을 더함
#  '.' 으로 끝나지 않는다면 text += '.'을 더함
#  text를 리턴 시킴 !
#  if 문에서 assert는 맞으면 a 임

# ex1)
# def correct_sentence(text: str) -> str:
#    return text[0].upper() + text[1:] + ("." if text[-1] != "." else "")
# ex2)
#       if text[-1] != '.':
#        text = text + '.'
#    return text.replace(text[0], text[0].upper(), 1)

def popular_words(text: str, words: list) -> dict: #딕셔너리로 바꿔줌
#딕셔너리는 {key1:value1, ....} key:value 방식으로 되어있음
#딕셔너리에서 key는 변하지 않는 값, value는 변하는 값과 변하지 않는 값 모두 사용 가능
    text = text.lower() # 모든 텍스트를 소문자로
    a = text.split() # 텍스트를 공백단위로 쪼갬
    answer = {} # answer는 dict 타입으로 만들어 줌

    for word in words: # words라는 것을 워드에 넣어줌
        answer[word] = a.count(word) # 나온 단어의 수를 카운터함
        print(answer[word])
        print(answer)

    return answer # answer로 리턴함



if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")

# def popular_words(text, words):
# lower_count = text.lower().split().count (lower_count는 텍스트를 소문자하고 공백을 제거하고 카운트해줌)
# return {word: lower_count(word) for word in words}


# def popular_words(text, words):
# return {word:text.lower().split().count(word.lower()) for word in words}

  

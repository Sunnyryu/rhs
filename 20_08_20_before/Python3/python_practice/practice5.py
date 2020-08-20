def between_markers(text: str, begin: str, end: str) -> str:
    if begin in text :
        begin_index = text.find(begin) + len(begin)
    else:
        begin_index = 0
    if end in text :
        end_index = text.find(end)
    else:
        end_index = len(text)


    return text[begin_index:end_index]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')

# 시작이 text에 있다면 시작은시작하는 텍스트 + 시작의 길이이며 / 없다면 0 이다. 예를 들어 >라 시작일 때 >가 없다면
# 시작하는 index는 0이다.
# 끝나는 것이 text 안에 있다면 끝나는 인덱스는 마지막의 찾는 것과 같고 아니라면 텍스트의 길이만큼 이다.
#def between_markers(text: str, begin: str, end: str) -> str:
#    start = text.find(begin) + len(begin) if begin in text else None
#    stop = text.find(end) if end in text else None
#    return text[start:stop]
#    다른 사람 풀이

# def between_markers(text: str, begin: str, end: str) -> str:
#    start, stop = map(text.find, (begin, end))
#    return text[(start + len(begin), 0)[start < 0]:(stop, None)[stop < 0]]

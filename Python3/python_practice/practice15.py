def left_join(phrases):
    return (','.join(phrases)).replace("right","left")
    # ,을 기준으로 phrases를 결합하고 right를 left로 대체해줌
    # ex) "i","right","you"라는 것이 phrases에 있다면 "i,left,you"가 됨!!

if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

from konlpy.tag import Kkma

kkma = Kkma()

text = "아버지가 방에 들어간다"
morphs = kkma.morphs(text)
print(morphs)

pos = kkma.pos(text)
print(pos)
nouns = kkma.nouns(text)
print(nouns)

sentences = "오늘 날씨는 어떤가요? 내일은 겁나 덥다는데"
s = kkma.sentences(sentences)
print(s)

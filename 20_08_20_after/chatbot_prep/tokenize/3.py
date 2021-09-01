from konlpy.tag import Okt

okt = Okt()

text = "아버지가 방에 들어갑니다."

morphs = okt.morphs(text)
print(morphs)

pos = okt.pos(text)
print(pos)

noins = okt.nouns(text)
print(noins)

text = "오늘 날씨가 좋아욤ㅋㅋㅋㅋ"
print(okt.normalize(text))
print(okt.phrases(text))

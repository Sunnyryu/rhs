from nltk.tag import pos_tag
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

result = []
a = "i love potato. I has been carry. I don't love it!. you have a party"

b = TreebankWordTokenizer().tokenize(a)
c = word_tokenize(a)
d = pos_tag(b)
e = pos_tag(c)
f = stopwords.words("english")
for zz in c:
    zz = zz.lower()
    if zz not in f:
        result.append(zz)
g = pos_tag(result)
#print(result,"test")
#print(b)
#print(c)
#print(d)
#print(e)
print(g)

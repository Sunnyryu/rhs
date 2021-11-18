import nltk
from nltk.tag import pos_tag
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

class Preprocess:
    def __init__(self):
        self.nltk = nltk


        self.exclusion_tags = ['.',',']

    def pos(self, sentence):
        receive_sentence = []
        tokenizeword = TreebankWordTokenizer().tokenize(sentence)
        stop_word = stopwords.words("english")
        stop_word.extend(['\'ve','\'re','\'m','\'s','n\'t'])
        for word in tokenizeword:
            word = word.lower()
            if word not in stop_word:
                receive_sentence.append(word)

        return self.nltk.tag.pos_tag(receive_sentence)

    def get_keywords(self, pos, without_tag=False):
        f = lambda x: x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list

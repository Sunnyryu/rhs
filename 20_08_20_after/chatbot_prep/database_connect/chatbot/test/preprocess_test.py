import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
#grandparentdir = os.path.dirname(parentdir)
sys.path.append(parentdir)
print(parentdir)
from utils.Preprocess import Preprocess

sent = '크리스토퍼 내일 오전 10시에 탕수육 주문할래'

p = Preprocess(userdic='../utils/user_dic.tsv')
print(p)
pos = p.pos(sent)
print(pos)
ret = p.get_keywords(pos, without_tag=False)
print(ret)

ret = p.get_keywords(pos, without_tag=True)
print(ret)

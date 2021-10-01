import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
#grandparentdir = os.path.dirname(parentdir)
sys.path.append(parentdir)
print(parentdir)
from utils.Preprocess import Preprocess

sent = '내일 오전 10시에 탕수육 주문할래'

p = Preprocess(userdic='../utils/user_dic.tsv')

pos = p.pos(sent)

ret = p.get_keywords(pos, without_tag=False)
print(ret)

ret = p.get_keywords(pos, without_tag=True)
print(ret)

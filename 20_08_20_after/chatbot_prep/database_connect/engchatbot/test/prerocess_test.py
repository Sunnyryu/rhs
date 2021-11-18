import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
#grandparentdir = os.path.dirname(parentdir)
sys.path.append(parentdir)
print(parentdir)

from utils.Preprocess import Preprocess

sent = "i love potato, i have a party. so i need your help. i'm happy."

p = Preprocess()

pos = p.pos(sent)

ret = p.get_keywords(pos, without_tag=False)
print(ret)

ret = p.get_keywords(pos, without_tag=True)
print(ret)

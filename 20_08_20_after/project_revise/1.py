import os
import sys
import datetime

print(os.getcwd())
print(sys.path.append(os.path.dirname(os.path.dirname(__file__))))

now = datetime.datetime.now()
print(type(now.month))
print("%02d" % now.month)

a = "./210218/1539"

b = a[2:8]
c = a[11:13]
d = a[9:11]
print(d)
print(b,c)

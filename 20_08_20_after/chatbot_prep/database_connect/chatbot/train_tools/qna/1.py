import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
print(currentdir, parentdir)
print(sys.path.append(parentdir))
print(os.path.dirname(os.path.dirname(parentdir)))


import pickle
f = open('1.txt', 'rb')
txt1 = pickle.load(f)
f.close()
print(txt1)

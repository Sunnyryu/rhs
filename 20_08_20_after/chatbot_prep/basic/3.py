import pickle
f = open('1.txt', 'wb')
txt1 = [{'title': 'python progran'}, {'author': 'sunny'}]
pickle.dump(txt1, f)
f.close()

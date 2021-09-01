import pickle 

f = open('2.txt', 'wb')

try:
    txt2 = [{'title':'python'},{'author':'sunny'}
            ]
    pickle.dump(txt2, f)
except Exception as e:
    print(e)
finally:
    f.close()

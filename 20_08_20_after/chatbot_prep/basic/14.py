import numpy as np

arr = np.array([1,2,3])

print(arr)
print(type(arr))

matrix = np.array([[1,2,3], [4,5,6]])
print(matrix)

cr1 = np.array([ [1,2], [3,4] ])
cr2 = np.array([ [1,1], [2,2] ])
cr3 = cr1 + cr2
print(cr3)
cr4 = cr1 - cr2
print(cr4)

dr1 = np.array([ [1,2],[3,4],[5,6] ])
print(dr1)
dr2 = np.array([ [7,8],[9,10]])
dr3 = np.matmul(dr1,dr2)
print(dr3)

er1 = np.array([ [1,2], [3,4] ])
er2 = 10
er3 = er1 * er2
print(er3)

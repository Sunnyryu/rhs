a = [[10, 20], [30, 40]]

import copy

b = copy.deepcopy(a)
b[0][0] = 500
print(b)



import matplotlib.pyplot as plt 

x = [a for a in range(0,11)]
y = list(range(0,11))

print('x축', x)
print('y축', y)

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt 

f = lambda x : x** 2 

x = [ x for x in range(-10, 10)]
y= [ f(y) for y in range(-10, 10)]

print('x축', x)
print('y축', y)

plt.plot(x,y)
plt.show()

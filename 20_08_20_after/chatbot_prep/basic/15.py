import pandas as pd 

numbers = pd.Series( [100,200,300])

print(numbers)

scores = pd.Series( [90, 80, 99], index=['A','B','C'])

print(scores)
print(scores.index)

print(scores.values)

print(scores.index[1], scores.values[1])

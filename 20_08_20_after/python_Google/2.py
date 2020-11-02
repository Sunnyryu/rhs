import pandas as pd 
import numpy as np
import matplotlib

pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())
print("1")

california_housing_dataframe.head()
california_housing_dataframe.hist('housing_median_age')

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
#print(type(cities['City name']))
print(cities, "0")
print(cities['City name'],"2")

#print(type(cities['City name'][1]))
print(cities['City name'][1], "3")

#print(type(cities[0:2]))
print(cities[0:2], "4")

print(population / 1000., "5")

print(np.log(population), "6")

print(population.apply(lambda val: val > 1000000), "7")

cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities, "8")

cities['new name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print(cities,"9")

print(city_names.index)
cities.reindex([2, 0, 1])
cities.reindex(np.random.permutation(cities.index))
print(cities.reindex([0, 4, 5, 2]))
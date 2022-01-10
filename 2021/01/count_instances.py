import numpy as np
from numpy import genfromtxt
my_data = genfromtxt('./2021/01/measurements.csv', delimiter='\n')
# my_data = genfromtxt('measurements.csv', delimiter='\n')


def count_how_many_increases(data):
    difference = np.diff(data)
    increased = [True if x > 0 else False for x in difference]
    return np.sum(increased)


print("First solution: {}".format(count_how_many_increases(my_data)))


sum_neighbors = [np.sum(my_data[i:i+3]) for i in np.arange(0, len(my_data)-2)]
print(my_data[0: 6])
print(sum_neighbors[0:3])
print(my_data[-7: -1])
print(sum_neighbors[-4:-1])

print("Second solution: {}".format(count_how_many_increases(sum_neighbors)))

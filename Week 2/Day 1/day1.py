import numpy as np

#create a array using np

arr = np.array([1,3,4])
print(arr)

#Create a matrix of zeros

zeros = np.zeros((3,3))
print(zeros)

#create a matrix of ones

ones = np.ones((2,5))
print(ones)

range_array = np.arange(1,11,3)
print(range_array)

line_space = np.linspace(1,3,6)
print(line_space)

print(arr.reshape(1,3))

print(arr[-2:-1])
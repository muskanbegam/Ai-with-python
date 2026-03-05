import numpy as np

matrix = np.array([[1,2,3],[2,3,4],[4,5,6]])
vector = np.array([[1,1,0]])

result_add = matrix + vector
result_mul = matrix * vector

print(f"Add : \n {result_add} \nMul : \n {result_mul}")
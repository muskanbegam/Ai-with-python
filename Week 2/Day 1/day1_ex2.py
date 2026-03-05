import numpy as np

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Original Matrix:\n{matrix}")

#Transpose of Matrix
tranpose = matrix.T
print(f"Transpose of the Matrix:\n{tranpose}")

print(f"Addition of Matrix : \n {matrix+tranpose}")
print(f"Subtraction of Matrix : \n {matrix-tranpose}")
print(f"Multiplication of Matrix : \n {matrix*tranpose}")
print(f"Division of Matrix : \n {matrix//tranpose}")






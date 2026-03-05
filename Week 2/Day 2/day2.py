import numpy as np

#Broadcasting
arr1 = np.array([[1,2,3],[4,5,6]])

vector = np.array([[1,0,1]])
print(f"Addition : \n {arr1+vector}")


#Aggrigation Functions: that summarize the array statistically
arr = np.array([[1,2,3,4,5,6]])

print(f"Sum: {np.sum(arr)}" )
print(f"Mean: {np.mean(arr)}")
print(f"Maximum: {np.max(arr)}")
print(f"Minimum: {np.min(arr)}")
print(f"Standard Diviation: {np.std(arr)}")
print(f"Sum along Columns: {np.sum(arr, axis=0)}") #columns - 0
print(f"Sum along Rows: {np.sum(arr, axis=1)}") #rows - 1

#Boolean Indexing and Filtering
evens = arr[arr%2 == 0]
print(evens) 

arr[arr>4] = 0
print(arr)

np.random.seed(2)

#Random Number Generation
random_arr = np.random.rand(3,6)

print(random_arr)
random_integers = np.random.randint(1,12,size = (3,4))
print(random_integers)

# Setting Random Seeds






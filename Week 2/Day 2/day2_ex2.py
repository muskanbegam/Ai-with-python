import numpy as np

#Generate Random Dataset
dataset = np.random.randint(1,51, size = (5,5))
print(f"Orginal Dataset:\n{dataset}")

#Filter values with greater than 25 and replace with 0
dataset[dataset>25] = 0
print(f"Filterred Dataset:\n{dataset}")

#Calculate summary stats
print(f"Sum of the dataset: {np.sum(dataset)}")
print(f"Mean mode of Dataset: {np.mean(dataset)}")
print(f"Standard Diviation of the Dataset: {np.std(dataset)}")
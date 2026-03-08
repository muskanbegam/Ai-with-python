import pandas as pd

#https://gist.github.com/netj/8836201.js

#Load Dataset
df = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

print("--------------------------------------")
print(df.head())
print("--------------------------------------")
print(df.tail(3))
print("--------------------------------------")
print(df.info())
print("--------------------------------------")
print(df.describe())
print("--------------------------------------")

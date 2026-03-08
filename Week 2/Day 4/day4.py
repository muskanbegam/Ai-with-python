#Handling Missing Values
import pandas as pd

df = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")
# df = df.dropna(axis=0)
# print(df.tail())

print(df.head(2))

df["sepal.new.col"] = df["sepal.length"]*3
print(df.head(3))

df["variety_new"] = df["variety"]+ " new"
print(df.head(3))
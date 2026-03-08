import pandas as pd

#Load Dataset
df = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")

selected_col = df[["variety", "sepal.length"]]
# print(selected_col)

selected_row = df[df["sepal.length"] > 5.0]
selected_row = selected_row[["variety", "sepal.length"]]

print(selected_row.head())
import pandas as pd

#Intro To Pandas for Data Manipulation
s = pd.Series([10,20,30,40,50], index = ["a","b","c","d","e"])
# print(s)

data = {"Names":["Muskan","Shreya","Sum","Aisha"], "Age": [15,38,26,48]}
# df = pd.DataFrame(data)
# print(df) 

df = pd.read_csv("D:\Jeez\Practice\Week 2\Day 3\data.csv")
# print(df.tail(3))
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df[["Event", "Description"]])
# print(df[df["Significance_Level"] == "Very High"])

# print(df.iloc[0]) #First Row 
# print(df.iloc[:, 0]) #First Column

print(df.loc[:,"Event"])
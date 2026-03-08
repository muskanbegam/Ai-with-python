import pandas as pd
import numpy as np

#Create a dataset
data = {
    "names" : ["Muskan","Sumithra","Aisha",np.nan,"Shreya"],
    "age": [21,np.nan,34,56,34],
    "score" : [86,43,np.nan,34,12],
}

#Covert our data to Dataframe
df = pd.DataFrame(data)
print(f"\nOrginal DataFrame:\n{df}")

df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].interpolate()
df["names"] = df["names"].fillna("NoName")

print(f"\nDataFrame:\n{df}")

#To rename the Columns
df = df.rename(columns= {"names": "Student-Names", "age": "Student-Age", "score" : "Student-Scores"})
print(f"\nDataFrame:\n{df}")

 

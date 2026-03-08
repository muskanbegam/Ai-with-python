import pandas as pd
import numpy as np

df1 = pd.DataFrame({
    "ID" : [1,2,3],
    "Names": ["Muskan", "Aisha","Leanna"],
    "Age": [25,22,21],
})

df2 = pd.DataFrame({
    "ID" : [1,2,3],
    "Score": [85,90,120]
})

print(f"DataSet 1\n{df1}\nDataSet 2\n{df2}\n")

#Merge DataFrames
merged_df = pd.merge(df1,df2,how="inner", on="ID")
print(f"After Merge of DataFrame:\n{merged_df}")

merged_df["Percentage"] = (merged_df["Score"]/200) * 100
print(f"After Calculating Percentage:\n{merged_df}")



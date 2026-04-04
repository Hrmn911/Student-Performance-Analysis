# Data Loading

import pandas as pd

df = pd.read_csv("student_data.csv")

print(df.head())

# Data Cleaning

print(df.isnull(). sum()) # for checking the missing values

df.drop_duplicates(inplace = True) # for checking the duplicates

df.fillna(0, inplace = True) # for filling the missing values












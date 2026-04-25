# Data Loading

import pandas as pd

df = pd.read_csv("student_data.csv")

print(df)

# Data Cleaning

print(df.isnull(). sum()) # for checking the missing values

df.drop_duplicates(inplace = True) # for checking the duplicates

df.fillna(0, inplace = True) # for filling the missing values

# Cleaning the data

df["Backlog_Subject"] = df["Backlog_Subject"].fillna("None")
df["Backlog_Status"] = df["Backlog_Status"].fillna("No Backlog")
df["Internship_Domain"] = df["Internship_Domain"].fillna("Unknown")
df["Sibling_Domain"] = df["Sibling_Domain"].fillna("Unknown")
df["Sibling_Performance"] = df["Sibling_Performance"].fillna("Uknown")

print(df)
print()
# Data Analysis

def performance(df):
    subjects = ["Math","Science","English"]

    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = df[subjects].mean(axis=1)

    total_students = len(df)

    avg_marks = df["Average"].mean()

    pass_percentage = (df["Average"] >=50).mean() * 100

    backlog_count =  (df[subjects]<50).sum(axis=1)


    return df, total_students, pass_percentage, avg_marks, backlog_count

df = performance(df)
print(df)









 





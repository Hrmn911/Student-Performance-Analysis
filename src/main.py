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
    df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

    total_students = len(df)

    avg_marks = df["Average"].mean()

    pass_percentage = (df["Average"] >=50).mean() * 100

    topper = df.loc[df["Average"].idxmax()]
    topper_name = topper["Name"]
    topper_score = topper["Average"]

    difficult_subject = (df[subjects] < 50).sum().idxmax()



    return df, total_students, pass_percentage, avg_marks, topper_name, topper_score, difficult_subject


df = performance(df)
print(df)









 





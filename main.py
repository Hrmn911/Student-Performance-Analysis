# Data Loading

import pandas as pd

df = pd.read_csv("student_data.csv")

print(df.head())

# Data Cleaning

print(df.isnull(). sum()) # for checking the missing values

df.drop_duplicates(inplace = True) # for checking the duplicates

df.fillna(0, inplace = True) # for filling the missing values

print()

# Data Analyize

df["Total"] = df[["Math", "Science", "English"]].sum(axis = 1) # Total
print(df)

print()

df["Average"] = df["Total"]/ 3 # Average
print(df)

print()
# Perfromance

def performace(avg):
    if avg >= 70:
        return "High Marks"
    elif avg>=50:
        return "Medium Marks"
    else:
        return "Low Marks"

df["Performance"] = df["Average"].apply(performace) # Runs a function on every value in column
print(df)
print()

print(df.sort_values(by= "Average", ascending = False).head()) # Top Students
print()

print(df[df['Average'] < 50]) # Weak Students
print()

print(df[['Math','Science','English']].mean()) # Subject wise Average


import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df['Average'], kde=True)
plt.title("Average Marks Distribution")
plt.show()

df[['Math','Science','English']].mean().plot(kind='bar')
plt.title("Subject-wise Average")
plt.show()

sns.scatterplot(x='Attendance', y='Average', data=df)
plt.title("Attendance vs Performance")
plt.show()

sns.countplot(x='Performance', data=df)
plt.show()


    

 










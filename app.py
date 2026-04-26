import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

from src.main import performance

# ================= TITLE =================
st.markdown("<h1 style='text-align: center;'>🎓 Student Performance Dashboard</h1>", unsafe_allow_html=True)

# ================= LOAD DATA =================
df = pd.read_csv("student_data.csv")

# ================= SIDEBAR FILTERS =================
st.sidebar.header("🔍 Filters")

# Section filter
section = st.sidebar.selectbox("Select Section", ["All"] + list(df["Section"].unique()))

# Gender filter
gender = st.sidebar.selectbox("Select Gender", ["All"] + list(df["Gender"].unique()))

# Search by name
search_name = st.sidebar.text_input("Search Student")

# ================= APPLY FILTERS =================
if section != "All":
    df = df[df["Section"] == section]

if gender != "All":
    df = df[df["Gender"] == gender]

if search_name:
    df = df[df["Name"].str.contains(search_name, case=False)]

# ================= PROCESS =================
df, total_students, pass_percentage, avg_marks, topper_name, topper_score, difficult_subject = performance(df)

# ================= KPI =================
st.subheader("📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("👨‍🎓 Students", total_students)
col2.metric("📘 Avg Marks", f"{avg_marks:.2f}")
col3.metric("✅ Pass %", f"{pass_percentage:.2f}%")

# ================= RESULT =================
st.subheader("📌 Insights")

df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 50 else "Fail")

col1, col2 = st.columns(2)

with col1:
    st.success(f"🏆 Topper: {topper_name} ({topper_score:.2f})")

with col2:
    st.info(f"📉 Difficult Subject: {difficult_subject}")

# ================= GRAPHS =================
st.markdown("---")
st.subheader("📊 Visual Insights")

sns.set_style("whitegrid")

col1, col2, col3 = st.columns(3)

# Graph 1
fig1, ax1 = plt.subplots(figsize=(3,2.5))
sns.histplot(df["Average"], kde=True, ax=ax1)
ax1.set_title("Distribution")
sns.despine()

with col1:
    st.pyplot(fig1)

# Graph 2
fig2, ax2 = plt.subplots(figsize=(3,2.5))
df[["Math","Science","English"]].mean().plot(kind="bar", ax=ax2)
ax2.set_title("Subjects")
sns.despine()

with col2:
    st.pyplot(fig2)

# Graph 3
fig3, ax3 = plt.subplots(figsize=(3,2.5))
df["Result"].value_counts().plot(kind="bar", ax=ax3)
ax3.set_title("Pass/Fail")
sns.despine()

with col3:
    st.pyplot(fig3)

# ================= TABLE =================
st.markdown("---")
st.subheader("📋 Data Table")
st.dataframe(df)
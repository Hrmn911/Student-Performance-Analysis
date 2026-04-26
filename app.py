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


fig1, ax1 = plt.subplots(figsize=(3,2.5))

sns.histplot(df["Average"], kde=True, ax=ax1)

ax1.set_title("Where Students Score Most")
ax1.set_xlabel("Average Marks")
ax1.set_ylabel("Number of Students")

# Highlight average line
mean_val = df["Average"].mean()
ax1.axvline(mean_val, linestyle="--")
ax1.text(mean_val, 1, f"Avg: {mean_val:.1f}", rotation=90)

sns.despine()
fig2, ax2 = plt.subplots(figsize=(3,2.5))

subject_avg = df[["Math","Science","English"]].mean()
bars = subject_avg.plot(kind="bar", ax=ax2)

ax2.set_title("Which Subject is Strongest?")
ax2.set_ylabel("Average Score")

# Add labels on bars
for i, v in enumerate(subject_avg):
    ax2.text(i, v + 1, f"{v:.1f}", ha='center')

sns.despine()

fig3, ax3 = plt.subplots(figsize=(3,2.5))

result_counts = df["Result"].value_counts()
bars = result_counts.plot(kind="bar", ax=ax3)

ax3.set_title("Who Passed and Failed?")
ax3.set_ylabel("Number of Students")

# Add labels
for i, v in enumerate(result_counts):
    ax3.text(i, v + 0.5, str(v), ha='center')

sns.despine()

col1, col2, col3 = st.columns(3)

with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)

with col3:
    st.pyplot(fig3)

st.markdown("### 📌 Quick Insights")

st.info(f"Most students scored around {int(df['Average'].mean())} marks")

best_subject = df[["Math","Science","English"]].mean().idxmax()
st.success(f"Students perform best in {best_subject}")

fail_count = (df["Result"] == "Fail").sum()
st.warning(f"{fail_count} students need improvement")


# ================= TABLE =================
st.markdown("---")
st.subheader("📋 Data Table")
st.dataframe(df)
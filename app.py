import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from src.main import performance

st.title(" 📊 Student Performance Data")

df = pd.read_csv("student_data.csv")
st.dataframe(df)

st.title("🎓 Student Dashboard")

df, total_students, pass_percentage, avg_marks, topper_name, topper_score, difficult_subject = performance(df)

st.subheader("📈 Dashboard Overview")

col1, col2, col3, col4, col5= st.columns(5)

with col1:
    st.metric("Total Students", total_students)

with col2:
    st.metric("Average Marks", f"{avg_marks:.1f}")

with col3:
    st.metric("Pass Percentage", f"{pass_percentage}%")

with col4:
    st.metric("Top Performer", f"{topper_score}%", topper_name)

with col5:
    st.metric("Difficult Subject", difficult_subject)


st.subheader("📊 Data")
st.dataframe(df)



import pandas as pd
import streamlit as st
from src.main import performance

df = pd.read_csv("student_data.csv")
st.dataframe(df)

st.title("🎓 Student Dashboard")

df, total_students, pass_percentage, avg_marks, backlog_count= performance(df)

st.subheader("📈 Dashboard Overview")

col1, col2, col3, col4= st.columns(4)

with col1:
    st.metric("Total Students", total_students)

with col2:
    st.metric("Average Marks", f"{avg_marks:.2f}%")

with col3:
    st.metric("Pass Percentage", f"{pass_percentage:.2f}%")

with col4:
    st.metric("Backlog Count", backlog_count)


st.subheader("📊 Data")
st.dataframe(df)



import pandas as pd
import streamlit as st

df = pd.read_csv("student_data.csv")
st.dataframe(df)


from src.main import performance

df = pd.read_csv("student_data.csv")
df = performance(df)

st.title("📊 Student Performance Dashboard")

st.dataframe(df)
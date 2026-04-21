import pandas as pd
import streamlit as st

df = pd.read_csv("student_data.csv")
st.dataframe(df)

from src.main import performance 

if df is not None:
    df = performance(df)
    
    st.subheader("📊 Performance Data")
    st.dataframe(df)
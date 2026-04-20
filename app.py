import pandas as pd
import streamlit as st

df = pd.read_csv("student_data.csv")
st.dataframe(df) 

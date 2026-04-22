import pandas as pd
import streamlit as st

df = pd.read_csv("student_data.csv")
st.dataframe(df)


import streamlit as st
import pandas as pd

# ✅ import from src folder
from src.main import performance

# ✅ load data
df = pd.read_csv("student_data.csv")

# ✅ process data
df = performance(df)

# ✅ display in UI
st.title("📊 Student Performance Dashboard")

st.subheader("Processed Data")
st.dataframe(df)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Student Dashboard", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 Student Analyzer")
menu = st.sidebar.radio("Navigation", ["Upload Data", "Dashboard", "Top Students", "Weak Students"])

# ---------------- TITLE ----------------
st.title("📊 Student Performance Dashboard")
st.markdown("Analyze student data easily with interactive insights.")

# ---------------- SESSION STORAGE ----------------
if "df" not in st.session_state:
    st.session_state.df = None

# ---------------- UPLOAD SECTION ----------------
if menu == "Upload Data":
    st.header("📂 Upload Dataset")

    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        # Cleaning
        df.drop_duplicates(inplace=True)
        df.fillna(0, inplace=True)

        # Feature Engineering
        df['Total'] = df[['Math','Science','English']].sum(axis=1)
        df['Average'] = df['Total'] / 3

        def performance(avg):
            if avg >= 75:
                return "High"
            elif avg >= 50:
                return "Medium"
            else:
                return "Low"

        df['Performance'] = df['Average'].apply(performance)

        st.session_state.df = df
        st.success("✅ File uploaded and processed successfully!")

        st.dataframe(df.head())

# ---------------- DASHBOARD ----------------
elif menu == "Dashboard":

    if st.session_state.df is None:
        st.warning("⚠️ Please upload data first.")
    else:
        df = st.session_state.df

        st.header("📊 Overview")

        col1, col2, col3 = st.columns(3)

        col1.metric("📌 Average Score", round(df['Average'].mean(), 2))
        col2.metric("🏆 Highest Score", df['Average'].max())
        col3.metric("📉 Lowest Score", df['Average'].min())

        st.markdown("---")
        st.subheader("📊 Visual Insights")

        col1, col2, col3 = st.columns(3)

        # GRAPH 1
        with col1:
            st.markdown("**Average Score Distribution**")
            fig1, ax1 = plt.subplots(figsize=(4,3))
            sns.histplot(df['Average'], kde=True, ax=ax1)
            plt.tight_layout()
            st.pyplot(fig1)
        

        # GRAPH 2
        with col2:
            st.markdown("**Subject-wise Average**")
            fig2, ax2 = plt.subplots(figsize=(4,3))
            df[['Math','Science','English']].mean().plot(kind='bar', ax=ax2)
            plt.tight_layout()
            st.pyplot(fig2)

        # GRAPH 3
        with col3:
            st.markdown("**Performance Levels**")
            fig3, ax3 = plt.subplots(figsize=(4,3))
            df['Performance'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax3)
            ax3.set_ylabel("")
            plt.tight_layout()
            st.pyplot(fig3)

# ---------------- TOP STUDENTS ----------------
elif menu == "Top Students":

    if st.session_state.df is None:
        st.warning("⚠️ Please upload data first.")
    else:
        df = st.session_state.df

        st.header("🏆 Top Performing Students")

        top_df = df.sort_values(by='Average', ascending=False).head(10)
        st.dataframe(top_df)

# ---------------- WEAK STUDENTS ----------------
elif menu == "Weak Students":

    if st.session_state.df is None:
        st.warning("⚠️ Please upload data first.")
    else:
        df = st.session_state.df

        st.header("⚠️ Students Needing Improvement")

        weak_df = df[df['Average'] < 50]
        st.dataframe(weak_df)
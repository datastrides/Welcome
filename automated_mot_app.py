import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit.components.v1 import html

st.set_page_config(page_title="Data MOT Generator", layout="wide")

st.title("🔍 Data MOT Generator")
st.markdown(
    "Upload your CSV or Excel file below to automatically generate a professional data profiling report."
)

uploaded_file = st.file_uploader("Upload your dataset (.csv or .xlsx)", type=["csv", "xlsx"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    st.subheader("📋 MOT Report")
    with st.spinner("Generating report... this may take 30-60 seconds"):
        profile = ProfileReport(df, title="Data MOT Report", explorative=True)
        profile_html = profile.to_html()

        html(profile_html, height=1000, scrolling=True)

        with open("mot_report.html", "w", encoding="utf-8") as f:
            f.write(profile_html)

        with open("mot_report.html", "rb") as f:
            st.download_button("📥 Download Full Report", f, file_name="Data_MOT_Report.html")
else:
    st.info("Please upload a dataset to begin.")

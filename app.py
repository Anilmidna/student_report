import streamlit as st
import pandas as pd
import zipfile
import os
from report_generator import batch_generate_reports, docx_to_pdf

st.title("Student Report Generator")

uploaded_file = st.file_uploader("Upload Student Scores Excel", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success(f"Loaded {len(df)} students. Click below to generate DOCX reports.")
    if st.button("Generate DOCX Reports"):
        docx_files = batch_generate_reports(df)
        st.success("DOCX reports generated! Click below to convert to PDF.")
        if st.button("Convert to PDF and Download ZIP"):
            pdf_files = []
            for docx_file in docx_files:
                pdf_path = docx_to_pdf(docx_file)
                pdf_files.append(pdf_path)
            zip_name = "student_reports.zip"
            with zipfile.ZipFile(zip_name, 'w') as zipf:
                for f in pdf_files:
                    zipf.write(f, os.path.basename(f))
            with open(zip_name, "rb") as fp:
                st.download_button("Download All PDFs (ZIP)", fp, file_name=zip_name)
            for f in pdf_files + docx_files:
                os.remove(f)
            os.remove(zip_name)
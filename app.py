import streamlit as st
import pandas as pd
import zipfile
import os
from dotenv import load_dotenv
from report_generator import batch_generate_reports, docx_to_pdf

# Load environment variables
load_dotenv()

st.title("Student Report Generator")

uploaded_file = st.file_uploader("Upload Student Scores Excel", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success(f"Loaded {len(df)} students. Click below to generate DOCX reports.")
    if st.button("Generate DOCX Reports"):
        docx_files = batch_generate_reports(df)
        st.success("DOCX reports generated! You can download individual files below.")

        # Display individual DOCX file download buttons
        st.subheader("Download Individual DOCX Reports")
        for docx_file in docx_files:
            with open(docx_file, "rb") as fp:
                st.download_button(
                    f"Download {os.path.basename(docx_file)}", 
                    fp, 
                    file_name=os.path.basename(docx_file),
                    key=docx_file  # Unique key for each button
                )

        # Zip all DOCX files and keep ZIP available for download
        zip_name = "student_reports_docx.zip"
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for f in docx_files:
                zipf.write(f, os.path.basename(f))
        st.subheader("Download All DOCX Reports as ZIP")
        with open(zip_name, "rb") as fp:
            st.download_button(
                "Download All DOCX (ZIP)", 
                fp, 
                file_name=zip_name,
                key="docx_zip"  # Unique key for the ZIP button
            )
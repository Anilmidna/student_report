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
        
        st.subheader("Convert to PDF and Download All")
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
                st.download_button(
                    "Download All PDFs (ZIP)", 
                    fp, 
                    file_name=zip_name,
                    key="pdf_zip"  # Unique key for the ZIP button
                )
            for f in pdf_files + docx_files:
                os.remove(f)
            os.remove(zip_name)
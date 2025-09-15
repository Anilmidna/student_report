import zipfile
import os

def zip_reports(report_files, zip_name="reports.zip"):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for f in report_files:
            zipf.write(f, os.path.basename(f))
    return zip_name

# In Streamlit
with open(zip_name, "rb") as fp:
    st.download_button("Download All Reports", fp, file_name=zip_name)
import subprocess

def docx_to_pdf(docx_path):
    pdf_path = docx_path.replace('.docx', '.pdf')
    subprocess.run(['docx2pdf', docx_path, pdf_path])
    return pdf_path
# Or use pypandoc if you prefer
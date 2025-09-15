import pypandoc

def docx_to_pdf(docx_path):
    pdf_path = docx_path.replace(".docx", ".pdf")
    pypandoc.convert_file(docx_path, 'pdf', outputfile=pdf_path)
    return pdf_path
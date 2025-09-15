from docx import Document
from docx.shared import Inches

def save_docx(student_name, report_text, chart_path):
    doc = Document()
    doc.add_heading(f"{student_name}'s Performance Report", 0)
    doc.add_paragraph(report_text)
    doc.add_picture(chart_path, width=Inches(5))
    filename = f"{student_name}_Report.docx"
    doc.save(filename)
    return filename
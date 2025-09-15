from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_pdf(student_name, report_text):
    filename = f"{student_name}_Report.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, f"{student_name}'s Performance Report")

    c.setFont("Helvetica", 12)
    # Wrap text for PDF (simple implementation)
    lines = report_text.split('\n')
    y = height - 100
    for line in lines:
        c.drawString(72, y, line)
        y -= 16
        if y < 72:  # Start a new page if needed
            c.showPage()
            y = height - 72

    c.save()
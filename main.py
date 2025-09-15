from read_excel import df
from prompt_template import make_prompt
from gpt_call import get_report_text
from pdf_report import save_pdf

for idx, row in df.iterrows():
    prompt = make_prompt(row)
    report_text = get_report_text(prompt)
    student_name = row['Name']
    save_pdf(student_name, report_text)
    print(f"Generated {student_name}_Report.pdf")
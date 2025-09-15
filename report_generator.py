import openai
import pandas as pd
import matplotlib.pyplot as plt
from docx import Document
from docx.shared import Inches
from docx2pdf import convert
import os
from concurrent.futures import ThreadPoolExecutor

openai.api_key = os.getenv("OPENAI_API_KEY")

def make_prompt(student_row):
    name = student_row['Name']
    scores = student_row.drop('Name').to_dict()
    scores_text = ', '.join([f"{subject}: {score}" for subject, score in scores.items()])
    prompt = f"""
Student Name: {name}
Scores: {scores_text}

Write an analysis covering:
- Overall performance
- Strongest subjects
- Weakest subjects
- Improvement suggestions

Make the report detailed and constructive.
"""
    return prompt

def get_report_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

def generate_chart(student_name, scores):
    plt.figure(figsize=(6,4))
    subjects = list(scores.keys())
    values = list(scores.values())
    plt.bar(subjects, values, color='skyblue')
    plt.title(f"{student_name} - Performance")
    plt.ylabel("Score")
    plt.tight_layout()
    chart_path = f"{student_name}_chart.png"
    plt.savefig(chart_path)
    plt.close()
    return chart_path

def save_docx(student_name, report_text, chart_path):
    doc = Document()
    doc.add_heading(f"{student_name}'s Performance Report", 0)
    doc.add_paragraph(report_text)
    doc.add_picture(chart_path, width=Inches(5))
    filename = f"{student_name}_Report.docx"
    doc.save(filename)
    return filename

def docx_to_pdf(docx_path):
    pdf_path = docx_path.replace(".docx", ".pdf")
    convert(docx_path, pdf_path)
    return pdf_path

def batch_generate_reports(df):
    report_paths = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        prompts = [make_prompt(row) for _, row in df.iterrows()]
        futures = [executor.submit(get_report_text, prompt) for prompt in prompts]
        report_texts = [future.result() for future in futures]
    for idx, row in df.iterrows():
        student_name = row['Name']
        scores = row.drop('Name').to_dict()
        chart_path = generate_chart(student_name, scores)
        report_text = report_texts[idx]
        docx_path = save_docx(student_name, report_text, chart_path)
        report_paths.append(docx_path)
        os.remove(chart_path)
    return report_paths
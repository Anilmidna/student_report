from docx import Document
from docx.shared import Inches
import matplotlib.pyplot as plt

def make_chart(scores, filename):
    subjects = list(scores.keys())
    values = list(scores.values())
    plt.figure(figsize=(6,4

import matplotlib.pyplot as plt

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
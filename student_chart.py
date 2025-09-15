import matplotlib.pyplot as plt

def make_chart(student_name, scores_dict):
    subjects = list(scores_dict.keys())
    scores = list(scores_dict.values())
    plt.figure(figsize=(6, 4))
    plt.bar(subjects, scores, color='skyblue')
    plt.title(f"{student_name}'s Scores")
    plt.xlabel("Subject")
    plt.ylabel("Score")
    plt.tight_layout()
    chart_path = f"{student_name}_chart.png"
    plt.savefig(chart_path)
    plt.close()
    return chart_path
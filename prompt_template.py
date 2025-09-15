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
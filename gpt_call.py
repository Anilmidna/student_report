import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def get_report_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # or use "gpt-4" if available
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response['choices'][0]['message']['content']
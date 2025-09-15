from concurrent.futures import ThreadPoolExecutor

def batch_generate_reports(student_rows, make_prompt, get_report_text):
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(get_report_text, make_prompt(row)) for row in student_rows]
        for future in futures:
            results.append(future.result())
    return results
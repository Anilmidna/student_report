# Student Report Generator App

Generate personalized student performance reports from Excel, using GPT analysis and charts, exportable to DOCX and PDF.

## Features
- Upload Excel of student scores via Streamlit
- Batch GPT-powered performance analysis
- Auto-generated performance charts (matplotlib)
- Download editable DOCX or PDFs (with charts)
- Bulk download (ZIP)

## Setup

1. **Clone the repo**

   ```sh
   git clone https://github.com/your-org/student-report-app.git
   cd student-report-app
   ```

2. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key**

   ```
   export OPENAI_API_KEY=your-key-here
   ```

4. **Run the app**

   ```sh
   streamlit run app.py
   ```

## Usage

- Upload your Excel file with student scores.
- Click "Generate DOCX Reports" to create editable reports.
- Click "Convert to PDF and Download ZIP" to get all student PDFs in a ZIP file.

## Notes

- First column = `Name`, remaining columns are subjects/assessments.
- DOCX reports are editable before PDF export.
- Example Excel:
    ```
    Name,Math,Science,English
    Alice,92,85,78
    Bob,75,80,88
    ```

---
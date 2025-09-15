# Student Report Generator App

Generate personalized student performance reports from Excel, using GPT analysis and charts, exportable to DOCX and PDF.

## Features
- Upload Excel of student scores via Streamlit
- Batch GPT-powered performance analysis with OpenAI
- Auto-generated performance charts using matplotlib
- Individual DOCX downloads for each student report
- Convert reports to PDF
- Bulk download all reports as ZIP
- Organized file storage in reports directory

## Setup

1. **Clone the repo**

   ```sh
   git clone https://github.com/your-org/student-report-app.git
   cd student-report-app
   ```

2. **Set up Python virtual environment**

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configure OpenAI API Key**

   Create a `.env` file in the project root:
   ```sh
   touch .env
   ```

   Add your OpenAI API key to the `.env` file:
   ```properties
   OPENAI_API_KEY=your-api-key-here
   ```
   
   Note: Replace `your-api-key-here` with your actual OpenAI API key from https://platform.openai.com/api-keys

5. **Run the app**

   ```sh
   streamlit run app.py
   ```

   The app will be available at http://localhost:8501

## Usage

1. **Prepare your Excel file**
   - First column must be named `Name`
   - Additional columns should be subject names with numerical scores
   - Example format:
     ```
     Name        Math    English    Science
     John Doe    85      92         88
     Jane Smith  90      85         95
     ```

2. **Generate Reports**
   - Upload your Excel file using the file uploader
   - Click "Generate DOCX Reports" to create reports
   - Individual DOCX reports will be available for download
   - Click "Convert to PDF" to generate PDF versions

3. **Access Generated Files**
   - All generated files are stored in the `reports/` directory
   - DOCX and PDF files can be downloaded individually
   - Use the ZIP download option to get all PDFs at once

## Project Structure

```
student_report/
├── reports/           # Generated reports (DOCX & PDF)
├── app.py            # Streamlit web interface
├── report_generator.py # Report generation logic
├── requirements.txt  # Python dependencies
└── .env             # Environment variables (API keys)
```

## Notes

- Generated files are stored in the `reports/` directory
- The `reports/` directory and all DOCX/PDF files are gitignored
- Each report includes:
  - Student name and scores
  - GPT-generated performance analysis
  - Visual performance chart
  - Downloadable in both DOCX and PDF formats
    ```
    Name,Math,Science,English
    Alice,92,85,78
    Bob,75,80,88
    ```

---
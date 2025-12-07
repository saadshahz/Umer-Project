# HR Assistant: CV-JD Matcher

> **Midterm Project Submission**  
> An AI-powered tool to automate the screening process by matching CVs against Job Descriptions.

## 📖 Overview
The **HR Assistant** is a web-based application designed to help recruiters process applications faster. By uploading a Candidate's CV and a Job Description (JD), the system analyzes the text to provide:
1.  **Match Percentage**: A weighted score based on skills, experience, and semantic similarity.
2.  **Gap Analysis**: A clear list of matched vs. missing skills.
3.  **Experience Check**: Comparison of seniority levels (e.g., Junior vs. Senior).
4.  **Education Check**: Identification of degrees (e.g., Bachelor's, Master's).

## 🚀 Features
-   **Multi-format Support**: Accepts PDF, DOCX, and TXT files.
-   **Semantic Matching**: Uses `spaCy` to understand context beyond simple keywords.
-   **Skill Categorization**: Automatically groups skills into Technical, Soft, and Tools.
-   **Instant Feedback**: "Glassmorphism" UI provides results in milliseconds.

## 🛠️ Installation

### Prerequisites
-   Python 3.9+
-   pip

### Steps
1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/samadaslamcodes/HR-Assistant.git
    cd HR-Assistant
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download AI Model**:
    This project uses `spacy`'s English model for semantic analysis.
    ```bash
    python -m spacy download en_core_web_md
    ```

## 🏃‍♂️ How to Run

1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```
2.  Run the application:
    ```bash
    python app.py
    ```
3.  Open your browser and visit:
    ```
    http://127.0.0.1:5001
    ```

## 📂 Project Structure

```text
HR-Assistant/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── match.py            # Core matching logic (NLP engine)
│   └── uploads/            # Temporary storage for processing
├── frontend/
│   ├── static/             # CSS, Images
│   └── templates/          # HTML templates (upload.html, results.html)
├── data/
│   └── samples/            # Sample CVs and JDs for testing
├── docs/                   # Documentation (Problem Statement, Use Cases, etc.)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🧪 Example Usage

**Scenario**: Hiring a Python Backend Developer.

1.  **Upload JD**: `Senior_Python_JD.pdf` (Requires Python, Flask, AWS, 5+ years exp).
2.  **Upload CV**: `Candidate_John.docx` (Has Python, Django, AWS, 6 years exp).
3.  **Result**:
    *   **Score**: **92%** (Green Badge)
    *   **Experience**: Match (Senior vs Senior)
    *   **Missing Skills**: "Flask" (Candidate knows Django, but Flask was requested).

---
*Created for Midterm Evaluation.*

# HR CV-JD Match Assistant

An AI-powered recruitment tool designed to parse CVs and Job Descriptions, identifying key skills, qualifications, and experience level to compute a compatibility match.

## Project Features (Mapped to Requirements)
1.  **Input Support**: Accepts **PDF, DOCX, and TXT** files for both CVs and JDs.
2.  **Extraction**: Automatically extracts **Skills** (Technical, Soft, Tools), **Experience Level** (Junior/Mid/Senior), and **Qualifications** (Degrees).
3.  **Matching Engine**: Hybrid algorithm using **TF-IDF**, **Semantic Vectors**, and **Skill Overlap** to generate a precise match score.
4.  **Insights**: Highlights **Matched vs. Missing Skills** and provides a detailed gap analysis.
5.  **Minimal & Modern**: Simple, intuitive "Glassmorphism" UI for instant results.

## Setup
1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Download AI Model**:
    ```bash
    python -m spacy download en_core_web_md
    ```

## How to Run
1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```
2.  Start the server:
    ```bash
    python app.py
    ```
3.  Open your browser and visit: `http://127.0.0.1:5001`

## Example Input / Output

I have provided sample files in the `data/samples/` directory for testing:

### 1. High Match Scenario (~85%+)
*   **Files**: `data/samples/high_match_cv.pdf` + `data/samples/high_match_jd.pdf`
*   **Scenario**: Senior Backend Engineer matching a Senior Backend JD exactly.
*   **Expected Result**: **High Match** (Green Badge) with "High" Experience Level and mostly "Matched Skills".

### 2. Low Match Scenario (<40%)
*   **Files**: `data/samples/low_match_cv.pdf` + `data/samples/low_match_jd.pdf`
*   **Scenario**: Graphic Designer applying for a Backend Engineering role.
*   **Expected Result**: **Low Match** (Red Badge) with "Missing Skills" highlighted (e.g., Python, AWS missing).

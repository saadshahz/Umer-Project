# Use Cases

## Overview
The HR Assistant system supports the core workflow of selecting a candidate file, selecting a job description file, and generating a compatibility report.

---

### Use Case 1: Upload and Analyze Documents
*   **Actor**: HR Recruiter
*   **Trigger**: User navigates to the homepage (`/`).
*   **Preconditions**:
    *   User has a CV file and a JD file (PDF, DOCX, or TXT).
    *   Server is running.
*   **Main Flow**:
    1.  User sees the "Drag & Drop" interface.
    2.  User drops (or selects) a **Resume/CV** file.
    3.  User drops (or selects) a **Job Description (JD)** file.
    4.  User clicks the **"Analyze Match"** button.
    5.  System uploads files to the server.
    6.  System validates file extensions.
    7.  System processes text and calculates similarity.
    8.  System redirects to the Results page.
*   **Alternate Flow (Invalid File)**:
    *   3a. User uploads an image (`.png`).
    *   3b. System detects invalid extension.
    *   3c. System shows an error flash message: "Allowed file types are .txt, .pdf, .docx".
    *   3d. User stays on the upload page.

---

### Use Case 2: View Match Score & Gap Analysis
*   **Actor**: Recruiter
*   **Trigger**: Successful completion of Use Case 1.
*   **Preconditions**: Valid match data generated.
*   **Main Flow**:
    1.  User lands on the Results page.
    2.  User views the **Match Percentage** (e.g., 85%).
    3.  User sees color-coded badges:
        *   **Green**: High Match (>70%)
        *   **Yellow**: Medium Match (40-70%)
        *   **Red**: Low Match (<40%)
    4.  User reviews **Experience Level** comparison (e.g., "Senior" vs "Mid-Level").
    5.  User examines the **Missing Skills** list to see gaps.
    6.  User decides whether to shortlist the candidate.

---

### Use Case 3: API Match (Headless/Integration)
*   **Actor**: External System / Developer
*   **Trigger**: POST request sent to `/api/match`.
*   **Preconditions**: Request includes `cv` and `jd` files.
*   **Main Flow**:
    1.  External system sends multipart/form-data POST request.
    2.  Server parses files and runs matching logic.
    3.  Server returns a JSON object containing:
        *   `match_percentage`
        *   `skills` (matched/missing)
        *   `confidence_score`
*   **Alternate Flow**:
    *   1a. Payload missing files.
    *   2a. Server returns HTTP 400 "No file part".

---

## High-Level Design / Data Flow

```text
+-----------------+       +-------------------+       +-----------------------+
|   User (HR)     | ----> |   Flask Frontend  | ----> |     app.py (Route)    |
| (Browser GUI)   |       | (Upload Form)     |       |   (Input Validation)  |
+-----------------+       +-------------------+       +-----------------------+
                                                                 |
                                                                 v
                                                      +-----------------------+
                                                      |    match.py (Engine)  |
                                                      |                       |
                                                      | 1. Text Extraction    |
                                                      |    (pdfplumber, docx) |
                                                      |                       |
                                                      | 2. Preprocessing      |
                                                      |    (Clean, Lowercase) |
                                                      |                       |
                                                      | 3. Analysis           |
                                                      |    - Experience       |
                                                      |    - Spacy (Semantic) |
                                                      |    - TF-IDF (Cosine)  |
                                                      |    - Skill Sets       |
                                                      +-----------------------+
                                                                 |
                                                                 v
+-----------------+       +-------------------+       +-----------------------+
|  User Decision  | <---- |   Result View     | <---- |      JSON Data        |
| (Shortlist/No)  |       | (HTML/CSS Score)  |       |   (Score, Skills)     |
+-----------------+       +-------------------+       +-----------------------+
```

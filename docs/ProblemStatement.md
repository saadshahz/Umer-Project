# Problem Statement

## 1. The User
*   **Primary Actors**: HR Recruiters, Talent Acquisition Specialists.
*   **Secondary Actors**: Hiring Managers, Department Heads.

## 2. The Pain Point
*   Recruiters often receive hundreds of applications for a single job posting.
*   Manually reading every Resume/CV against a Job Description (JD) is:
    *   **Time-Consuming**: It takes minutes per resume, adding up to hours/days.
    *   **Error-Prone**: Fatigue leads to overlooking qualified candidates.
    *   **Inconsistent**: Different recruiters may prioritize different criteria subjectively.
    *   **Biased**: Unconscious bias may affect screening decisions.

## 3. Why It Matters
*   **Efficiency**: Automating the initial screen saves 70-80% of screening time.
*   **Quality**: Ensures every candidate is evaluated against the *same* criteria found in the JD.
*   **Speed-to-Hire**: Reduces the time to shortlist candidates, securing talent faster.

## 4. MVP Goal
*   Develop a **Web-based 'CV-JD Match Assistant'**.
*   **Core Function**: Allow a user to upload one Resume (CV) and one Job Description (JD).
*   **Output**: An intelligent compatibility score (0-100%) with a breakdown of matched vs. missing skills, experience alignment, and education fit.

## 5. Scope
*   **File Support**: Handling `.pdf`, `.docx`, and `.txt` formats for both inputs.
*   **Text Extraction**: Robust parsing of unstructured text from documents.
*   **Matching Engine**:
    *   **Keyword Matching**: Identifying exact skills (e.g., "Python", "React").
    *   **Semantic Analysis**: Understanding context (e.g., "Machine Learning" related to "Data Science").
    *   **Rule-based Checks**: verifying Education and Experience levels.
*   **Visualization**: A clean, "Glassmorphism" UI displaying the score and gap analysis.
*   **Single Session**: No database persistence; results are shown for the current session.

## 6. Out of Scope (for MVP)
*   **Bulk Upload**: Checking 100 CVs at once against 1 JD (planned for future).
*   **User Accounts**: Login/Signup system (Application is currently open-access).
*   **Interview Scheduling**: Automated calendaring.
*   **Multi-language Support**: Only English is supported for the mid-term.

## 7. Assumptions
*   All uploaded files are readable (not scanned images without OCR).
*   The Job Descriptions are written in English.
*   The standard Python libraries (`spacy`, `scikit-learn`) provide sufficient accuracy for a mid-term prototype without needing a fine-tuned LLM.

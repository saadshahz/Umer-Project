# Release Roadmap

## Phase 1: Immediate Term (3 Months)
**Focus: Usability & Persistence**
*   **Database Integration**: Store upload history in SQLite/PostgreSQL. Recruiters can view past scans.
*   **User Accounts**: Login/Register for different recruiters.
*   **Export to PDF**: Button to download the "Match Report" as a PDF file to share with Hiring Managers.
*   **Detailed Feedback**: Tooltips explaining *why* a match score is low (e.g., "Experience mismatch: Required Senior, Found Junior").

## Phase 2: Medium Term (1 Year)
**Focus: Scale & Intelligence**
*   **Bulk Processing**: Upload a ZIP file of 50 CVs and rank them against 1 JD.
*   **ATS Integration**: Connect with Greenhouse/Lever APIs to pull JDs and push Candidates automatically.
*   **Advanced NLP**: Move from `spacy` vectors to a fine-tuned Transformer model (BERT/RoBERTa) for better context understanding in Tech JDs.
*   **Multi-Language**: Support for French and Spanish CVs.

## Phase 3: Long Term (2 Years+)
**Focus: Full Automation**
*   **Interview Bot**: AI Agent that schedules a preliminary chat with top-matched candidates.
*   **Behavioral Analysis**: Analyzing "Soft Skills" by parsing cover letters and external links (GitHub/LinkedIn).
*   **Bias Detection**: Algorithms specifically tuned to flag and reduce unconscious bias in JDs (e.g., gendered language).
*   **Market Insights**: Suggesting salary ranges based on the skills found in the JD.

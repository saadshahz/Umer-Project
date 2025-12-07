# AI Usage Log

## 1. AI Tools Used
*   **Google Gemini (Antigravity Agent)**: Used for code generation, analyzing existing files, and drafting documentation.
*   **Automated Code Assistants**: Used for writing boilerplate HTML/CSS (during initial dev) and Python logic.

## 2. Prompts & Actions
Below is a summary of the key prompts provided to the AI and the resulting actions:

| Step | Prompt / Request | AI Action | Purpose |
|------|------------------|-----------|---------|
| 1 | "Clone this repo... and run this project..." | `git clone`, `pip install`, `python app.py` | **Project Setup**: Automating the environment configuration and dependency resolution. |
| 2 | "Generate midterm-required files (ProblemStatement, UseCases, TestPlan, etc.)" | Created MD files in `docs/` and updated `README.md`. | **Documentation**: Quickly generating professional-grade documentation based on code analysis. |

## 3. Reflection on AI Usage

### Usefulness
*   **Speed**: Setup, which usually takes 15-20 minutes (finding requirements, debugging paths), was completed in < 2 minutes.
*   **Context Awareness**: The AI read the `app.py` and `match.py` files to understand that the project uses `spacy` and `TF-IDF`, allowing it to write an accurate `ProblemStatement.md` without manual dictation.
*   **Symmetry**: It ensured all documents (`UseCases`, `TestPlan`) followed a consistent tone and structure.

### Risks & Limitations
*   **Dependency**: Over-reliance on AI for documentation can lead to a lack of deep understanding of the underlying logic if the developer doesn't review it.
*   **Verification**: The AI might assume "perfect" code. For example, writing a test plan that assumes a feature exists when it might be buggy. Manual verification is still required (hence the "Verification" steps in our workflow).

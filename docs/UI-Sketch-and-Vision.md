# UI Sketch and Vision

## 1. Future UI Vision
The current interface is functional, but the vision for v2.0 is a **"Recruiter Dashboard"**.
*   **Aesthetic**: Glassmorphism (frosted glass effects), vibrant gradients (Purple/Blue), and floating cards.
*   **Interactivity**: Drag-and-drop with real-time progress bars. Micro-animations when a match is calculated.

## 2. Key UI Decisions
1.  **Split Screen Layout**: CV on the left, JD on the right for visual comparison, with the Score floating in the center/top.
2.  **Color-Coded Badges**:
    *   **Green**: > 70% (Go)
    *   **Yellow**: 40-70% (Maybe)
    *   **Red**: < 40% (No)
    *   *Why?* Recruiters need to make split-second decisions.
3.  **Gap Analysis Highlight**: "Missing Skills" should be the most prominent text after the score, as it's the primary reason to reject a candidate.

## 3. Wireframe (ASCII)

```text
+---------------------------------------------------------------+
|  HR Assistant v2.0              [History] [Settings] [Logout] |
+---------------------------------------------------------------+
|                                                               |
|  +---------------------+   +---------------------+            |
|  |      CANDIDATE      |   |   JOB DESCRIPTION   |            |
|  |                     |   |                     |            |
|  |  [ PDF Icon ]       |   |  [ DOCX Icon ]      |            |
|  |  John_Doe_CV.pdf    |   |  Senior_Fullstack   |            |
|  |                     |   |                     |            |
|  +---------------------+   +---------------------+            |
|             \                       /                         |
|              \                     /                          |
|           +---------------------------+                       |
|           |      MATCH: 87% (A)       |  <-- Green Pulse      |
|           +---------------------------+                       |
|                                                               |
| +-----------------------------------------------------------+ |
| |  Skill Analysis                                           | |
| |  [+] Python  [+] React  [+] AWS  [+] Docker               | |
| |  [-] Kubernetes (Missing)  [-] Azure (Missing)            | |
| +-----------------------------------------------------------+ |
|                                                               |
|         [ DOWNLOAD REPORT ]       [ SAVE PROFILE ]            |
+---------------------------------------------------------------+
```

## 4. Design System Draft
*   **Font**: Inter or Roboto (Clean, Sans-serif).
*   **Primary Color**: #6C63FF (Purple).
*   **Secondary**: #4CAF50 (Success Green), #F44336 (Error Red).
*   **Background**: Light Gray (#F5F7FA) with White Cards (#FFFFFF).

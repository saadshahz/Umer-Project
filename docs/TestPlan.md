# Test Plan

## Overview
This document outlines the testing strategy for the HR Assistant MVP. It focuses on functional testing of the matching engine and file handling.

## Test Cases

| ID | Test Case | Type | Input Data | Steps | Expected Output | Actual Output |
|----|-----------|------|------------|-------|-----------------|---------------|
| **TC-01** | **Perfect Match (High Score)** | Positive | **CV**: `Senior_Dev_CV.pdf`<br>**JD**: `Senior_Dev_JD.pdf` | 1. Upload both files.<br>2. Click Match. | Score > 85%.<br>Experience Level: "Senior" = "Senior".<br>Missing Skills: None/Few. | Will match after execution |
| **TC-02** | **Clear Mismatch (Low Score)** | Negative | **CV**: `Graphic_Designer.pdf`<br>**JD**: `Backend_Dev_JD.pdf` | 1. Upload both files.<br>2. Click Match. | Score < 40%.<br>Skills warning displayed.<br>Missing most technical keywords. | Will match after execution |
| **TC-03** | **Partial Skill Overlap** | Normal | **CV**: `Junior_Python_CV.docx`<br>**JD**: `Mid_Python_JD.txt` | 1. Upload files.<br>2. Click Match. | Score ~50-70%.<br>Experience mismatch detected (Junior vs Mid). | Will match after execution |
| **TC-04** | **Invalid File Type** | Edge | **CV**: `My_Photo.png`<br>**JD**: `Job.txt` | 1. Upload the PNG file.<br>2. Click Match. | System rejects upload.<br>Flash message: "Allowed file types are .txt, .pdf, .docx". | Will match after execution |
| **TC-05** | **Empty/Corrupt File** | Edge | **CV**: `Empty.txt` (0 bytes)<br>**JD**: `Job.txt` | 1. Upload empty file.<br>2. Click Match. | System handles gracefully.<br>Score: 0% or Error message warning about empty text. | Will match after execution |

## Testing Environment
*   **OS**: Windows 10/11
*   **Browser**: Chrome / Edge
*   **Python**: 3.9+
*   **Dependencies**: `spacy` model embedded.

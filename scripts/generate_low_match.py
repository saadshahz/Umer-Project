from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_pdf(filename, text_lines):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 40
    
    for line in text_lines:
        c.drawString(40, y, line)
        y -= 20
        
    c.save()
    print(f"Created {filename}")

# LOW MATCH SCENARIO
# CV: Graphic Designer
# JD: Python Backend Engineer

cv_content = [
    "Jordan Lee",
    "Creative Graphic Designer",
    "jordan.lee@example.com",
    "",
    "Summary:",
    "Visual storyteller with 4 years of experience in Adobe Creative Suite.",
    "Specialized in branding, logo design, and social media graphics.",
    "",
    "Skills:",
    "- Adobe Photoshop, Illustrator, InDesign",
    "- Typography, Color Theory",
    "- UI/UX Basics (Figma, Sketch)",
    "- Video Editing (Premiere Pro)",
    "",
    "Experience:",
    "Graphic Designer | Creative Studio (2019 - Present)",
    "- Designed marketing materials for 50+ clients.",
    "- Created brand identity packages including logos and guidelines.",
    "",
    "Education:",
    "- Bachelor of Fine Arts (BFA), Art Institute"
]

jd_content = [
    "Job Title: Senior Backend Engineer",
    "",
    "Job Description:",
    "We are looking for a Senior Backend Engineer to join our core infrastructure team.",
    "",
    "Requirements:",
    "- 5+ years of experience in backend development.",
    "- Strong proficiency in Python and Django/Flask.",
    "- Experience with cloud platforms, specifically AWS.",
    "- Hands-on experience with Docker and Kubernetes.",
    "- Solid understanding of databases like PostgreSQL and Redis.",
    "- Bachelor's in Computer Science or related field.",
    "",
    "Tech Stack:",
    "- Python, Django, AWS, Docker, Kubernetes, PostgreSQL"
]

if __name__ == "__main__":
    create_pdf("low_match_cv.pdf", cv_content)
    create_pdf("low_match_jd.pdf", jd_content)

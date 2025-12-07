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

# HIGH MATCH SCENARIO
# Both documents share: 
# - Title: Senior Backend Engineer
# - Skills: Python, Django, AWS, Docker, Kubernetes, PostgreSQL, Redis, Celery
# - Exp: Senior / 5+ years
# - Edu: Bachelor's in Computer Science

cv_content = [
    "Alex Smith",
    "Senior Backend Engineer",
    "alex.smith@example.com",
    "",
    "Professional Summary:",
    "Highly skilled Senior Backend Engineer with 6 years of experience in Python development.",
    "Expert in building scalable web applications using Django and Flask.",
    "Proficient in cloud architecture on AWS and containerization with Docker and Kubernetes.",
    "",
    "Skills:",
    "- Languages: Python, JavaScript, SQL",
    "- Frameworks: Django, Flask, FastAPI",
    "- Cloud/DevOps: AWS, Docker, Kubernetes, CI/CD",
    "- Databases: PostgreSQL, Redis",
    "- Other: Celery, Git, REST APIs",
    "",
    "Experience:",
    "Senior Python Developer | Tech Solutions Inc. (2018 - Present)",
    "- Led a team of 5 developers to build a SaaS platform using Python and Django.",
    "- Optimized PostgreSQL database queries, reducing load times by 40%.",
    "- Deployed microservices on AWS using Docker and Kubernetes.",
    "",
    "Education:",
    "- Bachelor's in Computer Science, University of Technology"
]

jd_content = [
    "Job Title: Senior Backend Engineer",
    "",
    "Job Description:",
    "We are looking for a Senior Backend Engineer to join our core infrastructure team.",
    "The ideal candidate has strong experience with Python, Django, and Cloud technologies.",
    "",
    "Requirements:",
    "- 5+ years of experience in backend development.",
    "- Strong proficiency in Python and Django/Flask.",
    "- Experience with cloud platforms, specifically AWS.",
    "- Hands-on experience with Docker and Kubernetes for containerization.",
    "- Solid understanding of databases like PostgreSQL and Redis.",
    "- Bachelor's in Computer Science or related field.",
    "",
    "Responsibilities:",
    "- Design and develop REST APIs.",
    "- Manage deployments using CI/CD pipelines.",
    "- Collaborate with the frontend team.",
    "",
    "Tech Stack:",
    "- Python, Django, AWS, Docker, Kubernetes, PostgreSQL"
]

if __name__ == "__main__":
    create_pdf("high_match_cv.pdf", cv_content)
    create_pdf("high_match_jd.pdf", jd_content)

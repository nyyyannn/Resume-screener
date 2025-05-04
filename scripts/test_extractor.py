from extractor import extract_text_generic

resume_path = "./resumes/resume.pdf"
jd_path = "./job_descriptions/job_description.txt"

resume_text = extract_text_generic(resume_path)
jd_text = extract_text_generic(jd_path)

print("=== RESUME TEXT SAMPLE ===")
print(resume_text)  # Just first 500 characters

print("\n=== JD TEXT SAMPLE ===")
print(jd_text)

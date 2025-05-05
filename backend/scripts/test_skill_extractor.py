from extractor import extract_text_generic
from skill_extractor import extract_entities_and_skills

resume_text = extract_text_generic("./resumes/resume.pdf")
jd_text = extract_text_generic("./job_descriptions/job_description.txt")

resume_data = extract_entities_and_skills(resume_text)
jd_data = extract_entities_and_skills(jd_text)

print("=== Resume Extracted Skills ===")
print(resume_data["matched_skills"])

print("\n=== JD Extracted Skills ===")
print(jd_data["matched_skills"])

from extractor import extract_text_generic
from skill_extractor import extract_entities_and_skills
from matcher import compute_similarity

# Extract resume and JD text
resume_text = extract_text_generic("./resumes/resume.pdf")
jd_text = extract_text_generic("./job_descriptions/job_description.txt")

# Extract skills from resume and JD
resume_data = extract_entities_and_skills(resume_text)
jd_data = extract_entities_and_skills(jd_text)

# Focus only on the skills part
resume_skills = " ".join(resume_data["matched_skills"])
jd_skills = " ".join(jd_data["matched_skills"])

# Calculate similarity based on skills
similarity_score = compute_similarity(resume_skills, jd_skills)

print(f"🧠 Resume-JD Similarity Score: {similarity_score}")

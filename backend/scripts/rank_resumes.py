import os
from scripts.extractor import extract_text_generic
from scripts.skill_extractor import extract_entities_and_skills
from scripts.matcher import compute_similarity

def rank_resumes_against_jd(jd_path, resumes_folder_path):
    jd_text = extract_text_generic(jd_path)
    jd_data = extract_entities_and_skills(jd_text)
    jd_skills = " ".join(jd_data["skills"])
    jd_experience = " ".join(jd_data["experience"])
    jd_combined = jd_skills + " " + jd_experience

    resume_scores = []

    for resume_filename in os.listdir(resumes_folder_path):
        if resume_filename.lower().endswith(('.pdf', '.txt', '.docx')):
            resume_path = os.path.join(resumes_folder_path, resume_filename)
            resume_text = extract_text_generic(resume_path)
            resume_data = extract_entities_and_skills(resume_text)

            resume_skills = " ".join(resume_data["skills"])
            resume_experience = " ".join(resume_data["experience"])
            resume_combined = resume_skills + " " + resume_experience

            score = compute_similarity(resume_combined, jd_combined)
            resume_scores.append((resume_filename, score))

    resume_scores.sort(key=lambda x: x[1], reverse=True)
    return resume_scores

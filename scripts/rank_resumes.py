import os
from skill_extractor import extract_entities_and_skills
from matcher import compute_similarity
from extractor import extract_text_generic
import numpy as np

def rank_resumes_against_jd(jd_path, resumes_folder_path):
    """
    Ranks multiple resumes based on their similarity to the job description.
    Returns a list of tuples with (resume_name, similarity_score).
    """
    # Extract and process JD
    jd_text = extract_text_generic(jd_path)
    jd_data = extract_entities_and_skills(jd_text)
    jd_skills = " ".join(jd_data["matched_skills"])

    resume_scores = []

    # Iterate through all resumes in folder
    for resume_filename in os.listdir(resumes_folder_path):
        resume_path = os.path.join(resumes_folder_path, resume_filename)

        # Handle only .pdf and .txt files, case-insensitive
        if resume_filename.lower().endswith(('.pdf', '.txt')):
            resume_text = extract_text_generic(resume_path)
            resume_data = extract_entities_and_skills(resume_text)
            resume_skills = " ".join(resume_data["matched_skills"])

            score = compute_similarity(resume_skills, jd_skills)
            resume_scores.append((resume_filename, score))

    # Sort in descending order
    resume_scores.sort(key=lambda x: x[1], reverse=True)

    return resume_scores


def shortlist_candidates(ranked_resumes, threshold=0.80):
    """
    Filters and returns resumes with similarity score above the threshold.
    """
    shortlisted = [(name, score) for name, score in ranked_resumes if score >= threshold]
    return shortlisted

def categorize_candidates(ranked_resumes):
    """
    Categorizes candidates into tiers based on their similarity scores.
    """
    categories = {"Strong Match": [], "Moderate Match": [], "Barely a Match": []}

    for resume, score in ranked_resumes:
        if score >= 0.85:
            categories["Strong Match"].append((resume, score))
        elif score >= 0.70:
            categories["Moderate Match"].append((resume, score))
        else:
            categories["Barely a Match"].append((resume, score))

    return categories

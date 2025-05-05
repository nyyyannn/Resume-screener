from rank_resumes import rank_resumes_against_jd, shortlist_candidates, categorize_candidates
import numpy as np

# Path to your job description
jd_path = "./job_descriptions/job_description.txt"
# Folder containing resumes
resumes_folder = "./resumes"

# Rank the resumes
ranked_resumes = rank_resumes_against_jd(jd_path, resumes_folder)

# Print the ranked resumes
print("=== Ranked Resumes ===")
for resume, score in ranked_resumes:
    print(f"{resume}: {score:.4f}")

# Apply shortlisting based on threshold
print("\n=== Shortlisted Candidates (Threshold: 0.60) ===")
shortlisted = shortlist_candidates(ranked_resumes, threshold=0.60)

if not shortlisted:
    print("🚨 No candidates met the threshold.")
else:
    for resume, score in shortlisted:
        print(f"{resume}: {score:.4f}")

# 📊 Statistical Analysis and Category Breakdown
print("\n📊 Statistical Analysis")
if ranked_resumes:
    scores = [score for _, score in ranked_resumes]
    print(f"Mean Score: {np.mean(scores):.4f}")
    print(f"Standard Deviation: {np.std(scores):.4f}")

    # Categorize candidates based on scores
    categories = categorize_candidates(ranked_resumes)

    print("\n=== Candidate Categories ===")
    for tier, members in categories.items():
        print(f"\n🔹 {tier} ({len(members)} candidates)")
        for name, score in members:
            print(f"   - {name}: {score:.4f}")
else:
    print("No ranked resumes to categorize.")

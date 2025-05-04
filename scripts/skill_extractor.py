import spacy
from spacy.matcher import PhraseMatcher

# Load the large English NLP model
nlp = spacy.load("en_core_web_lg")

# Define a custom skillset (expand as needed)
CUSTOM_SKILLS = [
    "Python", "Java", "C++", "SQL", "JavaScript", "Node.js", "React",
    "Django", "Flask", "REST", "MongoDB", "PostgreSQL", "Git", "Docker",
    "AWS", "Azure", "Machine Learning", "NLP", "Pandas", "NumPy", "scikit-learn"
]

# Build PhraseMatcher
def create_matcher(skills_list):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill) for skill in skills_list]
    matcher.add("SKILLS", patterns)
    return matcher

matcher = create_matcher(CUSTOM_SKILLS)

def extract_entities_and_skills(text):
    """
    Extracts entities using NER and keyword matching.
    Returns a dict of relevant info.
    """
    doc = nlp(text)

    # Named Entities from spaCy
    entities = [ent.text for ent in doc.ents if ent.label_ in {"ORG", "GPE", "PERSON", "DATE", "NORP", "WORK_OF_ART"}]

    # Matched custom skills
    matches = matcher(doc)
    matched_skills = set()
    for match_id, start, end in matches:
        span = doc[start:end]
        matched_skills.add(span.text)

    return {
        "named_entities": list(set(entities)),
        "matched_skills": list(matched_skills)
    }

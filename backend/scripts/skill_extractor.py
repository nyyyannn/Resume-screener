import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from collections import Counter

nlp = spacy.load("en_core_web_lg")

# Define a function to get relevant skills dynamically
def get_skills_from_job_description(job_desc_text, threshold=0.7):
    """
    Extracts relevant skills from a job description by matching text against skills in the job description.
    Uses word similarity to identify terms that are likely to be skills.
    
    Args:
    job_desc_text (str): The job description text.
    threshold (float): The minimum similarity threshold for considering a match.

    Returns:
    list: A list of relevant skills found in the job description.
    """
    doc = nlp(job_desc_text)
    
    # Initialize a counter for matching terms
    skill_counter = Counter()

    # Try to extract words and phrases that resemble common skills or technologies
    for token in doc:
        if token.pos_ in {'NOUN', 'PROPN'} and len(token.text) > 3:  # Consider nouns and proper nouns
            # Check if the word's similarity with known skill-like terms is above the threshold
            for skill in doc:
                similarity = token.similarity(skill)
                if similarity > threshold and token != skill:  # Avoid self-similarity
                    skill_counter[token.text.lower()] += 1

    # Filter out terms that occur less frequently (low confidence)
    filtered_skills = [skill for skill, count in skill_counter.items() if count > 1]
    
    return filtered_skills

def create_matcher(skills_list):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill) for skill in skills_list]
    matcher.add("SKILLS", patterns)
    return matcher

def extract_entities_and_skills(text):
    """
    Extracts named entities (such as organizations, locations, and persons) and relevant skills from the provided text.
    
    Args:
    text (str): The text to analyze.
    
    Returns:
    dict: A dictionary containing named entities and matched skills.
    """
    doc = nlp(text)

    entities = [ent.text for ent in doc.ents if ent.label_ in {"ORG", "GPE", "PERSON", "DATE", "NORP", "WORK_OF_ART"}]

    relevant_skills = get_skills_from_job_description(text)

    return {
        "named_entities": list(set(entities)),
        "matched_skills": relevant_skills
    }


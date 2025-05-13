from collections import Counter

def extract_relevant_phrases(text):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    skill_phrases = set()
    experience_phrases = set()

    # Skill extraction: noun chunks with technical flavor
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.strip()
        if 2 < len(chunk_text) < 50:
            if any(tok.pos_ in {"NOUN", "PROPN"} for tok in chunk):
                if not chunk.root.is_stop and chunk.root.pos_ != "DET":
                    skill_phrases.add(chunk_text)

    # Experience extraction: smarter matching
    for sent in doc.sents:
        lower = sent.text.lower()
        if "experience" in lower or "worked on" in lower or "developed" in lower or "built" in lower:
            if any(tok.like_num for tok in sent):  # Look for numbers (like "3 years")
                experience_phrases.add(sent.text.strip())

    return {
        "skills": list(skill_phrases),
        "experience": list(experience_phrases)
    }

def extract_entities_and_skills(text):
    doc = nlp(text)

    named_entities = [
        ent.text for ent in doc.ents
        if ent.label_ in {"ORG", "GPE", "PERSON", "DATE", "NORP", "WORK_OF_ART"}
    ]

    content = extract_relevant_phrases(text)

    return {
        "named_entities": list(set(named_entities)),
        "skills": content["skills"],
        "experience": content["experience"]
    }

import spacy

# Load spaCy model once (important for performance)
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str) -> str:
    """
    NLP preprocessing:
    - Tokenization
    - Lemmatization
    - Stopword & punctuation removal
    """
    doc = nlp(text)

    tokens = []
    for token in doc:
        if not token.is_stop and not token.is_punct:
            tokens.append(token.lemma_.lower())

    return " ".join(tokens)
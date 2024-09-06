import spacy
import requests
from sklearn.feature_extraction.text import CountVectorizer
from services import perform_seo_analysis

# Load Spacy model for NLP
nlp = spacy.load('en_core_web_sm')

# Keyword Extraction
def extract_keywords(content):
    doc = nlp(content)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    return keywords

# Competitor Analysis using Content Similarity
def competitor_content_analysis(url, competitor_url):
    original_content = perform_seo_analysis(url)['content']
    competitor_content = perform_seo_analysis(competitor_url)['content']
    
    vectorizer = CountVectorizer().fit_transform([original_content, competitor_content])
    vectors = vectorizer.toarray()
    
    cosine_sim = cosine_similarity(vectors)
    return {'similarity_score': cosine_sim[0][1]}

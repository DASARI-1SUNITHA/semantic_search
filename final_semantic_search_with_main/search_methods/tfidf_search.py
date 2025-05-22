from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tfidf_search(question, chunks):
    vectorizer = TfidfVectorizer().fit([question] + chunks)
    vectors = vectorizer.transform([question] + chunks)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    return chunks[similarities.argmax()]

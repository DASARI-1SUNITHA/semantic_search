"""
main.py - Smart Semantic Search System

Automatically selects the best search technique (Keyword, TF-IDF, or Embedding-based)
based on the user's question length and performs semantic search on a transcript.
"""

import os
from utils.text_chunker import chunk_text
from search_methods.keyword_search import keyword_search
from search_methods.tfidf_search import tfidf_search
from search_methods.embedding_search import embedding_search

def load_transcript(path="transcript.txt"):
    """
    Loads transcript text from file.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Transcript file not found.")
        return ""

def smart_search(question, chunks):
    """
    Selects the best search method based on question length and returns the best-matched chunk.
    """
    word_count = len(question.split())

    if word_count <= 4:
        print("\n🔍 Search Method Used: Keyword Search (best for short/specific queries)")
        return keyword_search(question, chunks)
    elif word_count <= 10:
        print("\n🔍 Search Method Used: TF-IDF Search (balanced for moderate queries)")
        return tfidf_search(question, chunks)
    else:
        print("\n🔍 Search Method Used: Embedding-Based Semantic Search (best for long/descriptive queries)")
        return embedding_search(question, chunks)

def main():
    """
    Main function to run the CLI loop for user queries.
    """
    transcript = load_transcript()
    if not transcript:
        return

    chunks = chunk_text(transcript)

    print("📘 Welcome to the Smart Semantic Search System!")
    print("Ask a question related to the transcript. Type 'exit' to quit.")

    while True:
        question = input("\n❓ Your Question: ").strip()
        if question.lower() == "exit":
            print("👋 Exiting. Thank you for using the search system!")
            break
        try:
            answer = smart_search(question, chunks)
            print("\n📌 Most Relevant Passage:\n", answer)
        except Exception as e:
            print("⚠️ Error occurred:", e)

if __name__ == "__main__":
    main()

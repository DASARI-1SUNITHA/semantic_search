# 📘 Semantic Search System for Transcript Q&A

This project implements a **Smart Semantic Search System** in Python that can extract the most relevant answer from a transcript based on a user’s question. It uses a combination of **keyword matching**, **TF-IDF cosine similarity**, and **embedding-based semantic search**—selecting the most appropriate method automatically depending on the complexity of the question.

---

## 🚀 Features

- 🔍 **Smart Method Selection**:
  - ≤ 4 words: **Keyword Search**
  - 5–10 words: **TF-IDF Search**
  - > 10 words: **Embedding-based Semantic Search**

- ✅ **Handles long-form transcripts**
- 💬 **Command-line interface**
- 📚 Uses modern NLP libraries like `scikit-learn`, `sentence-transformers`, `numpy`
- 📦 Clean modular structure for reusability and scalability

---

## 🧠 Search Techniques Used

| Technique      | When Used           | Description |
|----------------|---------------------|-------------|
| Keyword Match  | ≤ 4 words            | Direct overlap of words between question and transcript chunks. |
| TF-IDF         | 5–10 words           | Measures term frequency–inverse document frequency to assess relevance. |
| Embedding-based| > 10 words           | Leverages transformer embeddings to find semantically similar content. |

--


from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def embedding_search(question, chunks):
    question_emb = model.encode(question, convert_to_tensor=True)
    chunk_embs = model.encode(chunks, convert_to_tensor=True)
    similarities = util.cos_sim(question_emb, chunk_embs)[0]
    best_match_idx = similarities.argmax().item()
    return chunks[best_match_idx]

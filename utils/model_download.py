# from sentence_transformers import SentenceTransformer
# import os

# # Load model
# model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'saved_bge_m3'))
# model = SentenceTransformer(model_path)

# # # Save model locally
# # save_path = "./saved_bge_m3"
# # model.save(save_path)
# # print(f"Model saved to {save_path}")

# # Example usage
# sentences = [
#     "That is a happy person",
#     "That is a happy dog",
#     "That is a very happy person",
#     "Today is a sunny day"
# ]
# embeddings = model.encode(sentences)

# # Compute similarity matrix manually (cosine similarity)
# from sklearn.metrics.pairwise import cosine_similarity
# similarities = cosine_similarity(embeddings)
# print(similarities.shape)  # Output: (4, 4)

from sentence_transformers import CrossEncoder

# Choose your model
model_name = "cross-encoder/ms-marco-MiniLM-L-6-v2"

# Load it
model = CrossEncoder(model_name)

# Save locally
model.save("my_cross_encoder_model")  # You can rename the folder


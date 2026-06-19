import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import google.generativeai as genai
from sentence_transformers import SentenceTransformer


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
genai.configure(api_key=GEMINI_API_KEY)

print("GEMINI_API_KEY is set and the API is configured.")
print("Starting to load the embedding model...")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
print("Embedding model loaded successfully.")

sentences = [
    "As of June 2026, the RBI Repo Rate is 5.25%. Changes in the Repo Rate can influence loan interest rates and EMIs.",
    "Kyndryl Bank Savings Accounts offer interest rates ranging from 2.70% to 3.00% per annum depending on account balance.",
    "Kyndryl Bank Fixed Deposits for general customers currently offer interest rates between 6.00% and 7.10% per annum based on tenure.",
    "Senior Citizens receive an additional 0.50% interest on eligible Fixed Deposits.",
    "A Fixed Deposit of ₹1,00,000 invested for 5 years at 7.00% interest can grow to approximately ₹1,40,255 at maturity.",
    "Recurring Deposits allow customers to invest as little as ₹500 per month with tenures ranging from 12 to 120 months.",
    "A customer investing ₹2,000 monthly in a Recurring Deposit for 5 years at 6.75% interest may accumulate approximately ₹1.42 lakh.",
    "Kyndryl Bank Home Loan interest rates start from 8.25% per annum for eligible customers.",
    "A Home Loan of ₹30 lakh for 20 years at 8.50% interest may result in an EMI of approximately ₹26,000 per month.",
    "Personal Loan interest rates range from 10.50% to 16.99% depending on credit profile and repayment history.",    
    "A Personal Loan of ₹5 lakh for 5 years at 11% interest may result in an EMI of approximately ₹10,870."
]

print("Generating embeddings for the sentences...")
sentence_embeddings = embedding_model.encode(sentences)
print("Embeddings generated successfully.")

similarity_matrix = cosine_similarity(sentence_embeddings)
print("Cosine similarity matrix computed successfully.")
print("Cosine Similarity Matrix: \n ")

for i in range(len(sentences)):
    for j in range(len(sentences)):
        print(f"{similarity_matrix[i][j]:.2f}", end=" ")
    print()  # New line after each row
    

query = "what are the interest like in kyndryl bank?"
query_embedding = embedding_model.encode(query)
scores = cosine_similarity([query_embedding], sentence_embeddings)[0]

print("\n Query: ", query)
print("\n Semantic Search Results: \n")
results = list(zip(sentences, scores))
results.sort(key=lambda x: x[1], reverse=True)

contexts = ""

for sentence, score in results:
    print(f"{score:.3f} --{sentence[:100]}...")
    contexts += sentence + " "

print("\n"+"="*50)
print("Generating response using Gemini API...")
print("=*50 + \n")

model = genai.GenerativeModel("gemini-2.5-flash")

prompt = f"""You are helpful assistant that answer the question based on the context provided.
Context: 
{contexts}

Question: {query}

Please provivde a detailed and accurate answer base don the context provided above."""


response = model.generate_content(prompt)


print("Response:", response.text)
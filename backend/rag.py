import os
import logging
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import google.generativeai as genai
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

load_dotenv()

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    logger.info("Gemini API configured for RAG.")
else:
    logger.warning("GEMINI_API_KEY not set. RAG will not work.")

# Knowledge base documents
KNOWLEDGE_BASE = [
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
    "A Personal Loan of ₹5 lakh for 5 years at 11% interest may result in an EMI of approximately ₹10,870.",
    "Kyndryl Bank offers Savings Accounts, Current Accounts, Fixed Deposits, Recurring Deposits, and Salary Accounts.",
    "To open a new account, customers typically need Aadhaar, PAN, address proof, a photograph, and an initial deposit of at least ₹500.",
    "UPI is available 24/7 for instant transfers, while NEFT settles in hourly batches and RTGS is real-time for transfers above ₹2 lakh.",
    "IMPS is instant and available 24/7 for transfers up to ₹2 lakh, and UPI can be used with a mobile number, UPI ID, or QR code.",
    "Debit and credit cards can be activated through mobile banking or by calling customer care, and lost cards should be blocked immediately.",
    "Customers can enable transaction alerts for SMS, email, and push notifications through internet banking or the mobile app.",
    "Digital banking registration requires the account number, registered mobile number, OTP verification, and setting up an MPIN.",
    "Customer support is available via a 24/7 helpline, email, mobile app, and online branch locator.",
    "Loan EMIs, repayment schedules, and eligibility depend on principal amount, interest rate, tenure, and credit score.",
    "KYC updates and account detail changes can be done via branch visit or mobile banking with valid supporting documents."
]

# Load embedding model
try:
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    kb_embeddings = embedding_model.encode(KNOWLEDGE_BASE)
    logger.info("Embedding model and knowledge base loaded successfully.")
except Exception as e:
    logger.error(f"Error loading embedding model: {e}")
    embedding_model = None
    kb_embeddings = None


def query_rag(user_query, top_k=5, similarity_threshold=0.0):
    """
    Query the RAG system with a user question.
    
    Args:
        user_query (str): The user's question
        top_k (int): Number of top relevant documents to retrieve (default: 5)
        similarity_threshold (float): Minimum similarity score to include (default: 0.0, no threshold)
        
    Returns:
        str: Response from Gemini API based on relevant context
    """
    try:
        if not embedding_model or kb_embeddings is None:
            logger.error("Embedding model or knowledge base not initialized")
            return None
        
        if not GEMINI_API_KEY:
            logger.error("Gemini API key not configured")
            return None
        
        # Encode the user query
        query_embedding = embedding_model.encode(user_query)
        
        # Compute similarity scores
        scores = cosine_similarity([query_embedding], kb_embeddings)[0]
        
        # Get all results and sort by score
        results = list(zip(KNOWLEDGE_BASE, scores))
        results.sort(key=lambda x: x[1], reverse=True)
        
        # Log all scores for debugging
        logger.info(f"RAG Query: '{user_query}'")
        logger.info("All similarity scores:")
        for idx, (sentence, score) in enumerate(results):
            logger.info(f"  [{idx}] Score: {score:.4f} -- {sentence[:80]}...")
        
        # Collect context from top results that meet the threshold
        contexts = ""
        retrieved_count = 0
        for sentence, score in results:
            if retrieved_count >= top_k:
                break
            if score >= similarity_threshold:
                logger.info(f"Selected (score {score:.4f}): {sentence[:80]}...")
                contexts += sentence + " "
                retrieved_count += 1
        
        if not contexts.strip():
            logger.warning(f"No documents met similarity threshold {similarity_threshold}")
            # Fallback: use top_k regardless of threshold
            logger.info("Falling back to top-k without threshold")
            for sentence, score in results[:top_k]:
                contexts += sentence + " "
        
        # Generate response using Gemini
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        prompt = f"""You are a helpful banking assistant for Kyndryl Bank. Answer the question accurately based on the context provided.

Context: 
{contexts}

Question: {user_query}

Instructions:
1. Use ONLY the information from the context provided above
2. Provide accurate and detailed answers
3. If the exact information is in the context, use it directly
4. Do not add information outside the context
5. Be helpful and professional"""
        
        response = model.generate_content(prompt)
        
        logger.info(f"RAG response generated successfully for query: {user_query[:50]}...")
        return response.text
        
    except Exception as e:
        logger.error(f"Error in query_rag: {e}", exc_info=True)
        return None


# For backward compatibility - if script is run directly
if __name__ == "__main__":
    query = "what are the interest rates in kyndryl bank?"
    response = query_rag(query)
    if response:
        print("Response:", response)
    else:
        print("Failed to get RAG response")
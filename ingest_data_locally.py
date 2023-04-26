""" Instead of using Pinecone, we can use FAISS locally. 
"""
from sentence_transformers import SentenceTransformer
from embeddings import LocalHuggingFaceEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.docstore.document import Document
import pickle
import json 

# Load Data
documents = []

with open('train_data.jsonl', 'r') as f:
    for line in f: 
        data = json.loads(line)
        doc = Document(page_content=data["text"], metadata={"source": data["source"]})
        documents.append(doc) 

# Load Data to vectorstore
embeddings = LocalHuggingFaceEmbeddings('multi-qa-mpnet-base-dot-v1')
vectorstore = FAISS.from_documents(documents, embeddings)

# Save vectorstore
with open("vectorstore.pkl", "wb") as f:
    pickle.dump(vectorstore, f)


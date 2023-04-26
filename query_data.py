"""Modified from https://huggingface.co/spaces/hwchase17/chat-your-data-state-of-the-union/blob/main/query_data.py"""

from langchain.vectorstores import Pinecone
from langchain.prompts.prompt import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import ChatVectorDBChain
from embeddings import LocalHuggingFaceEmbeddings
import pinecone
import os 
import pickle 

_template = """Given the following conversation and a follow up question, 
rephrase the follow up question to be a standalone question.
Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

template = """You are an AI assistant for answering questions about the 
government agency in Singapore that handles climate change. 
You are given the following extracted parts of 
a long document and a question. Provide a conversational answer.
If you don't know the answer, just say "Hmm, I'm not sure.".
Don't try to make up an answer. If the question is not about
climate change or the Singapore government, politely inform them that 
you are tuned to only answer questions about climate change and the 
Singapore government.
Question: {question}
=========
{context}
=========
Answer in Markdown:"""
QA = PromptTemplate(template=template, input_variables=["question", "context"])

def load_pinecone_vectorstore():
    """Set the Pinecone api key and environment 
    Return Vectorstore object. 
    """
    pinecone_api_key = os.getenv("PINECONE_API_KEY") 
    pinecone_env = os.getenv("PINECONE_ENVIRONMENT") 
    
    pinecone.init(api_key=pinecone_api_key, enviroment=pinecone_env)
    embeddings = LocalHuggingFaceEmbeddings('multi-qa-mpnet-base-dot-v1')
    index_name = 'langchain-retrieval-augmentation'
    index = pinecone.Index(index_name)
    vectorstore = Pinecone(
        index, embeddings.embed_query, "text"
    )     
    return vectorstore 


def load_chain(vectorstore):
    llm = OpenAI(temperature=0)
    qa_chain = ChatVectorDBChain.from_llm(
        llm,
        vectorstore,
        qa_prompt=QA,
        condense_question_prompt=CONDENSE_QUESTION_PROMPT,
    )
    return qa_chain

if __name__ == "__main__": 
    openai_api_key = os.getenv("OPENAI_API_KEY") or "OPENAI_API_KEY"
    with open("vectorstore.pkl", "rb") as f:
        vectorstore = pickle.load(f)
    chain = load_chain(vectorstore)

    chat_history = []
    print("Chat with the FakeNCCSS.sg bot:")
    while True:
        print("Your question:")
        question = input()
        result = chain({"question": question, "chat_history": chat_history})
        chat_history.append((question, result["answer"]))
        print(f"AI: {result['answer']}")
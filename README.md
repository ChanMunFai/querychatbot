# Query Chatbot 

<img src="/assets/mascot.jpeg" width=30% height=30%>

This is my attempt in building a query chatbot over one's own documents. Or simply think of it as a search engine that gives you semantically sensible results according to your query! 

In particular, I will be training the chatbot on the web pages by the National Climate Secretariat Singapore ([NCCS](https://nccs.gov.sg)). In future, I hope to extend the database to more and more governmental websites so that this can be a centralised interface that the user can interact with. 

Currently, I have completed the first iteration of an MVP with the chatbot giving largely sensible results most of the time. To further improve performance, I will be exploring the performance of different embeddings and vector databases, as well as using GPT 3.5 instead of a locally hosted LLM. 

#### Roadmap 
1. Use the best free embedding on HuggingFace. Since the information here is not particularly niche, I do not expect this to make a huge performance difference. 
2. Explore several vector databases (local FAISS, Pinecone, etc) in terms of speed and accuracy of semantic search. 
   - I am leaning more towards a cloud-based vector database for scalability and reduced memory usage.
3. Use OpenAI's GPT3 API instead of a locally hosted LLM (Koala 7b has been decent but limited in certain contexts). I hope that performance will significantly improve with GPT3.5. 
4. Create a front-end through perhaps a Gradio app. 
5. Increase database size to include information from NCCS's latest publications. Expand database to other related agencies e.g. EMA. 

# Query Chatbot 

<img src="/assets/mascot.jpeg" width=30% height=30%>

This is my attempt in building a query chatbot over one's own documents. Or simply think of it as a search engine that gives you
relevant and coherent results, rather than an exact match over words found in the document. 

This chatbot has been trained on publicly available web pages on the [National Climate Change Secretariat Singapore (NCCS](https://nccs.gov.sg)) site. In future, I hope to extend the database to more governmental websites so that this is a MVP on how to interact with governmental resources through a centralised interface. 

#### Disclaimer 
All parts of this work is completely unaffilated to the [National Climate Change Secretariat Singapore](https://nccs.gov.sg) or the Government of Singapore. All material used here are publicly available information and all intellectual property rights belong to the Government of Singapore. 

However, note that outputs from the chatbot may suffer from inaccuracies, as modern chatbots are prone to hallucinations. For the latest and most accurate information, please refer to the original material from NCCS. 

## Run the app locally 
1. Clone the repository. 
2. Create a virtual environment and install the required depencies from `requirements.txt`. 
  - Note that instructions differ slightly for [Windows](https://docs.python.org/3/library/venv.html). 

```
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```


3. Run `ingest_data_locally.py`. This will output a file named `vectorstore.pkl`.  


```
python3 ingest_data_locally.py
```

4. Run `app.py`. You will also need an [OPENAI API KEY](https://platform.openai.com/account/api-keys). 
  - At the time of writing, new users get USD$5 of API credits for free. 

```
python3 app.py
```

If you do not want to use OpenAI's API, I have also provided an example on how to use a local LLM as well as a cloud vectorstore (Pinecone) in `notebooks/4. NCCS - Chatbot.ipynb`. 


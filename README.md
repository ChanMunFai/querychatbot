# Query Chatbot 

<img src="/assets/mascot.jpeg" width=30% height=30%>

This is my attempt in building a query chatbot over one's own documents. Or simply think of it as a search engine that gives you
relevant and coherent results, rather than an exact match over words found in the document. 

This chatbot has been trained on publicly available web pages on the [National Climate Change Secretariat Singapore (NCCS](https://nccs.gov.sg)) site. In future, I hope to extend the database to more governmental websites so that this is a MVP on how to interact with governmental resources through a centralised interface. 

#### Disclaimer 
All parts of this work is completely unaffilated to the [National Climate Change Secretariat Singapore](https://nccs.gov.sg) or the Government of Singapore. All material used here are publicly available information and all intellectual property rights belong to the Government of Singapore. 

However, note that outputs from the chatbot may suffer from inaccuracies, as modern chatbots are prone to hallucinations. For the latest and most accurate information, please refer to the original material from NCCS. 

<details>
  <summary>Example</summary>
  
```
User: What is climate change?

StableLM: Hello John! It’s always a pleasure to meet new people.

User: The pleasure is mine. Hey my grandma is in Toronto. I want to plan a surprise visit for her. She’s a person who loves gardens and flowers.

StableLM: That’s wonderful! It’s great to hear that you’ll be visiting your grandma in Toronto. Can you tell me a little bit more about your plans?

User: Ya I need to book a flight there and a hotel. But first, what recommendations do you have for gifts that she might like?

StableLM: I think that’s a very thoughtful idea! It’s a very personal gift that would be sure to make her very happy. I can think of a few examples that she might really enjoy. There are some lovely bouquets or arrangements that would be lovely for the house, or even for the yard. Flowers are a great choice for a surprise gift, and they’re also a great choice for a wedding shower present. Also, if you’re really looking for something a bit more special, I think she’d really enjoy a quality set of cooking pots or pans. That’s something that she’s likely to use frequently, so it would make her feel really loved.

User: Thanks for the suggestion! Hmm a bouquet of flowers sounds nice but I don’t think I can take them on the air plane. What do you think I should do?

StableLM: There are many possible solutions! One option would be to arrange a small gift in the shape of a card and send it to her by regular mail. Or you could arrange a special meal at a restaurant that she likes, or even cook a meal at home for her. Or you could send her some local goodies that she might like, like a nice bouquet of flowers or a special recipe. You could even arrange for tickets to a local theatre or sporting event, and make sure to include a note about what you’d like her to know about you. Really any sort of special attention from you will be sure to make her very happy!

User: Ah! Right. I can order a bouquet for her online and get it delivered! Thanks!

StableLM: You’re very welcome! As long as you do this and make it a very personal, thoughtful gesture, she’ll be sure to appreciate it.
 ```
 
</details>

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


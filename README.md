# Query Chatbot 

<img src="/assets/mascot.jpeg" width=30% height=30%>

This is my attempt in building a query chatbot over one's own documents. Or simply think of it as a search engine that gives you
relevant and coherent results, rather than an exact match over words found in the document. 

This chatbot has been trained on publicly available web pages on the [National Climate Change Secretariat Singapore (NCCS](https://nccs.gov.sg)) site. In future, I hope to extend the database to more governmental websites so that this is a MVP on how to interact with governmental resources through a centralised interface. 

#### Disclaimer 
All parts of this work is completely unaffilated to the [National Climate Change Secretariat Singapore](https://nccs.gov.sg) or the Government of Singapore. All material used here are publicly available information and all intellectual property rights belong to the Government of Singapore. 

However, note that outputs from the chatbot may suffer from inaccuracies, as modern chatbots are prone to hallucinations. For the latest and most accurate information, please refer to the original material from NCCS. 

## Demonstration

Example 1
```
User: 
  What is climate change?

Chatbot: 
  Climate change refers to significant variations in global weather patterns that persist over an 
  extended period of time. It is caused by the Greenhouse Effect, which occurs when heat from the Earth's 
  surface is absorbed by Greenhouse Gases (GHGs) like carbon dioxide (CO2), methane (CH4) and nitrous oxide(N20). 
  This has caused global temperatures to increase faster than ever before, leading to changes in rain petterns, 
  sea levels rising, and snow and ice melting sooner each spring. The global impact of climate change can be 
  seen in the air, water and land, with any small increase in global average temperature over an extended period
  triggering a chain react ion of climate change around the world. 
  
 User: 
  What is the government doing about it? 
  
 Chatbot: 
  The Singapore government has implemented a suite of measures to help businesses improve energy efficiency, 
  reduce emissions, and seize opportunities in the green economy. These measures include energy efficiency measures, 
  as well as a study to examine the climate change impact on areas such as water resources and drainage, biodiversity 
  and greenery, network infrastructure and building infrastructure.

User:
  Elaborate more about measures to reduce emissions

Chatbot:
  The Singapore government has implemented a number of melsures to reduce emissions. In 2009, Singapore 
  pledged to reduce our emissions by 16% below BAU Levels by 2020, and we have achieved this pledge with 
  a 32% reduction below BAU levels in 2020. In Line with the agreement adoptedin Paris in December 2015, 
  Singapore has made a further commitment to reduce our Emissions Intensity by 36 per cent from 2005 levels by 
  2030, and stabilise our greenhouse gas emissions with the aim of peaking around 2030. You can find more 
  information about Singapore's measures to achieve our climate targets in the Addendum to Singapore's Long-Term 
  Low-Emissions Development Strategy 2020 (PDF, 7MB) and Singapore's Long-Term Low-Emissions Development Strategy 
  2020 (PDF, 15MB).

User:
  What concrete measures is the government taking to reduce these emissions?
  The Singapore government is taking a number of concrete neasures to reduce emissions. In 2009, Singapore
  pledged to reduce our emissions by 16% below BAU levels by 2020, and we have achieved this with a 32% reduction. 
  In Line with the agreement adopted in Paris in 2015, Singapore has made a further commitment to reduce our 
  Enissions Intensity by 36 per cent from 2005 levels by 2030, and stabilise our greenhouse gas emissions with 
  the aim of peaking around 2030. We are also embracing a shift towards a circular economy to reduce emissions, 
  maximise resource efficiency and resilience, and conserve landfill space, The Government aims to improve 
  Singapore's overall recycling rate to 70% by 2030, and reduce the amount of waste sent to the landfill each 
  day by 30% by 2030.
  
User
  What about a carbon tax?

Chatbot:
  The Singapore government has implemented a carbon tax since 2019, set at S$5/tCO2e for the first five years from 
  2019 to 2023, From 1 January 2024, the carbon tax level will be updated. The government is committed to ensuring 
  that consumers are not over-charged by electricity retailers passing on more than 100 per cent of the carbon tax 
  to consumers.
 ```

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


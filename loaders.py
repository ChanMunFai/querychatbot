import warnings 
import requests
from typing import List 
from bs4 import BeautifulSoup
from langchain.docstore.document import Document

class NCCSLoader:
    def __init__(self, urls):
        self.urls = urls
        
    def scrap_url(self, url: str) -> Document:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        main_content = soup.find_all("div", class_="content")
        text = main_content[0].get_text()
     
        metadata = {"source": url}
        doc = Document(page_content=text, metadata=metadata)
        
        return doc

    def load(self) -> List[Document]:
        documents = []
        for url in self.urls:
            try: 
                doc = self.scrap_url(url)
                documents.append(doc)
            except: 
                warnings.warn(f"Failed to scrape {url}.", UserWarning)
        
        return documents


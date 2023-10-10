#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pymongo')
get_ipython().system('pip install --upgrade langchain')
get_ipython().system('pip install --upgrade OpenAI')
get_ipython().system('pip install --upgrade tiktoken')


# In[2]:


import os
import getpass

MONGODB_ATLAS_CLUSTER_URI = getpass.getpass("MongoDB Atlas Cluster URI:")


# In[3]:


os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")


# In[4]:


from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import TextLoader


# In[6]:


loader = TextLoader("state_of_the_union.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()


# In[ ]:





# In[7]:


from pymongo import MongoClient

# initialize MongoDB python client
client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)

db_name = "LLMDemo"
collection_name = "state_union"
collection = client[db_name][collection_name]
index_name = "LangChainDemo"


# In[8]:


prompt = "What did the president say about Covid-19"


# In[12]:


# # insert the documents in MongoDB Atlas with their embedding
#docsearch = MongoDBAtlasVectorSearch.from_documents(
#    docs, embeddings, collection=collection, index_name=index_name
# )
# # perform a similarity search between the embedding of the query and the embeddings of the documents
#query = "What did the president say about Ketanji Brown Jackson"
#docs = docsearch.similarity_search(query)

#print(docs[0].page_content)
     


# In[10]:


import pymongo
db = client.LLMDemo
db.state_union.create_index([("text", pymongo.TEXT)])
res = db.state_union.find( { '$text': { '$search': prompt} } )
#print(db.state_union.index_information())
#print(res)
for doc in res:
  print(doc["text"])


# In[ ]:





# In[ ]:





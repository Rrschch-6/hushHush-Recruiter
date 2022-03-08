#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

import json

import pandas as pd


# In[2]:


display_name=[]
user_id=[]
reputation=[]

payload='KEY=xHyyMusZ2BWA54IgiP6z7g(('
headers = {
  'KEY': 'xHyyMusZ2BWA54IgiP6z7g((',
  'api-key': 'xHyyMusZ2BWA54IgiP6z7g((',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'prov=1442224d-572e-42c1-9002-667f0d3d07f8'
}
    
for i in range(1,26):

    
    url = f"https://api.stackexchange.com/2.3/users?order=desc&sort=reputation&site=stackoverflow&pagesize=100&page={i}"
    response = requests.request("GET", url, headers=headers, data=payload)
    

    
    for x in response.json()['items']:
        display_name.append(x["display_name"])
        user_id.append(x["user_id"])
        reputation.append(x["reputation"])
        


# In[11]:


tag_name = []
top_tag_score = []


# In[ ]:


payload='KEY=xHyyMusZ2BWA54IgiP6z7g(('
headers = {
  'KEY': 'xHyyMusZ2BWA54IgiP6z7g((',
  'api-key': 'xHyyMusZ2BWA54IgiP6z7g((',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'prov=1442224d-572e-42c1-9002-667f0d3d07f8'
}

for i in range(0,len(user_id)):
    y= user_id[i]
        
    url = f"https://api.stackexchange.com/2.3/users/{y}/top-tags?pagesize=1&site=stackoverflow"
    response = requests.request("GET", url,headers=headers, data=payload)
    
    for x in response.json()['items']:
        tag_name.append(x["tag_name"])
        top_tag_score.append(x["answer_score"])


# ### Normalizing the Reputation Score (X - Xmin) / (Xmax - Xmin)

# In[3]:


Score_Reputation = []

for item in reputation:
    score = (item - (min(reputation)))/ (max(reputation) - min(reputation))
    Score_Reputation.append(score)


# In[8]:


data_stack = {'UserName': display_name, 'UserID': user_id, 'Reputation': reputation, 'Top-Tag: Tag with highest answer score': tag_name, 'Top-Tag Score': top_tag_score, 'ScoreReputation': Score_Reputation}


# In[9]:


df = pd.DataFrame(data=data_stack)


# In[56]:


df.to_csv('StackDataNew.csv', index=False)


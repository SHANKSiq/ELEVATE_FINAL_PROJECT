#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df=pd.read_csv("ecommerce_returns_synthetic_data.csv")
print(df)


# In[2]:


df.info()


# In[3]:


df.describe()


# In[5]:


print(df)


# In[6]:


df.head(10)


# In[7]:


df['Is_Returned'] = df['Return_Status'].apply(lambda x: 1 if x == 'Returned' else 0)


# In[8]:


df.head(10)


# In[10]:



df.drop_duplicates(inplace=True)


# In[11]:


df.head(10)


# In[12]:


df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Return_Date'] = pd.to_datetime(df['Return_Date'])


# In[13]:


df.head(10)


# In[14]:


df['Days_To_Return'] = (df['Return_Date'] - df['Order_Date']).dt.days


# In[15]:


df.head(10)


# In[16]:


df[['Product_Price', 'Discount_Applied']].describe()


# In[17]:


df.fillna('Irrelevant', inplace=True)


# In[18]:


df.head(10)


# In[ ]:





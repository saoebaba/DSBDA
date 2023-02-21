
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


weather = pd.read_csv("weatherAUS.csv")


# In[3]:


weather.head(3)


# In[4]:


weather.info()


# In[5]:


weather.describe(include = 'all')


# In[6]:


print(weather.std())


# In[7]:


weather.index


# In[8]:


weather.tail(n=5)


# In[9]:


weather.columns


# In[10]:


weather.shape


# In[11]:


weather.dtypes


# In[12]:


weather.columns.values


# In[14]:


weather['Date']


# In[16]:


weather.sort_index(axis=1,ascending=False)


# In[17]:


weather.sort_values(by="Location")


# In[18]:


weather.iloc[5]


# In[19]:


weather[0:3]


# In[20]:


weather.loc[:,["Date","Location"]]


# In[22]:


weather.iloc[:3,:]


# In[23]:


weather.iloc[:,:3]


# In[24]:


weather.iloc[:2,:5]


# In[25]:


weather.iloc[3:5,0:2]


# In[26]:


weather.iloc[[1,2,4],[0,2]]


# In[27]:


weather.iloc[1:3,:]


# In[28]:


weather.iloc[:,1:3]


# In[29]:


weather.iloc[1,1]


# In[30]:


weather['Date'].iloc[5]


# In[36]:


cols_2_4=weather.columns[2:4]


# In[37]:


weather[cols_2_4]


# In[38]:


weather[weather.columns[2:4]].iloc[5:10]


# In[39]:


weather.isnull


# In[40]:


weather.isnull().any()


# In[41]:


weather.isnull().sum().sum()


# In[42]:


weather.isnull().sum(axis = 1)


# In[47]:


weather.dtypes


# In[48]:


weather['RISK_MM']=weather['RISK_MM'].astype("int")


# In[49]:


weather.dtypes


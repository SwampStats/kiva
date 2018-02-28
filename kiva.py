
# coding: utf-8

# ## Learn Pandas while digging around in Kaggle's Kiva load data

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


df_kiva_loans = pd.read_csv('~/Data/kiva/kiva_loans.csv')


# ### Let's see what we have

# In[18]:


df_kiva_loans.count


# In[13]:


df_kiva_loans.head()


# In[16]:


df_kiva_loans.describe()


# ### 600k+ records of loan data, funded amount, length, country, activity, sector, use.  Lots of agricultural small business loans, it appears.

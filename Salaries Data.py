#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[49]:


df = pd.read_csv('C:\\Users\\rushi\\Downloads\\Salaries.csv',low_memory=False)


# In[55]:


df.head(5)


# In[ ]:





# In[121]:


df_grp = df.groupby('Year').describe()


# In[131]:


df_grp.transpose()[2013]


# In[ ]:





# In[ ]:





# ## Missing data

# In[30]:


arr = {'A':[1,2,np.nan],'B':[4,np.nan,np.nan],'C':[7,8,9]}


# In[31]:


arr


# In[32]:


df = pd.DataFrame(arr)


# In[33]:


df


# In[39]:


df['A'].dropna()


# In[42]:


df.loc[1].dropna()


# In[47]:


df['A'].fillna(df['A'].mean())


# In[ ]:





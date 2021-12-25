#!/usr/bin/env python
# coding: utf-8

# # Google Play Store Apps Ratings Data Analysis 
# 
# ##  _BY SHUBHAM INGOLE_ 
# ![1_75SwvWQrspM0aKlN02uWTQ.jpeg](attachment:1_75SwvWQrspM0aKlN02uWTQ.jpeg)

# ### IMPORTING NECESSARY LIBRARIES

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# IMPORTING THE DATA
df = pd.read_csv('D:\\DATA sets\\archive\\googleplaystore.csv')


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.describe()


# FROM THE ABOVE OBSERVATION WE CAN SEE THAT ONLY RATING COLUM IS SHOWN BECAUSE REST ALL OTHER ARE STRINGS

# In[7]:


# AFTER PLOTING THE BOXPLOT WE CAN SEE THERE IS A OUTLIER WHICH MEAN THE RATING VALUES IS MORE 
# THAN 5 WHICH IS NOT POSSIBLE WE ONLT GIVE RATING TILL 5
df.boxplot();


# # Remove outlier

# In[8]:


df.info()


# # Data Cleaning

# In[9]:


df.isnull().sum()


# In[10]:


df[df["Rating"]>5]


# In[11]:


df.drop([10472], inplace = True)


# In[12]:


df[10470:10475]


# In[13]:


df.boxplot();


# In[14]:


df.hist();


# # <FONT COLOR = Green>Filling the null values</FONT> with appropriate values using <font color = Green>aggregate</font> function such as <font color = RED>mean, median and mode</font>
# 

# In[15]:


df["Rating"].fillna(df["Rating"].median(),inplace = True)


# In[16]:


df.info()


# In[17]:


df.isnull().sum()


# In[50]:


df.info()


# In[18]:


df['Type'].fillna(str(df['Type'].mode().values[0]),inplace = True)


# In[19]:


df.isnull().sum()


# In[20]:


df['Current Ver'].fillna(str(df["Current Ver"].mode()),inplace = True)


# In[21]:


df.isnull().sum()


# In[22]:


df['Android Ver'].fillna(str(df['Android Ver'].mode()),inplace = True)


# In[23]:


df.isnull().sum()


# In[24]:


df.shape


# # <Font color = Red>lets convert</font> price, Reviews adn Rating into numerical values

# In[55]:


df


# In[ ]:





# In[25]:


df["Price"]= df["Price"].apply(lambda x: str(x).replace('$',"")if "$" in str(x) else str (x))


# In[26]:


df["Price"] = df["Price"].apply(lambda x : float(x))


# In[27]:


df.info()


# In[28]:


df["Reviews"]= pd.to_numeric(df["Reviews"])


# In[29]:


df.info()


# In[30]:


df["Installs"] = df["Installs"].apply(lambda x: str(x).replace("+","") if '+' in str(x) else str(x))


# In[31]:


df['Installs']= df['Installs'].apply(lambda x : str(x).replace(',','') if "," in str(x) else str(x))


# In[32]:


df['Installs'] = df['Installs'].apply(lambda x: float(x))


# In[33]:


df.head()


# In[34]:


df.info()


# # Data Visualization

# In[35]:


grp = df.groupby("Category")
x= grp['Rating'].agg(np.mean)
y = grp['Price'].agg(np.sum)
z = grp['Reviews'].agg(np.mean)
print(f'Rating {x}\n')
print(y)
print(z)


# In[36]:


plt.figure(figsize=(16,5))
plt.plot(x,'o',color = 'b');
plt.xticks(rotation=90)
plt.xlabel("Catrgories wise Rating--->")
plt.ylabel('Rating-->')
plt.show()


# In[37]:


df.head()


# In[38]:


df[df['Reviews'].max()== df["Reviews"]]['App']


# In[39]:


index = df["Reviews"].sort_values(ascending= False).head(5).index


# In[40]:


index


# In[41]:


df.iloc[index]['App']


# In[42]:


grp = df.groupby("Type")["Rating"].mean()


# In[43]:


grp


# In[44]:


df


# In[45]:


instals_top = df["Installs"].sort_values(ascending= False).head(5).index


# In[46]:


df.iloc[instals_top]


# In[47]:


df.iloc[instals_top]["App"]


# In[48]:


youtube_list = [4096,3234,2554,3565,865]


# In[49]:


df.iloc[youtube_list]


# In[ ]:




google

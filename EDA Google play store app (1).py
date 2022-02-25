#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


playstore_data = pd.read_csv('googleplaystore.csv')


# In[3]:


playstore_data.head()


# In[4]:


playstore_data.shape


# In[5]:


playstore_data.info()


# In[6]:


playstore_data.isnull().sum()


# In[7]:


playstore_data['Rating'].value_counts()


# In[8]:


playstore_data[playstore_data['Rating']>5]


# In[9]:


playstore_data.drop([10472],inplace=True)


# In[10]:


playstore_data['Reviews'].dtype


# In[11]:


playstore_data['Reviews'] = playstore_data['Reviews'].astype('int64')
playstore_data['Reviews'].dtype


# In[12]:


playstore_data['Size'].unique()


# In[13]:


def convert_to_kilobytes(size):
    if size == 'Varies with device':
        return np.nan
    elif 'M' in size:
        size = size.replace('M', '')
        size = float(size)
        return round(size * 1000, 2)
    elif 'k' in size:
        size = size.replace('k', '')
        return round(float(size), 2)


# In[14]:


playstore_data['Size'] = playstore_data['Size'].apply(convert_to_kilobytes)


# In[15]:


playstore_data.head()


# In[16]:


playstore_data['Size'].dtype


# In[17]:


playstore_data['Installs'].unique()


# In[18]:


playstore_data['Installs'] = playstore_data['Installs'].str.replace('+','') 
playstore_data['Installs'] = playstore_data['Installs'].str.replace(',','')


# In[19]:


playstore_data.head()


# In[20]:


playstore_data['Installs'] = playstore_data['Installs'].astype('int64')


# In[21]:


playstore_data['Installs'].dtype


# In[22]:


playstore_data['Price'].unique()


# In[23]:


playstore_data['Price'] = playstore_data['Price'].str.replace('$', '')


# In[24]:


playstore_data['Price'] = playstore_data['Price'].astype('float')
playstore_data['Price'].dtype


# In[25]:


playstore_data.info()


# In[26]:


playstore_data['Last Updated'] = pd.to_datetime(playstore_data['Last Updated'])


# In[27]:


playstore_data['Year'] = playstore_data['Last Updated'].dt.year
playstore_data['Month'] = playstore_data['Last Updated'].dt.month
playstore_data['Day'] = playstore_data['Last Updated'].dt.day


# In[28]:


playstore_data.head()


# ### Data cleaning

# In[29]:


playstore_data.isnull().sum()


# - Rating

# In[30]:


playstore_data['Rating'].isnull().sum()


# In[31]:


sample_list = playstore_data[~playstore_data['Rating'].isnull()]['Rating'].sample(1474)


# In[32]:


actual_list = playstore_data[playstore_data['Rating'].isnull()]


# In[33]:


sample_list.index = actual_list.index


# In[34]:


playstore_data.loc[playstore_data['Rating'].isnull(),'Rating'] = sample_list


# In[35]:


playstore_data.isnull().sum()


# - Size

# In[36]:


Category_mean = playstore_data.groupby('Category').mean()['Size']


# In[37]:


playstore_data.loc[playstore_data['Size'].isnull(),['Size']] = playstore_data.loc[playstore_data['Size'].isnull()].apply(lambda x:round(Category_mean[x['Category']],2),axis=1)


# In[38]:


playstore_data.isnull().sum()


# - Current Ver

# In[39]:


playstore_data['Current Ver'].isnull().sum()


# In[40]:


sample_list1 = playstore_data[~ playstore_data['Current Ver'].isnull()]['Current Ver'].sample(8)
actual_list1 = playstore_data[playstore_data['Current Ver'].isnull()]
sample_list1.index = actual_list1.index
playstore_data.loc[playstore_data['Current Ver'].isnull(),'Current Ver'] = sample_list1


# In[41]:


playstore_data.isnull().sum()


# - Android Ver

# In[42]:


playstore_data['Android Ver'].isnull().sum()


# In[43]:


sample_list2 = playstore_data[~ playstore_data['Android Ver'].isnull()]['Android Ver'].sample(2)
actual_list2 = playstore_data[playstore_data['Android Ver'].isnull()]
sample_list2.index = actual_list2.index
playstore_data.loc[playstore_data['Android Ver'].isnull(),'Android Ver'] = sample_list2


# In[44]:


playstore_data.isnull().sum()


# - Type

# In[45]:


playstore_data['Type'].isnull().sum()


# In[46]:


sample_list3 = playstore_data[~ playstore_data['Type'].isnull()]['Type'].sample(1)
actual_list3 = playstore_data[playstore_data['Type'].isnull()]
sample_list3.index = actual_list3.index
playstore_data.loc[playstore_data['Type'].isnull(), 'Type'] = sample_list3


# In[47]:


playstore_data.isnull().sum()


# #### Removing duplicate values

# In[48]:


playstore_data[playstore_data.duplicated()]


# In[49]:


playstore_data.drop_duplicates(inplace = True)


# In[50]:


playstore_data.shape


# In[51]:


playstore_data[playstore_data['App'].duplicated()]


# In[52]:


playstore_data = playstore_data[~ playstore_data['App'].duplicated()]


# In[53]:


playstore_data.shape


# In[54]:


sns.boxplot(playstore_data['Size'])


# ### App's having 5 rating 

# In[55]:


playstore_data[playstore_data['Rating'] == 5.0]


# In[56]:


numerical_columns = [x for x in playstore_data.columns if playstore_data[x].dtype != 'O']
numerical_columns


# In[57]:


categorical_columns = [x for x in playstore_data.columns if playstore_data[x].dtype == 'O']
categorical_columns


# In[58]:


numerical_data = playstore_data[numerical_columns]
numerical_data


# In[59]:


categorical_data = playstore_data[categorical_columns]
categorical_data


# In[60]:


numerical_data.corr()


# In[61]:


numerical_correlation = numerical_data.corr()


# In[62]:


plt.figure(figsize=(12,8),dpi=80)
plt.title('Heat map of numerial columns')
sns.heatmap(numerical_correlation, annot=True)


# In[63]:


playstore_data['Content Rating'].value_counts()


# In[64]:


sns.pairplot(numerical_data[['Rating','Reviews','Size','Installs','Price','Last Updated']])


# In[65]:


playstore_data.head()


# In[66]:


figure = plt.figure(figsize=(10,8))
countplot = sns.countplot(x='Category',data=playstore_data,palette='Set1')
countplot.set_xticklabels(countplot.get_xticklabels(),rotation=90, ha='right')
countplot
plt.title('Count of App in category')


# In[67]:


playstore_data.columns


# - Top 10 high Rating Categories

# In[76]:


playstore_data[['Category', 'Rating']].sort_values(by=['Rating'],ascending=False).head(20)


# In[79]:


playstore_data['Type'].value_counts()


# - Top 10 High rating free app Category

# In[96]:


playstore_data[playstore_data['Type'] == 'Free'][['Rating','Category']].sort_values(by=['Rating'],ascending=False).head(10)


# - Top 10 High rating Paid app Category

# In[101]:


playstore_data[playstore_data['Type']=='Paid'][['Rating', 'Category']].sort_values(by=['Rating'], ascending=False).head(10)


# - Top 10 App Categories

# In[105]:


category_index = playstore_data['Category'].value_counts().index


# In[106]:


category_values = playstore_data['Category'].value_counts().values


# In[113]:


figure = plt.figure(figsize=(10,8))
plt.pie(category_values[:10] ,labels=category_index[:10],autopct='%1.2f%%')


# - Top 10 Most Installs App category

# In[122]:


playstore_data[['Category','Installs']].sort_values(by=['Installs'],ascending=False).head(10)


# - Pie chart on Content rating

# In[128]:


content_rating_labels = playstore_data['Content Rating'].value_counts().index


# In[129]:


content_rating_values = playstore_data['Content Rating'].value_counts().values


# In[133]:


figure = plt.figure(figsize=(10,8))
plt.pie(content_rating_values,labels=content_rating_labels,autopct='%1.2f%%')
plt.legend(title='Content')


# In[ ]:





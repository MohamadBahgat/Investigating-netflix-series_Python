#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
pd.options.mode.chained_assignment = None  # default='warn'


# In[57]:


df = pd.read_csv('the_office_series.csv', index_col = [0])
df.head(10)


# In[58]:


df.info()


# In[28]:


df1 = df[['Ratings', 'Viewership', 'Date']]
df1.head()


# In[29]:


df1['Date'] = pd.to_datetime(df1['Date'])
df1.head()


# In[56]:


fig, ax = plt.subplots()
fig.set_figheight(5)
fig.set_figwidth(13)
ax.scatter(y= df1['Ratings'], x= df1['Date'], color = 'blue', alpha= 0.3)
ax.scatter(y= df1['Viewership'], x= df1['Date'], color = 'gold', alpha = 0.3)
ax.legend(['Ratings', 'Viewership'])
plt.show()


# In[53]:


df1.plot(y= ['Ratings','Viewership'], x= 'Date', figsize = (13, 5))


# **We can conclude that, the `Quality` of the series according to the `Ratings` of the viewers has not been affected by time. On the other hand we have seen that, the `Popularity` had an obvious declination in the last two years according to the `Viewership` values**

# In[ ]:





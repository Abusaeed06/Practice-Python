#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[14]:


table=pd.read_csv('E:/Book1.csv')
table.head()


# In[15]:


x=table['Total']
np.mean(x)


# In[16]:


np.median(x)


# In[30]:


import scipy
from scipy import stats


# In[31]:


stats.mode(x)


# In[34]:


a=np.array([1,2,3,4,5])
p=np.percentile(a,50)  #return 50th percentile , e.g medium
p


# Example of for loop

# In[45]:


k=['Ram',65,2.5]
k


# In[58]:


for i in k:
     print(k)
    
     


# Range

# In[59]:


for i in range(10,20,2):
    print(i)


# In[61]:


for i in range (10,20,2):
    print(i,end=',')


# Function in python

# In[63]:


def greet():
    print('Hi')
    print('Good Evening')
greet()


# In[64]:


def add(p,q):
    c=p+q
    print(c)
add(10,20)


# Finding maximum and minimum

# In[66]:


min(x),max(x)


# In[93]:


data=[1,3,4,6,7,9,10,20,15,17]
min(data),max(data)


# In[86]:


data=[1,3,4,6,7,9,10,20,15,17]
def min_and_max(data):
    min_val=min(data)
    max_val=max(data)
    
    
    return(min_val,max_val)
min_and_max(data)


# In[92]:


def range(data):
    min_val=min(data)
    max_val=max(data)
    return(max_val - min_val)
range(data)


# Quartile

# In[96]:


a=np.array([1,2,3,4,5])
q1=np.percentile(a,25)
q1


# In[97]:


a=np.array([1,2,3,4,5])
q2=np.percentile(a,50)
q2


# In[98]:


a=np.array([1,2,3,4,5])
q3=np.percentile(a,75)
q3


# ##### Inter Quartile range

# In[100]:


IQ=q3-q1
IQ


# Variance

# In[102]:


np.var(x)


# Population standard devation

# In[103]:


import statistics


# In[104]:


statistics.pstdev(x)


# Sample standard devation

# In[105]:


statistics.stdev(x)


# Standerd devation

# In[106]:


np.std(x)


# Skewness

# In[107]:


from scipy.stats import skew
skew(x)


# Box Plot

# In[115]:


from matplotlib import pyplot as plt
plt.boxplot(x,sym='*')
plt.show()


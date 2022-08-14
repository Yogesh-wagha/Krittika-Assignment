#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit as cf
import statistics


# In[2]:


dmv = pd.read_csv("G:\IITB\ktittika\data.txt")
#print(dmv)
mu=dmv['mod0'].values
losvel=dmv['vgsr'].values
d=10**(mu/5-5)       #Mega parsec


# In[3]:


def velocity(dist,m,c):
    return dist*m+c
plt.scatter(d,losvel,s=1)


# In[4]:


p_opt, p_cov = cf(velocity,d,losvel)


# In[47]:


print(p_opt)


# In[6]:


plt.plot(d,velocity(d,*p_opt),label='Best Fit',color='g')

plt.scatter(d,losvel,label='OG_Data',s=1,color='darkorange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Fit')
plt.legend()


# In[7]:


age=1000/p_opt[0]
print("age of the universe is ",age,"billion years")


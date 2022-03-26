#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


# In[3]:


f=open("sgb-words.txt","r")
file=f.read()
words=list(map(str,file.split()))
print(random.choice(words))


# In[4]:


import re


# In[5]:


r=re.compile("ju")
ff=list(filter(r.match,words))


# In[6]:


for i in ff:
    print(i)


# In[22]:


rand_pos=random.randint(0,len(words)-1)


# In[23]:


Wordpos=f"The word in position {rand_pos} is {words[rand_pos]}"


# In[24]:


print(Wordpos)


# In[ ]:





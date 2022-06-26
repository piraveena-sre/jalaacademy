#!/usr/bin/env python
# coding: utf-8

# In[3]:


class Python:
# Access through class    
 staticVariable = 9 
print(Python.staticVariable)


# In[4]:


Python.staticVariable = 12
print(Python.staticVariable) # Gives 12


# In[5]:


instance = Python()
print(instance.staticVariable) 


# In[6]:


instance.staticVariable = 15
print(instance.staticVariable) 
print(Python.staticVariable) 


# In[ ]:





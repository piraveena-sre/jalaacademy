#!/usr/bin/env python
# coding: utf-8

# In[2]:


Dict = dict([(1,'piraveena'), (2,'arun'), (3,'maha'), (4,'subha'), (5,'kavee')])
print("Dictionary with each item as a pair:",Dict) #printing dictionary

#adding element in dictionary
Dict[6] = 'latha'
print("\n Dictionary with new item added:",Dict)

#updating values in dictionary
Dict[3] = 'mani'
print("\n Dictionary with updated values:",Dict)

print("\n Accessing one value in Dictionary:",Dict[1])

#deleting value from drictionary
del Dict[6]
print("\n Delete a value from a Dictionary:",Dict)

#creating a nested dictionary
Dict1 = {1: 'piraveena', 2: 'arun',
        3:{'Age' : 18, 'Branch' : 'bsc', 'Year' : 'Third Year'}}
print("\n Nested loop Dictionary:",Dict1)

print("\n Accessing an element of a Nested Dictionary:",Dict1[2])


# In[ ]:





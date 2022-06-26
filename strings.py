#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Jala Academy")
print('Jala Academy')
print("'Jala Academy'")


# In[2]:


a="Jala"
b="Academy"
c=a+" "+b
print(c)


# In[3]:


a="Jala Academy"
print(len(a))


# In[4]:


myString="Jala Academy"
print(myString[0:4])
print(myString[5:12])
print(myString[:6])


# In[5]:


myString="Jala Academy"
print(myString.index("J"))
print(myString.index("e"))
print(myString.index("m"))


# In[6]:


import re

pattern='^a...s$'
string='abaas'
result=re.match(pattern,string)

if result:
  print("Matched")
else:
  print("Not Matched")


# In[7]:


a='Jala'
b='Jala'
if a==b:
  print("a and b are equal")
else:
  print("a and b are not equal")


# In[8]:


a="Jala academy"
b=a.startswith("Jala")
print(b)
b=a.endswith("academy")
print(b)


# In[9]:


a="  Jala "
x=a.strip()
print("I am doing",a,"internship")


# In[10]:


a="How are you"
x=a.replace("are","is")
print(x)


# In[ ]:


name1,name2,name3=input("Enter 3 names:").split()
print("Name 1:",name1)
print("Name 2:",name2)
print("Name 3:",name3)


# In[ ]:


a=20
print(type(a))
a=str(a)
print(a)


# In[ ]:


a="Jala Academy"
print(a.upper())
print(a.lower())


# In[ ]:





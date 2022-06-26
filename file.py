#!/usr/bin/env python
# coding: utf-8

# In[3]:


file1 = open("MyFile.txt","a")
file2 = open(r"D:\Text\MyFile2.txt","w+")


# In[9]:


with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")


# In[8]:


file1 = open("HW.txt","r")
data = file1.read()
print(data)
print()


# In[4]:


import struct

thefile = open('somebinfile', 'r+b')
record_size = struct.calcsize(format_string)

thefile.seek(record_size * record_number)
buffer = thefile.read(record_size)
fields = list(struct.unpack(format_string, buffer))

# Perform computations, suitably modifying fields, then:

buffer = struct.pack(format_string, *fields)
thefile.seek(record_size * record_number)
thefile.write(buffer)

thefile.close(  )


# In[6]:


f=open("GFG.txt","r")
f.seek(20)
print(f.tell())
print(f.readline())
f.close


# In[7]:


import os
os.access('my_file', os.R_OK) # Check for read access
True
os.access('my_file', os.W_OK) # Check for write access
True
os.access('my_file', os.X_OK) # Check for execution access
False
os.access('my_file', os.F_OK) # Check for existance of file
True


# In[ ]:





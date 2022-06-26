#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(10):
  print("Bright IT Career")


# In[2]:


num1=50
num2=10*5
if num1 == num2:
  print("equal")
else:
  print("not equal")  
num1=45
num2=76
if num1 != num2:
  print("not equal")
else:
  print("equal")


# In[3]:


a=int(input("Enter the number:"))
if a % 2==0:
  print("even")
else:
  print("odd")


# In[4]:


i=1
while(i<=20):
  print(i)
  i+=1


# In[5]:


a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
  print("A is largest")
if b>a and b>c:
  print("B is largest")
else:
  print("C is largest")


# In[6]:


i=12
while(i<20):
  print(i)
  i+=2


# In[7]:


i=1 
while True:
  print(i)
  i+=1
  if i>10:
    break


# In[8]:


num=int(input("Enter a number: "))
sum=0
temp=num
while temp > 0:
  digit=num % 10
  sum=digit**3
  temp//=10
if num==sum:
  print(num,"is an armstrong number")
else:
  print(num,"is not an armstrong number")


# In[9]:


num=56
if num > 1:
  for i in range(2,int(num/2)):
    if num % i==0:
      print(num,"is a prime number")
      break
    else:
      print(num,"is not a prime number")


# In[10]:


a=input("Enter the string: ")
if(a==a[::-1]):
   print("The string is a palindrome")
else:
   print("The string is not a palindrome")


# In[11]:


a=int(input("Enter a number:"))
if a % 2==0:
  print("The given number is even")
else:
  print("The given number is odd")


# In[12]:


def get_gender(self):
    if self.use_url==none:
        print("i am anonymous use.")
        return'unknown'
    else:
        if self.soup==none:
            self.parser()
            soup=self.soup
            try:
                gender=str(soup.find("span",class_="itemgender").i)
                if(gender=='<iclass="icon icon-profile-female"></i>'):
                    return'female'
                else:
                    return'male'
            except:
                return'unknown'


# In[ ]:





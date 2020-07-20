#!/usr/bin/env python
# coding: utf-8

# In[ ]:


QUESTION:
    
Please reverse the text below without using text index methods. Please use a loop.
text = “Clarusway”

ANSWER:
    
text = "Clarusway"
newtext = ""
for i in range(len(text)-1, -1, -1):
   newtext += text[i]
print(newtext)


# In[1]:


text = "clarusway"
newtest = ""
for i in range(len(text)-1,-1,-1):
    newtest += text[i]
print(newtest)


# In[6]:


sayi = int(input("1-10 kadar bir sayi giriniz: "))
 
for i in range(0,10): #default olarak (0,10,1) o yuzden i yi artirmaya gerek yok.
    print(f"{sayi}*{i} = {sayi*i}")     


# In[ ]:





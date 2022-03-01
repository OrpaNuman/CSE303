#!/usr/bin/env python
# coding: utf-8

# In[2]:


#exercise 1

divisible8 = [i for i in range(1,1001) if i % 7 == 0] 
print(divisible8)


# In[3]:


#exercise 2

six = [i for i in range(1,1001) if '6' in str(i)] 
print(six)


# In[4]:


#exercise 3


nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

n=len(string)
cnt=0

for i in range(1,n):
    if(string[i] == ' '):
       cnt+=1 
print("Spaces of the string is : ",cnt)


# In[5]:


#exercise 4


string = "Practice Problems to Drill List Comprehension in Your Head."
for word in string:
    if word in ('a','e','i','o','u','A','I','E','O','U'):
        string = string.replace(word, '')
        
print("without vowel :", string)


# In[7]:


#exercise 5

string = "Practice Problems to Drill List Comprehension in Your Head."
word=string.split(" ")
L=len(word)
for i in range (1,L):
    if(len(word[i])<5 ):
        print(word[i])
       


# In[8]:


#exercise 6

string = "Practice Problems to Drill List Comprehension in Your Head."
words = string.split()
word_lengths = []
for word in words:
   word_lengths.append(len(word))
print(words)
print(word_lengths)


# In[ ]:





# In[ ]:





# In[ ]:





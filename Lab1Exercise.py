#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Excersice 1

a = int(input("Enter A: "))
b = int(input("Enter B: "))

product=a*b

if(product>1000):
    sum=a+b
    print("Sum is = %d" %sum)
else: print("Product is = %d" %product)


# In[5]:


#Exercise 2

import math

def circle_rad(r):
    return math.pi*r*r

def circle_peri(r):
    return 2* math.pi*r

r = float (input("Enter radius: "))
area= circle_rad(r)
print("Area of a circle= ", area)

perimeter= circle_peri(r)
print("Perimeter of a circle = ", perimeter)


# In[8]:


#Excercise 3

def compound_interest_051(P,R,T):
    return P*(1+(R/100))**T

P = float(input("Enter principle amount: "))
R = float(input("Enter interest amount: "))
T = float(input("Enter time(years): "))
CI= compound_interest_051(P,R,T)
print("Compound Interest = ", CI)


# In[9]:


#Excersice 4

def series_sum(num):
    if(num == 0):
        return 0
    else:
        return (num * num) + series_sum(num - 1)

N = int(input("Enter value of N : "))
sum = series_sum(N)
print("Value of the series : %d" %sum)


# In[11]:


#Excercise 5

def prime_find(num):
    if num>1:
        for i in range(2,num):
            if (num % i) == 0:
                return True
            else: False
    else: False

N = int(input("Enter N : "))
if (prime_find(N)==True):
    print(N, "not a prime number")
else:
    print("%d a prime number" %N)


# In[12]:


#Excercise 6

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Enter positive integer n : "))
if(n<0):
    print("Wrong input")
else: 
    print("n-th fibonacci number is = %d" %fibonacci(n))


# In[13]:


#Excersice 7

list1 = [20,19,2,60,51]
total = 0
for element in range(0, len(list1)):
    total = total + list1[element]

print("Sum of the list: ", total)


# In[15]:


#Excercise 8

list1 = [20,19,2,60,51]
total = 0
L=len(list1)
for i in range(L):
   if(i%2==0):
       total+=list1[i];
print("Sum of the even indexed list: ", total)


# In[21]:


#excrercise 9
list1 = [20,19,2,60,51]
def largest_number(num):
    largest=num[0]
    for i in range(len(num)):
        if num[i] > largest:
            largest= num[i]
    print("Largest number is:", largest)
     
def smallest_number(num):
    smallest= num[0]
    for i in range(len(num)):
        if num[i] < smallest:
             smallest = num[i] 
    print("Smallest number is:", smallest)

largest_number(list1)
smallest_number(list1)


# In[23]:


#excercise 10

list1 = [20,19,2,60,51]
l=len(list1)
list1.sort()
print("Second largest element is:", list1[l-2])


# In[25]:


#Exercise 11

string=input("Enter string: ")
for i in range (len(string)):
    if(i%2==0):
        print(string[i])


# In[28]:


#Exercise 12

string=input("Enter string: ")
l=len(string)
n=int(input("Enter number: "))

new=""

for i in range(0,l):
    if i>=n:
        new=new+string[i]

print(new)


# In[30]:


#excercise 13

phrase ='CSE303 is a four credit data science course.'
print(phrase)
sub_string = 'CSE303'
print(sub_string)
cnt = 0
sub_len=len(sub_string)
for i in range(len(phrase)):
    if phrase[i:i+sub_len] == sub_string:
        cnt += 1
print (cnt)


# In[33]:


#exercise 14

def palindrome_checker_051(s):
    return s == s[::-1]
 
s = "mom"
result = palindrome_checker_051(s)
 
if result:
    print("Yes")
else:
    print("No")


# In[39]:


#Excercise 15

odd=[]
even=[]
list1=[1,2,3,4,15,6] 
list2=[7,8,9,10,11,12] 
length1=len(list1)
length2=len(list2)
print("Odd numbers from list 1 : ")
for i in range (0,length1):
    if(list1[i]%2!=0):
        odd.append(list1[i])
print(odd)
list2=[7,8,9,10,11,12] 
print("Even numbers from list 2 : ")
for i in range (0,length2):
    if(list2[i]%2==0):
        even.append(list2[i])
print(even)


# In[ ]:





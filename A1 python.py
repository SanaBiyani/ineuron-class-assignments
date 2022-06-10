#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Write a Python program to find those numbers which are divisible by 7
#and multiple of 5, between 1500 and 2700 (both included).


# In[2]:


for i in range(1500,2701):
    if (i%7==0) & (i%5==0):
        print("",i)

    


# In[ ]:


#2. Python program to add two numbers


# In[3]:


def get_sum(a,b):
    return a + b
get_sum(2,5)


# In[ ]:


#3. Maximum of two numbers in Python


# In[4]:


def get_max(a,b):
    return max(a,b)
get_max(2,5)


# In[ ]:


#4. Python Program for factorial of a number


# In[7]:


import math 
def get_fact(a):
    return math.factorial(a)
get_fact(5)


# In[ ]:


#5. Python Program for simple interest 


# In[20]:



def simple_interest(p,r,t):
    return (float(p)*float(r)/100*float(t)) + float(p)

simple_interest(input("enter principle:"),
 input("enter rate:"),
 input("enter time:")) 


# In[28]:


#6. Python Program for compound interest
def compound_interest(p,r,n,t):
    return(float(p)*(1+(float(r)/100)/float(n))**(float(n)*float(t)))
compound_interest(input("enter priciple:"),
                input("enter rate:"),
                input("enter number of times interest applied per time period:"),
                     input("enter time:"))


# In[ ]:


#7.Python Program to check Armstrong Number


# In[11]:


total = 0
o_num = input("enter number:")
num = list(map(int,o_num))
for i in range(0,len(num)):
    total = total + num[i]**len(num)
    
final= str(total)
if final == o_num:
    print("armstrong  number")
else:
    print("not armstrong number ")


# In[ ]:


#8. Python Program for Program to find area of a circle.


# In[12]:


rad= input("enter radius:")
22/7*int(rad)**2


# In[ ]:


#9. Python program to print all Prime numbers in an Interval.


# In[27]:


sn = int(input("enter starting number:"))                            
en = int(input("enter ending number:"))

for num in range(sn,en+1):
    if num > 1:
        for i in range(2,num):
            if (num % i)==0:
                break
            
        else:
            print(num)


# In[34]:


#10. Python program to check whether a number is Prime or not.
num = int(input("enter number:"))
if num > 1:
    for i in range (2, num):
        if(num % i)==0:
            print("not prime number")
            break
    else:
        print("prime number")
else:
    print("all prime numbers are greater than 1")


# In[ ]:





# In[ ]:





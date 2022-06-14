#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Python Program for n-th Fibonacci number


# In[3]:


def get_fib (n):
    if n ==0:
        return"not valid"
    elif n<=2:
        return n-1
    else:
        return get_fib(n-1)+  get_fib(n-2)

print(get_fib(5))


# In[ ]:


#2. Python Program for How to check if a given number is Fibonacci number.


# In[4]:


import math 
def is_perfect_sq(k):
    s = int(math.sqrt(k))
    return s * s == k

def is_fib(x):
    if is_perfect_sq(((5*x**2+4) and (5*x**2-4))or((5*x**2+4) or (5*x**2-4))) == True: 
        return "is fibonacci number" 
    else :
        return "isn't fibonacci number"
    
print(is_fib(13))


# In[ ]:


#3. Python Program for n\’th multiple of a number in Fibonacci Seriesv


# In[5]:


def fib_multiple(k,n):
    f1 = 0
    f2 = 1
    i =2; 
    while i!=0:
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
 
        if f2%k == 0:
            return n*i
 
        i+=1
         
    return
 
print(fib_multiple(2,3))  


# In[ ]:


#4. Program to print ASCII Value of a character.


# In[2]:


def ascii_value (n):
    return ord(n)

print(ascii_value(input("enter character:")))


# In[ ]:


#5. Python Program for Sum of squares of first n natural numbers


# In[12]:


n = int(input("enter number:"))
num = 0
for i in range(1,(n + 1)):
    num = num + i ** 2
    
print(num)


# In[ ]:


#6. Python Program for cube sum of first n natural numbers


# In[13]:


n = int(input("enter number:"))
num = 0
for i in range(1,(n + 1)):
    num = num + i ** 3
    
print(num)


# In[ ]:


#7. Python Program to find sum of array


# In[4]:


import numpy as np
def sum_of_arr(a):
    total = 0
    for i in a:
        total += i
    return total

a = np.array([1,2,3,4])

final = sum_of_arr(a)

print(final)


# In[5]:


type(a)


# In[ ]:


#8. Python Program to find largest element in an array.


# In[7]:


a = i([1,49,82,39])
print(np.max(a))


# In[ ]:


#9. Python Program for array rotation.


# In[42]:


def rotate_array(arry, E):
    K = len(arry)
    temp_1 = []  
    J = 0  
    while (J < E):  
        temp_1.append(arry[J])  
        J = J + 1  
    J = 0  
    while (E < K):  
        arry[J] = arry[E]  
        J = J + 1  
        E = E + 1  
    arry[:] = arry[J:] + temp_1  
    return arry 

arry =([1,3,5,7,9,11,13,15])
print(rotate_array(arry,4))


# In[ ]:


#10. Python Program for Reversal algorithm for array rotation.


# In[50]:


def reverse_array(arry,start,end):
    while start<end:
        x = arry[start]
        arry[start]= arry[end]
        arry[end] = x
        end = end - 1
        start= start+1
    


def rotation(arry,E):
    K = len(arry)
    reverse_array(arry,0,E-1)
    reverse_array(arry,E,K-1)
    reverse_array(arry,0,K-1)
    return arry
    

arry = ([1,3,5,7,9,11,13,15])
print(rotation(arry,2))
    


# In[56]:


#11. Python Program to Split the array and add the first part to the end.


# In[63]:


def array_split(arr,E):
    e_arr1=[()]
    e_arr2=[()]
    for i in (0,E-1):
    e_arr1.append(arr[i])
        
    for i in (E,len(arr)-1):
        e_arr2.append(arr[i])
    return  e_arr2 + e_arr1
        
arr= ([1,3,5,7,9,11,13,15])    
print(array_split(arr,4))
    


# In[89]:


def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
         
        arr[n-1] = x

n=len(arr)
arr = ([1,3,5,7,9,11,13,15]) 
splitArr(arr, len(arr), 2)
for i in range(0, n):
    print((arr[i]), end = ' ')
        


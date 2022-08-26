#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Half Diamond Pattern printing Exercises
# Using while loop

num = 0
dia_len = int(input("Please input length of your Diamond :"))
while num < dia_len:
    num += 1
    print(num*'*')
while num != 1:
    num -= 1
    dia_len -= 1
    print(num*'*')


# In[63]:


# using for loop
dia_len = int(input("Please input your Diamond length :"))
for i in range(dia_len):
    for j in range(0, i+1):
        print('*', end="")
    print()
for i in range(1, 5):
    for j in range(i, 5):
        print('*', end="")
    print()


# In[97]:


def pypart(pat_size):
    for i  in range(pat_size):
        i = i + 1
        print(i*"*")
    
pat_size = int(input("Please enter pattern size :"))
#print(pypart(pat_size))
pypart(pat_size)


# In[96]:


def pypart(pat_size):
    for i  in range(pat_size):
        i = i + 1
        print(i*"1")
    
pat_size = int(input("Please enter pattern size :"))
#print(pypart(pat_size))
pypart(pat_size)


# In[116]:


def pypart(n):
    for i in range(n):
        for j in range(0, i+1):
            print("*",end="")
        print()
n = 5
pypart(n)


# In[119]:


def pypart(n):
    for i in range(n):
        for j in range(0, i+1):
            j += 1
            print(j, end="")
        #print()
        print("\r")
n = 5
pypart(n)


# In[163]:


def pypart(n):
    for i in range(n):
        for j in range(i, n):
            print("*",end="")
        print()
n = 5
pypart(n)


# In[193]:


def pypart(n):
    for i in range(n):
        for j in range(i+1):
            print("* ",end="")
        print()
n = 5
pypart(n)


# In[220]:


def pypart2(n):
    # number of spaces
    k = 2*n - 2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        
        k = k - 2
        
        for j in range(i+1):
            print("* ", end="")
        print("\r")
 
n = 5
pypart2(n)


# In[237]:


def pattern(n):
    k = 2*n-2
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k -= 2
        for j in range(i+1):
            print("* ", end="")
        print()
    
n = 5
pattern(n)


# In[239]:


def pattern(n):
    k = 2*n-1
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k -= 1
        for j in range(i+1):
            print("* ", end="")
        print()
    
n = 5
pattern(n)


# In[246]:


# python3 code to print pyramid pattern using while loop
n=5;i=0
while(i<=n):
  print(" " * (n - i) +"*" * i)
  i+=1


# In[247]:


# python3 code to print pyramid pattern using while loop
n=5;i=0
while(i<=n):
  print(" " * (n - i) +"* " * i)
  i+=1


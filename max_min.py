#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Initializing list
test_list = [ 1, 4, 5, 7, 8 ]
 
# Printing test_list
print ("The list is : " + str(test_list))
counter = 0
for i in test_list:
    counter += 1
    #return counter
print("Length of list using naive method is : ", counter)


# In[18]:


def maximum_num(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
        
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("Maximum no is: ",maximum_num(num1, num2))

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("Maximum no is: ",max(num1, num2))


# In[19]:


def minimum_num(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
        
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("Minimum no is: ",minimum_num(num1, num2))

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
print("Minimum no is: ",min(num1, num2))


# In[ ]:





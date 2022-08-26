#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Assigning Subsequent Rows to Matrix first row elements

test_list = [[5, 8, 10], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
print(test_list)
res = {test_list[0][ele] :  test_list[ele + 1] for ele in range(len(test_list) - 1)}
print("\n",res)


# In[13]:


# Adding and Subtracting Matrices in Python
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[4,5],[6,7]])

print("A+B is : ",  A+B)
print("\nA-B is : ",  A-B)

print("\nA+B using np.add is : ",np.add(A,B))
print("\nA-B using np.subtract is : ",np.subtract(A,B))


# In[70]:


#Print Multiple Arguments in Python
def mul_string(name, num):
    print("My name is :",name, "and fav num is :",num)

name = str(input("What is your name :"))
num = int(input("Input your Fav no :"))
mul_string(name, num)
          


# In[85]:


# Sorting objects of user defined class
def sort_func(list_num, list_abc):
    print(sorted(list_num))
    print(sorted(list_abc))
    
list_num = [1,26,3,9]
list_abc = ['b','d','c','a']
print(sort_func(list_abc, list_num))


# In[ ]:





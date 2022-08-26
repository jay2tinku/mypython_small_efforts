#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list = [12, 35, 9, 56, 24]
print(my_list)
#first_ele = my_list[0]
last_ele = my_list[-1]
first_ele = last_ele
my_list[-1] = my_list[0]
my_list[0] = first_ele
my_list


# In[2]:


def swap_list(swapList):
    temp = my_list[0]
    my_list[0] = my_list[-1]
    my_list[-1] = temp
    #print(my_list)
    return my_list

my_list = [12, 35, 9, 56, 24]
print(my_list)
swap_list(my_list)


# In[3]:


def exchange_list(newList):
    newList[0],newList[-1] = newList[-1],newList[0]
    return newList
#newList = [1, 2, 3]
newList = [24, 35, 9, 56, 12]
print(newList)
exchange_list(newList)


# In[ ]:





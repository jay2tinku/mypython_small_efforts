#!/usr/bin/env python
# coding: utf-8

# In[14]:


def swap_list(list):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list

list = [23, 65, 19, 90, 100]
print(list)
pos1 = int(input('Enter first position: '))
pos2 = int(input('Enter first position: '))
swap_list(list)


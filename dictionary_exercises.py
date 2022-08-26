#!/usr/bin/env python
# coding: utf-8

# In[55]:


#sort dictionary with key values

from collections import OrderedDict
key_value = {
    '2' : '238',
    '4' : '231',
    '1' : '234',
    '3' : '238',
    '6' : '236',
    '5' : '231'
}
print(key_value,"\n")
#print(type(key_value))
#print(key_value.values())
print(key_value.keys(),"\n")

key_value1 = OrderedDict(sorted(key_value.items()))

#key_value1 = key_value(sorted(key_value.items))
print(key_value1,"\n")
print(type(key_value1))


# In[68]:


"""
Find the size of a Set in Python
"""
import sys

set1 = {"A", 1, "B", 2, "C", 3}
set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

print("Size of Set1 : ",sys.getsizeof(set1),"bytes")
print("Size of Set1 : ",sys.getsizeof(set2),"bytes")
print("Size of Set1 : ",sys.getsizeof(set3),"bytes")


# In[70]:


"""
Iterate over a set in Python
"""

test_set = set("geEks")
for i in test_set:
    print(i)


# In[75]:


# min and Max in given set

set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
print("min and Max in given set is : ", min(set), "and", max(set))


# In[111]:


#Remove items from Set
def remove_set(set):
    set = sorted(set)
    print(set)
    while set:
        set.pop()
        print(set)
    
set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
print(remove_set(set))
print("\n \n \n######################################################### \n \n \n")
def add_set(set1):
    while set1:
        set1 = sorted(set1)
        set1.pop()
        print(set1)
    
set1 = (['d', 'c', 'a', 'e', 'g', 'f', 'b', 'k', 'r', 'p', 's'])
print(add_set(set1))


# In[131]:


#Check if two lists have at-least one
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

print("List1 is : ",list1,"\nList2 is : ",list2)

exist = False
for x in list1:
    for y in list2:
        if x == y:
            exist = True
if exist == True:
    print("\nList1 content exist in List2")
else:
    print("\nList1 content doesn't exist in List2")


# In[ ]:





# In[ ]:





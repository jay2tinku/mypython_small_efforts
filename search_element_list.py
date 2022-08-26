#!/usr/bin/env python
# coding: utf-8

# In[9]:


#search_element_list

test_list = [1, 6, 3, 5, 3, 4]
print(test_list)
find_num = int(input("Input the number you want to find: "))
if find_num in test_list:
    print("We can find your number: ", find_num)
else:
    print("Your number doesn't exist") 


# In[10]:


#clear list
geek = [6, 0, 4, 1]
print("list before clear :",geek)
geek.clear()
print("list after clear :",geek)


# In[29]:


#revese list
list = [4, 5, 6, 7, 8, 9]
print("list before clear :",list)
list.reverse()
print("list after clear :",list)

l = []
for i in list:
    l.insert(0, i)
print("Reverse using for loot", l)


# In[37]:


#clone list
list = [4, 5, 6, 7, 8, 9]
print("list before clone :",list)

copy = list.copy()
print("list after copy :",copy)


# In[49]:


#occurrences of element in list

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10, 10, 12, 12, 12, 10, 15, 15, 12, 10]
print(lst)
count = 0
occur_num = int(input("Enter number from list to check occurance :"))
for number in lst:
    if number == occur_num:
        count += 1
print(count)


# In[59]:


#sum and avg
import numpy as np
list = [4, 5, 1, 2, 9, 7, 10, 8]
print("My list is: ", list)
my_array = np.array(list)
print("Sum of list is: ", my_array.sum())
print("Mean of list is: ", my_array.mean())

print("\n#######################################################\n")
sum = 0
for i in list:
    sum += i
print("Sum of the list is :",sum)

avg = sum/len(list)
print("Avg of the list is :",avg)


# In[ ]:





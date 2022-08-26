#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
print
def tuple_size(tuple):
    tuple_size = sys.getsizeof(tuple)
    return tuple_size

tuple1 = ("A", 1, "B", 2, "C", 3)
tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

#for tuple in tuple1 tuple2 tuple3:
#print("My tuple is : ", tuple1)
print("Tuple size of tuple1 :",tuple_size(tuple1))
print("Tuple size of tuple1 :",tuple_size(tuple2))
print("Tuple size of tuple1 :",tuple_size(tuple3))


# In[2]:


def tuple_sum(test_tup):
    sum = 0
    for num in test_tup:
        sum = sum + num
    return sum
test_tup = (7, 8, 9, 1, 10, 7)
print("My tuple is : ", test_tup)
print("Sum of my tuple is : ", tuple_sum(test_tup))

print(sum(list(test_tup)))


# In[19]:


list1 = [1, 2, 3]
[(num, pow(num, 3)) for num in list1]
#res = [(val, pow(val, 3)) for val in list1]
#print(res)


# In[ ]:





# In[ ]:





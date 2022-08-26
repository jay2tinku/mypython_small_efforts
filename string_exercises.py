#!/usr/bin/env python
# coding: utf-8

# In[16]:


string = input("Please enter your string to check symmetrical and palindrome : ")
print(string)
string_half = int(len(string)/2)
if len(string)%2 == 0: #even
    first_string = string[:string_half]
    second_string = string[string_half:]
else:
    first_string = string[:string_half]
    second_string = string[string_half+1:]

## symmetric    
if first_string == second_string:
    print(string, "Given string is symetric")
else:
     print(string, "Given string is not symetric")
        
# palindrome
if first_string == second_string[::-1]:
    print(string, "Given string is palindrome")
else:
     print(string, "Given string is not palindrome")


# In[38]:


str = "My name is Rakesh"
str_split = str.split()
print(str_split)
temp = str_split[0]
str_split[0] = str_split[-1]
str_split[-1] = temp
str = str_split
print(str_split)


# In[45]:



# Python code
# To reverse words in a given string
 
# input string
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
l = []
for i in s:
    # apending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))


# In[68]:


str = 'Mamta / Rakesh'
#def find_str_len(str):
print("String length using len function : ",len(str))
count = 0
for i in str:
    count += 1
print("String length using iteration : ",count)

#str = 'Mamta / Rakesh'
#ind_str_len(str)


# In[132]:


def even_word(split_str):
    for even_word in split_str:
        if len(even_word)%2 == 0:
            print(even_word)

str = "Hello how are you ?"
split_str = str.split()
print("Original string : ", str)
even_word(split_str)


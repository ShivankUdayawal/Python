#!/usr/bin/env python
# coding: utf-8

# ### Date

# In[1]:


# to print current date

import datetime
a = datetime.datetime.now()
print(a)


# In[2]:


print(a.year)


# In[3]:


print(a.month)


# In[4]:


print(a.strftime("%A"))  # weekday


# In[5]:


b = datetime.datetime(2022, 5, 20)
print(b)


# In[6]:


print(a.strftime("%B")) #month
print(a.strftime("%Y")) #year
print(a.strftime("%I")) #hour
print(a.strftime("%M")) #minute
print(a.strftime("%S")) #sec
print(a.strftime("%p")) #am - pm/
print(a.strftime("%Z")) #timezone


# In[7]:


x = pow(10,2) #power
print(x)


# In[8]:


import math
c = math.sqrt(81)
print(c)


# In[9]:


import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


# In[10]:


d = math.pi
print(d)


# * "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# 
# * "a" - Append - Opens a file for appending, creates the file if it does not exist
# 
# * "w" - Write - Opens a file for writing, creates the file if it does not exist
# 
# * "x" - Create - Creates the specified file, returns an error if the file exists
# 
# * "t" - Text - Default value. Text mode
# 
# * "b" - Binary - Binary mode (e.g. images)

# In[11]:


f = open("demofile.txt")


# In[12]:


f = open("demofile.txt", "rt")


# In[13]:


f = open("demofile.txt", "r")
print(f.read())


# In[14]:


print(f.read(5))


# In[15]:


print(f.readline())


# In[16]:


f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


# In[17]:


f = open("demofile.txt", "r")
print(f.readline())
f.close()


# * "a" - Append - will append to the end of the file
# 
# * "w" - Write - will overwrite any existing content
# 
# * "x" - Create - will create a file, returns an error if the file exist

# In[18]:


f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())


# In[19]:


f = open("myfile.txt", "x")


# In[20]:


# removing the file

import os
os.remove("demofile.txt")


# In[21]:


import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")


# In[22]:


# delete the folder

import os
os.rmdir("myfolder124")


# ### removing duplicates

# In[23]:


mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)


# In[24]:


h = ["apple", "apple", "kiwi", "banana"]
h = list(dict.fromkeys(h))
print(h)


# In[25]:


# Create a dictionary, using the List items as keys. 
# This will automatically remove any duplicates because dictionaries cannot have duplicate keys.


# In[26]:


def my_function(x):
    return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)


# In[27]:


txt = "Hello World"[::-1]
print(txt)


# In[28]:


k = [1,2,3,4,5]
k[::-1]


# In[29]:


def my_function(x):
    return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)


# In[30]:


a = 12345
i = 0
while (a > 0):
    r = a % 10
    i = (i * 10) + r
    a = a // 10
    
print(i)


# In[32]:


x = input("Type a number: ")
y = input("Type another number: ")

sum = int(x) + int(y)

print("The sum is: ", sum)


# ### RegEx
# 
# * A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# 
# 

# In[33]:


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")


# In[34]:


import re

text = "Hello world ! there"
x = re.search("...World..", text)

if x:
    print("match")
else:
    print("no match")


# In[ ]:





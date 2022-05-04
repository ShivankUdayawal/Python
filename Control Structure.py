#!/usr/bin/env python
# coding: utf-8

# ## If....Else

# In[1]:


a = 30
b = 10

if a > b:
    print("a is greater")


# In[2]:


if a < b:
    print("a is less")
else:
    print("a is greater")


# In[3]:


if a < b:
    print("a is less")
elif a == b:
    print("a is equal")
else:
    print("a is greater")


# In[4]:


if a > b: print("a is great")


# In[5]:


print("a is less") if a < b else print("a is great")


# In[6]:


print("a is less") if a < b else print("a is equal") if a == b else print("a is great")


# In[7]:


c = 50
if a > b and b < c:
    print("T")
    
# both true the True


# In[8]:


if a > b and b > c:
    print("T")
else:
    print("F")


# In[9]:


if a > b or b > c:
    print("T")
    
# either one is true


# In[10]:


if a < b or b > c:
    print("T")
else:
    print("F")


# In[11]:


a


# In[12]:


if a > 10:
    print("Above ten")
    if a > 15:
        print("above 15")
    else:
        print("between 10 - 15")


# In[13]:


#pass - if can't be empty, so somehow if with no content, put "pass"  to avoid error
if a > b:
    pass


# ## while

# In[14]:


i = 0
while i < 6:
    print(i)
    i = i + 1


# In[15]:


A = 12345
i = 0 
while A > 0:
    r = A % 10
    i = (i * 10) + r
    A = A // 10
    
print(i)


# In[16]:


# break - to stop the loop

i = 0
while i < 6:
    print(i)
    if i == 4:
        break
    i = i + 1


# In[17]:


# continue - stop the current iteration and continue with next

i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)


# In[18]:


i = 0
while i < 10:
    i = i + 1
    if i == 5:
        continue
    print(i)    


# In[19]:


i = 0
while i < 6:
    print(i)
    i = i + 1
else:
    print("i is no less than 6")


# In[20]:


i = 6
while i < 6:
    print(i)
    i = i + 1
else:
    print("i is no less than 6")


# ## for

# In[21]:


x = ["a", "b", "c", "d", "e"]

for i in x:
    print(i)


# In[22]:


for i in "c":
    print(i)


# In[23]:


for i in x:
    print(i)
    if i == "c":
        break


# In[24]:


x = ["a", "b", "c", "d", "e"]

for i in x:
    if i == "c":
        break
    print(i)


# In[25]:


x = ["a", "b", "c", "d", "e"]
for i in x:
    if i == "c":
        continue
    print(i)


# In[26]:


for i in range(6):
    print(i)


# In[27]:


for i in range(2,8):
    print(i)


# In[28]:


for i in range(2,10,2):
    print(i)


# In[29]:


for i in range(6):
    print(i)
else:
    print("yes")


# In[30]:


for i in range(10):
    if i == 4:
        break
    print(i)
else:
    print("yes")


# ## function
# 
# * The syntax for function definition is
#        
#        def NAME( PARAMETERS ):
#             """ Docstring """
#             STATEMENTS
#        [return]
# 
# * A function must be defined before its first use
# 
# * The return statement is used to return a value from function.
# 
# * If a function does not have return statement , it is considered as a Procedure
# 
# * If a function has to return multiple values , tuples are preferred
# 
# * Sample function call
#         
#         name = my_func (arg1, arg2, arg =‘Default')

# In[31]:


def my_function():
    print("Yes")
    
my_function()


# In[32]:


def my_function(name):
    print(name  + "Reee" )
    
my_function("Jay")


# In[33]:


my_function("Oh my ")


# In[34]:


# parameter and argrument can be used for same thing
# parameter - variable listed inside the parentheses in function definitation
# argumnets - value that is sent to function when it called.


# In[35]:


# 2 arguments

def my_function(fname, lname):
    print(fname + " " + lname)
    
my_function("Jay", "Ro")


# In[36]:


my_function("Jay")


# In[37]:


# arbitrary argumnets - *args

def my_function(*name):
    print("Students name " + name[2])
    
my_function("jay", "rao", "sam")


# In[38]:


def my_function(*name):
    print("Students name " + name[1])
    
my_function("jay", "rao", "sam")


# In[39]:


def my_function(*name):
    print("Students name " + name[0])
    
my_function("jay", "rao", "sam")


# In[40]:


def my_function(n1, n2, n3):
    print("Students name " + n2)
    
my_function("jay", "rao", "sam")


# In[41]:


def my_function(**name):
    print("Students name " + name["lname"])
    
my_function(fname = "jay", lname = "rao")


# In[42]:


def my_function(**name):
    print("Students name " + name["fname"] + name["lname"])
    
my_function(fname = "jay", lname = "rao")


# In[43]:


#default parameter

def my_function(name = "jay"):
    print("Student name  is " + name)
    
my_function("rao")


# In[44]:


my_function()


# In[45]:


# list an argument

def my_function(name):
    for i in name:
        print(i)
j = ["a", "b", "c", "d", "g"]    
my_function(j)


# In[46]:


def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(6))


# In[47]:


def my_function():
    pass


# In[48]:


# recursion - function  can call itself

def my_function(i):
    if i > 0:
        result = i + my_function(i - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion")
my_function(6)


# ##### Adding default values to parameters
# 

# In[49]:



def hello(greeting = 'Hello', name = 'world'):
    print ('%s, %s!' % (greeting, name))

hello('Greetings')


# In[50]:


def hello(greeting = 'Hello', name = 'world'):
    print(greeting + name)

hello("ha", "ho")


# In[51]:


def hello(greeting = 'Hello', name = 'world'):
    print('%s, %s!' % (greeting , name))

hello("ha")


# ##### Using named parameters. In this case the order of the arguments does not matter.
# 

# In[52]:



def hello_1(greeting,name):
    print('%s, %s!' % (greeting, name))

hello_1(greeting = "Hey", name = "world")


# In[53]:


def hello_1(greeting,name):
    print('%s, %s!' % (greeting, name))

hello_1(name = "world", greeting = "Hey")


# ##### The variable length function parameters allow us to create a function which can accept any number of parameters.

# In[54]:


def hello_2(*params):
    print(params)

hello_2("Testing")
hello_2(1,2,3,4)
hello_2(1,2,3,4,5,6,7,8,9,10)


# ##### Variable named parameters

# In[55]:


def hello_3(**params):
    print(params)
    
hello_3(x = 1, y = 2, z = 3)


# In[56]:


hello_3(x = 1)


# In[57]:


hello_3(x = 1, y = 2, z = 3, a = 4, b = 5, c = 6)


# ##### A combination of all of above cases

# In[58]:


def hello_4(x, y, z = 1, *params, **key):
    print(x, y, z)
    print(params)
    print(key)
    
hello_4(1,2,3,4,5,6,7, foo = 1, bar = 2)
hello_4(1,2)


# ##### Recursion

# In[59]:


def Recursion(i):
    if (i > 0):
        result = i + Recursion(i - 1)
        print(result)
    else:
        result = 0
    return result

Recursion(0)


# In[60]:


Recursion(1)


# In[61]:


Recursion(2)


# In[62]:


Recursion(3)


# In[63]:


Recursion(4)


# In[64]:


Recursion(5)


# In[65]:


Recursion(6)


# ### The Anonymous Functions
# 
# * A lambda function is a small anonymous function.
# 
# * A lambda function can take any number of arguments, but can only have one expression.
# 
#                lambda arguments : expression

# In[66]:


x = lambda a : a + 10
print(x(2))
print(x(10))


# In[67]:


x = lambda a, b : a * b
print(x(2,4))


# In[68]:


x = lambda a, b : a / b
print(x(10,2))


# In[69]:


x = lambda a, b, c : a + b + c
print(x(10,17,26))


# In[70]:


def myfun(n):
    return lambda a : a * n

double = myfun(2)
print(double(11))


# In[71]:


triple = myfun(3)
print(triple(11))


# In[72]:


double = myfun(2)
triple = myfun(3)

print(double(11))
print(triple(11))


# In[ ]:





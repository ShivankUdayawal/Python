#!/usr/bin/env python
# coding: utf-8

# In[1]:


# list
# collection of ordered and chnageable, allow duplicates
x = ["A", "B", "C"]
type(x)


# In[2]:


#tuple
# collection of ordered and unchnageable, allow duplicates
y = ("A", "B", "C")
type(y)


# In[3]:


#range
z = range(6)
z
type(z)


# In[4]:


#dict
# collection of ordered and chnageable, no duplicates
a = {"name":"shiv","age":25}
a
type(a)


# In[5]:


#set
# collection of unordered, unchnageable and unindexed, no duplicates
b = {"A","B","C"}
b
type(b)


# In[6]:


#frozenset
c = frozenset({"A","B","C"})
c
type(c)


# In[7]:


#bytes
d = b"Hello"
d
type(d)


# In[8]:


#bytearray
e = bytearray(5)
e
type(e)


# In[9]:


#memoryview
f = memoryview(bytes(5))
f
type(f)


# In[10]:


g = -35.26
type(g)


# In[11]:


int(g)


# In[12]:


complex(g)


# In[13]:


#printing random no b/w 1 to 10
import random
print(random.randrange(1,10))


# In[14]:


h = int("3")
h = float("3")
h


# In[15]:


i = "Hello world!"
print(i[0])
print(i[-1])
print(i[:])
print(i[::])
print(i[::-1])
print(i[2:5])
print(i[:5])
print(i[2:])
print(i[-5:-2])
print(i[2::])


# In[16]:


len(i)


# In[17]:


#checking character present in the string or not
print("o" in i)
print("O" in i)
if "o" in i:
    print("Yes")
    
print("a" not in i)
print("H" not in i)


# In[18]:


print(i.upper())
print(i.lower())
print(i.strip()) #remove any blank space from the beginning or the end
print(i.replace("o", "O"))
print(i.split(" ")) #splits the srting into substrings


# In[19]:


j = "How are you ? {}"
print(i + j)
print(i + " " + j)


# In[20]:


age = 19
print(j.format(age)) #format is used to insert no into string but string has to {} inside the string


# In[21]:


quantity = 2
item = 4
price = 65.98
order = "I want {} piece of item {} for {} pound"
print(order.format(quantity,item,price))

myorder = "I want {0} piece of item {1} for {2} pound"
print(myorder.format(quantity,item,price))


# In[22]:


orders = "I want \'s piece of item \'s for \n pound"
print(orders)


# In[23]:


print(i.capitalize())  #convert first letter to upper case
print(i.center(20))  #centre the string
print(i.count("o")) #count the no of times a word appears
print(i.encode())   #encoded version of srting
print(i.endswith("!"))  #true if string ends with that character
print(i.endswith("a"))
print(i.find("w")) #returned the position of that character


# In[24]:


print(10>9)
print(10<=9)
print(10!=9)
print(bool("Hello"))
print(bool(567))


# In[25]:


#function that return  boolean value
def myFunction():
    return True

print(myFunction())


# In[26]:


# print yes if function return true otherwise false
def myFunction():
    return True
if myFunction():
    print("Yes")
else:
    print("no")
    
myFunction()


# In[27]:


print(10/2)
print(10%2) #remainder
print(10**2)
print(10//2) #div


# In[28]:


k = 5
k &= 3 # k = k & 3   # $ AND - set each bit to 1 if both bits are 1
print(k)

k |= 3     # | OR - sets each bit to 1 if one of two bits is 1
print(k)

k ^=3      # ^ XOR - sets each bit to 1 if only one of two bits is 1
print(k)

k >>=3     # signed right shift
print(k)

k <<=3  #   << Zero fill left shift
print(k)


# ## List

# In[29]:


x


# In[30]:


print(type(x))
print(len(x))
print(x[:2:])
print(x[::-1]) # reverse the list
x[2] = "D"
print(x)
x[0:2] = ["X", "Y", "Z"]
print(x)


# In[31]:


print((x.insert(2, "G")))  #insert an item at specified index
x


# In[32]:


x.append("A") # append to add an item at last
x


# In[33]:


x1 = ["A", "B", "C", "D", "E", "F", "G"]
x.extend(x1)     # append elements from another list to current list
print(x)


# In[34]:


x.extend(y) # append elements from tuple
print(x)


# In[35]:


x.remove("D") #remove
print(x)


# In[36]:


x.pop(1)   # pop - remove using index value
print(x)


# In[37]:


del x[0]  # del - delete = removes the specified index
print(x)


# In[38]:


#x.clear()  #empty the list
#print(x)


# In[39]:


x


# In[40]:


for i in x:
    print(i)


# In[41]:


# list items by refering to their index number
for i in range(len(x)):
    print(i)


# In[42]:


l = 0
while l <len(x):
    print(x[l])
    l = l + 1


# In[43]:


l = 0
while l <len(x):
    print(x[-l])
    l = l + 1


# In[44]:


[print(i) for i in x]


# In[45]:


# list comprehension
# create an empty list then append the speificed character
newlist = []
for i in x:
    if "A" in i:
        newlist.append(i)

print(newlist)


# In[46]:


new = [i for i in x if "A" in i]
print(new)


# In[47]:


# syntax
# newlist = [expression for item in iterable if condition == True] 
# return value a new list with leaving old list unchanged

newlist = [i for i in x if i != "D"]
print(newlist)


# In[48]:


newlist1 = [i for i in range(10)]
print(newlist1)


# In[49]:


newlist2 = [i for i in range(10) if i <5]
print(newlist2)


# In[50]:


x.sort() # sorting assending
print(x)


# In[51]:


X = [100, 30, 20, 4, 70, 43, 78, 44, 22, 14, 90]
X.sort()                   # sorting
X.sort(reverse = True)     # sorting descending
X


# In[52]:


Y = ["Apple", "cherry", "Banana", "orange"]
Y.sort()
Y.sort(key = str.lower)
Y.reverse()
Y


# In[53]:


X.reverse() 
X[::-1]

#both use for reverses the order of elements


# In[54]:


my_list = X.copy()  # Copy
print(my_list)


# In[55]:


list1 = x + X  # joining the lists
print(list1)

list2 = x + Y
print(list2)


# In[56]:


#joining the list using append
for i in list2:
    list1.append(i)
    
print(list1)


# In[57]:


# joining the list using extend
list1.extend(list2)
print(list1)


# ## Tuples

# In[58]:


y


# In[59]:


print(type(y))
print(len(y))


# In[60]:


print(y[0])
print(y[1])
print(y[2])
print(y[-1])
print(y[::-1])


# In[61]:


# update tuple
# tuple are unchnageable/immutable so convert it to list then add then back to tupple
A = list(y)
A[1] = "K"
y = tuple(A)
print(y)


# In[62]:


# adding a tuple to a tuple
B = ("B",)
y = y + B
print(y)


# In[63]:


# removing the element from tuple
C = list(y)
C.remove("B")
y = tuple(C)
print(y)


# In[64]:


# removing element from tuple using del
#del y
#print(y)
# tuple y is deleted


# In[65]:


# unpacking a tuple - when creating a tuple, assign a value to it called packing a tuple

y
(Apple, Kiwi, Car) = y
print(Apple)
print(Kiwi)
print(Car)


# In[66]:


D = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L")
(apple, green, red, *yellow) = D
print(apple)
print(green)
print(red)
print(yellow)


# In[67]:


(apple, green, *red, yellow) = D
print(apple)
print(green)
print(red)
print(yellow)


# In[68]:


for i in D:
    print(i)


# In[69]:


for i in range(len(D)):
    print(i)


# In[70]:


I = 0
while I < len(D):
    print(D[I])
    I = I + 1


# In[71]:


I = 0
while I < len(D):
    print(D[-I])
    I = I + 1


# In[72]:


tuple = y + D
print(tuple)

tuple1 = tuple * 2
print(tuple1)


# In[73]:


count = tuple1.count("A")
print(count)


# In[74]:


inde = tuple1.index("J")
print(inde)


# ## Sets

# In[75]:


b


# In[76]:


type(b)


# In[77]:


# duplicates not allowed
b = {"A", "B", "C", "D", "A"}
print(b)
print(len(b))


# In[78]:


set1 = {"A", 23, "True", 22, "B", 0}
print(set1)
type(set1)


# In[79]:


set2 = set((tuple1))
print(set2)
#duplicates not allowed


# In[80]:


for i in set2:
    print(i)


# In[81]:


print("F" in set2)
print("A" in set2)


# In[82]:


# adding set items

set2.add("apple")
print(set2)


# In[83]:


# adding two sets b and set2 using update
b.update(set2)
print(b)


# In[84]:


# remove
b.remove("C")
print(b)


# In[85]:


# remove using discard
b.discard("G")
print(b)


# In[86]:


# reomove using pop
#re = b.pop("I")
#print(re)
#print(b)


# In[87]:


# clear - emppties the set
b.clear()
print(b)


# In[88]:


# del - delete the set completely
del set1
print(set1)


# In[89]:


set2

for i in set2:
    print(i)


# In[90]:


set3 = {"a", "b", "c"}

# join the sets

set4 = set2.union(set3)
print(set4)


# In[91]:


# update - to insert the sets

set2.update(set3)
print(set2)


# In[92]:


# both union and update exclude any duplicate items


# In[93]:


# keeping duplicates

set2.intersection_update(set3)
print(set2)


# In[94]:


set4.intersection_update(set2)
print(set4)


# In[95]:


set4.intersection(set2)
print(set4)


# In[96]:


# keep all not duplicates

set4.symmetric_difference_update(set3)
print(set4)


# ## Dictionary

# In[97]:


a


# In[98]:


print(type(a))
print(a["name"])
print(a["age"])


# In[99]:


a = {"name":["shiv", "jay", "rao", "jai"],
    "age":[24, 45, 23, 45],
    "car": ["Honda", "Honda", "maruti", "Bmw"],
    "car": ["H", "H", "M", "M"]}

print(a)


# In[100]:


# duplicates not allowed


# In[101]:


print(a["name"])
print(a["age"])
print(a["car"])


# In[102]:


R = a.get("name")
R


# In[103]:


U = a.keys()
U


# In[104]:


# add new item

a["height"] = ["20", "30", "40", "50"]
print(a)


# In[105]:


T = a.values()
T


# In[106]:


# items - return each item in dict as tuple in a list

Get = a.items()
Get


# In[107]:


type(Get)


# In[108]:


a["age"] = ["42", "54", "76", "65"]
print(a)


# In[109]:


# update - update the values

a["age"] = [24, 45, 23, 45]
print(a)


# In[110]:


# remove
# pop - remove the specified key name
a.pop("height")
print(a)


# In[111]:


# popitem - remove last inserted item
a.popitem()
print(a)


# In[112]:


# del - remove the item with specified key name
del a["age"]
print(a)


# In[113]:


#clear - empty the dictionary
#a.clear()
#print(a)


# In[114]:


a = {"name":["shiv", "jay", "rao", "jai"],
    "age":[24, 45, 23, 45],
    "car": ["Honda", "Honda", "maruti", "Bmw"],
    "car": ["H", "H", "M", "M"]}

print(a)


# In[115]:


#for key
for i in a:
    print(i)


# In[116]:


#for values
for i in a:
    print(a[i])


# In[117]:


for i in a.values():
    print(i)


# In[118]:


for i in a.keys():
    print(i)


# In[119]:


for i,j in a.items():
    print(i,j)


# In[120]:


# copy
newdict = a.copy()
print(newdict)


# In[122]:


# copy
newdict1 = dict(a)
print(newdict1)


# In[ ]:





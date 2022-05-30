#!/usr/bin/env python
# coding: utf-8

# ### List Exercise
# 
# * https://pynative.com/python-list-exercise-with-solutions/
# * https://www.geeksforgeeks.org/python-list-exercise/

# ##### 1. Reverse a list in Python

# In[1]:


list1 = [100, 200, 300, 400, 500]


# In[2]:


print(list1[::-1])


# In[3]:


list1.reverse()
print(list1)


# #### 2. Concatenate two lists index-wise
# 
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# In[4]:


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = list(zip(list1, list2))
print(list3)


# In[5]:


list3 = [i + j for i, j in zip(list1, list2)]
print(list3)


# #### 3. Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

# In[6]:


numbers = [1, 2, 3, 4, 5, 6, 7]

for i in numbers:
    print(i ** 2)


# In[7]:


result = []
for i in numbers:
    result.append(i ** 2)
    
print(result)


# #### 4. Concatenate two lists in the following order

# In[8]:


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = []

for i in list1:
    for j in list2:
        list3.append(i + j)
    
print(list3)


# #### 5. Iterate both lists simultaneously
# 
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order

# In[9]:


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i, j in zip(list1, list2[::-1]):
    print(i, j)


# In[10]:


for i, j in zip(list1, list2[::-1]):
    print(i, j)


# #### 6. Remove empty strings from the list of strings

# In[11]:


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

result = list(filter(None, list1))
print(result)


# In[12]:


result = list(filter(None, list1))
result


# #### 7. Add new item to list after a specified item
# 
# Write a program to add item 7000 after 6000 in the following Python List

# In[13]:


list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
list1


# #### 8. Extend nested list by adding the sublist
# 
# You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.

# In[14]:


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
list1


# * **extend()** method to add new items after it.

# #### 9. Replace list’s item with new value if found
# 
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

# In[15]:


list1 = [5, 10, 15, 20, 25, 50, 20]

# finding the index value of 20
index = list1.index(20)

# replacing the 20 with 200
list1[index] = 200
print(list1)


# In[16]:


# find the index value of 20
index = list1.index(20)

list1[index] = 2000
print(list1)


# #### 10. Remove all occurrences of a specific item from a list.
# 
# write a program to remove all occurrences of item 20.

# In[17]:


list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
    
print(list1)

while 20 in list:
    list.remove(20)
    
print(list)
# #### 11. Program to interchange first and last elements in a list

# In[18]:


Input = [12, 35, 9, 56, 24]
    
def swap(list1):
    list1[0], list1[-1] = list1[-1], list1[0]
    return list1
    
print(swap(Input))


# In[19]:


def swap(list1):
    list1[0], list1[-1] = list1[-1], list1[0]
    return list1

print(swap(Input))


# #### 12. Program to swap two elements in a list

# In[20]:


List = [23, 65, 19, 90]
# pos1 = 1, pos2 = 3

def swap(list1, pos1, pos2):
    list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
    return list1

print(swap(List, 1, 2))


# #### 13. Swap elements in String list

# In[21]:


test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

print("Original string list is: ", test_list)

result = [i.replace('G', 'e').replace('e', 'G') for i in test_list]
print("Swapping string list is: ", result)


# In[22]:


print("Original string list is: ", str(test_list))

result = [i.replace('G', 'e').replace('e', 'G').replace('s', 'o') for i in test_list]
print("Swapping string list is: ", str(result))


# #### 14. Ways to find length of list

# In[23]:


# 1: Naive Method

test_list = [ 1, 4, 5, 7, 8]

count = 0
print("The orginial list is:", test_list)

for i in test_list:
    count = count + 1
    
print("The length of the list using Naive method is", count)


# In[24]:


# 2 : Using len()

print("The orginial list is:", test_list)

print("The length of the list using len method is", len(test_list))


# In[25]:


# 3 : Using length_hint()

from operator import length_hint

test_list = [ 1, 4, 5, 7, 8]


print("The orginial list is:", test_list)

print("The length of the list using length_hint method is", length_hint(test_list))


# #### 15. Check if element exists in list in Python

# In[26]:


test_list = [ 1, 6, 3, 5, 3, 4]

print("Checking 4 is present in list or not")

for i in test_list:
    if i == 4:
        print("4 is present")      


# In[27]:


#  Using set() + in

test_list = [ 1, 6, 3, 5, 3, 4]

print("Checking 4 is present in list or not")

test_list = set(test_list)

if 4 in test_list:
    print("4 is present")


# In[28]:


# Using count()

test_list = [ 1, 6, 3, 5, 3, 4]

print("Checking 4 is present in list or not")

test_list_count = test_list.count(4)

if test_list_count > 0:
    print("4 is present")
else:
    print("No, 4 not here")


# #### 16. Different ways to clear a list in Python

# In[29]:


list1 = [1, 2, 3]
list2 = [5, 6, 7]

print(list1.clear())


# In[30]:


list1 = [1, 2, 3]
list2 = [5, 6, 7]

del list2


# #### 17. Count occurrences of an element in a list

# In[31]:


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]

lst.count(10)


# In[32]:


def count_occur(l1, cunt):
    count = 0
    for i in l1:
        if i == cunt:
            count = count + 1
    return count


count_occur(lst, 10)


# In[33]:


print(count_occur(lst, 15))


# In[34]:


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]

print(count_occur(lst, 8))


# In[35]:


def cunt(l1, x):
    return l1.count(x)

print(cunt(lst, 8))


# In[36]:


# Using Counter()

from collections import Counter

l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

x = 2
d = Counter(l)
d[x]


# In[37]:


x = 4
d = Counter(l)
d[x]


# #### 18. Find sum and average of List in Python

# In[38]:


L = [4, 5, 1, 2, 9, 7, 10, 8]

count = 0

for i in L:
    count = count + i
    

avg = count/len(L)

print("Sum:", count)
print("Avg:", avg)


# In[39]:


L = [4, 5, 1, 2, 9, 7, 10, 8, 12, 45]

count = 0
for i in L:
    count = count + i
    
avg = count/len(L)
print("Sum:", count)
print("Avg:", avg)


# In[40]:


count = sum(L)
Avg = count/(len(L))
print(count)
print(Avg)


# #### 19. Sum of number digits in List

# In[41]:


test_list = [12, 67, 98, 34]

# Using loop + str() 

res = []
for i in test_list:
    sum = 0
    for j in str(i):
        sum = sum + int(j)
    res.append(sum)
    
str(res)


# In[42]:


res = []
for i in test_list:
    sum = 0
    for j in str(i):
        sum = sum + int(j)
    res.append(sum)

str(res)


# In[43]:


list1 = [12, 67, 98, 34]

res = []
for i in list1:
    sum = 0
    for j in str(i):
        sum = sum + int(j)
    res.append(sum)

print("Sum:", str(res))


# #### 20. Multiply all numbers in the list

# In[44]:


#Traversal

l1 = [1, 2, 3]

def mullist(l1):
    result = 1
    for i in l1:
        result = result * i
    return result

print(mullist(l1))


# In[45]:


l2 = [2, 3, 4, 5]

def multi(kl):
    result = 1
    for i in l2:
        result = result * i
    return result



multi(l2)


# #### 21. find smallest  & largest number in a list

# In[46]:


list1 = [10, 20, 4, 45, 99]

list1.sort()
print(*list1[:1])


# In[47]:


print(min(list1))


# In[48]:


print(list1[-1])


# In[49]:


print(max(list1))


# #### 22. find second largest number in a list

# In[50]:


print(list1[-2])


# #### 23. count Even and Odd numbers in a List

# In[51]:


list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

for i in list1:
        if i % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1

print(even_count)
print(odd_count)


# In[52]:


even_count, odd_count = 0, 0
for i in list1:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print(even_count)
print(odd_count)


# #### 24. Remove multiple elements from a list in Python

# In[53]:


l1 = [11, 5, 17, 18, 23, 50]

for i in l1:
    if i % 2 == 0:
        l1.remove(i)
        
print(l1)


# In[54]:


l1 = [i for i in l1 if i % 2 != 0]
print(*l1)


# #### 25. Remove empty tuples from a list

# In[55]:


tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]

def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples

print(Remove(tuples))


# In[56]:


def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples

print(Remove(tuples))


# In[57]:


tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]

def Remove(tuples):
    tuples = filter(None, tuples)
    return tuples

print(Remove(tuples))


# #### 26. print duplicates from a list of integers

# In[58]:


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

l1 = []
for i in list1:
    if i not in l1:
        l1.append(i)

print(l1)


# In[59]:


# Python program to print duplicates from a list of integers

def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print (Repeat(list1))


# In[60]:


from collections import Counter

d = Counter(list1)

for i in d:
    if d[i] > 1:
        print(i)


# In[61]:


from collections import Counter
d = Counter(list1)
result = list([i for i in d if d[i] > 1])
print(result)


# #### 27. find Cumulative sum of a list

# In[62]:


l1 = [10, 20, 30, 40, 50]

new_list = []
j = 0

for i in range(0, len(l1)):
    j = j + l1[i]
    new_list.append(j)   

print(new_list)


# In[63]:


new = []
j = 0
for i in range(0, len(l1)):
    j = j + l1[i]
    new.append(j)
    
print(new)


# #### 28. Break a list into chunks of size N

# In[64]:


my_list = ['geeks', 'for', 'geeks', 'like', 'geeky','nerdy', 'geek', 'love', 'questions','words', 'life']

def divide_chunk(l1, n):
    for i in range(0, len(my_list), n):
        yield l1[i:i + n]
        
n = 5
x = list(divide_chunk(my_list, n))
print(x)


# In[65]:


def divide_chunk(l1, n):
    for i in range(0, len(my_list), n):
        yield l1[i:i+n]
        
print(list(divide_chunk(my_list, 2)))


# In[66]:


def div_chunk(l1, n):
    for i in range(0, len(l1), n):
        yield l1[i: i + n]
        
print(list(div_chunk(my_list, 3)))


# In[67]:


x = [{i: i + 2 for i in range(5)}]
print(x)


# #### 29. Split a list into sublists of given lengths

# In[68]:


l1 = [1, 2, 3, 4, 5, 6, 7]

from itertools import islice
length = [2, 2, 3, 4]
l2 = iter(l1)
output = [list(islice(l2, i)) for i in l1]

print(length)
print(l2)
print(output)


# In[69]:


from itertools import islice
lenght = [2, 3, 4, 2]
l2 = iter(l1)
output = [list(islice(l2, i) for i in l1)]

print(output)


# #### 30. Remove empty List from List

# In[70]:


test_list = [5, 6, [], 3, [], [], 9]

for i in test_list:
    if i != []:
        print(i)


# In[71]:


result = [i for i in test_list if i != []]
print(result)


# #### 31. Convert List to List of dictionaries

# In[72]:


test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

keys = ['name', 'number']
n = len(test_list)
res = []
for i in range(0, n, 2):
    res.append({keys[0]: test_list[i], keys[1]: test_list[i + 1]})
    
print(res)


# In[73]:


key = ['name', 'number']
res = []
for i in range(0, len(test_list), 2):
    res.append({key[0]: test_list[1], key[1]: test_list[i + 1]})
    
print(res)


# #### 32. Convert Lists of List to Dictionary

# In[74]:


test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

res = dict()
for i in test_list:
    res[tuple(i[:2])] = tuple(i[2:])

print(res)


# In[75]:


res = dict()
for i in test_list:
    res[tuple(i[2:])] = tuple(i[:2])

print(res)


# #### 33. Reverse Row sort in Lists of List

# In[81]:


l1 = [[4, 1, 6], [7, 8], [4, 10, 8]]

for i in l1:
    i.sort(reverse = True)
    
print(l1)


# In[82]:


for i in l1:
    i.sort(reverse = True)
    
print(l1)


# #### 34. Pair elements with Rear element in Matrix Row

# In[84]:


l1 = [[4, 1, 6], [7, 8], [4, 10, 8]]

res = []
for i in l1:
    res.append([[j, i[-1]] for j in i[:-1]])

print(res)


# In[85]:


res = []
for i in l1:
    res.append([[j, i[-1]] for j in i[:-1]])
    
print(res)


# In[86]:


for i in l1:
    for j in i[:-1]:
        res.append([j, i[-1]])
    
print(res)


# #### 35. count unique values inside a list

# In[88]:


input_list = [1, 2, 2, 5, 8, 4, 4, 8]

res = []
count = 0

for i in input_list:
    if i not in res:
        count = count + 1
        res.append(i)
        
print(res)
print(count)


# In[89]:


from collections import Counter

l = Counter(input_list).keys()
print(len(l))


# #### 36. program to find the character position of Kth word from a list of strings

# In[90]:


l1 = ["geekforgeeks", "is", "best", "for", "geeks"]

k = 2
res = [i[0] for j in enumerate(l1) for i in enumerate(j[1])]
res = res[k]
print(res)


# #### 37. Extract words starting with K in String List

# In[91]:


l1 = ["geekforgeeks", "is", "best", "for", "geeks"]

k = 'g'
res = []
for i in l1:
    sp = i.split()
    for j in sp:
        if j[0].lower() == k.lower():
            res.append(j)
            
print(res)


# In[92]:


k = 'i'
res = []
for i in l1:
    sp = i.split()
    for j in sp:
        if j[0].lower() == k.lower():
            res.append(j)
            
print(res)


# #### 38. Prefix frequency in string List

# In[94]:


l1 = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']
k = 'gf'
res = 0
for i in l1:
    if i.startswith(k):
        res = res + 1
        
print(res)


# In[95]:


k = 'gfg'
res = 0
for i in l1:
    if i.startswith(k):
        res = res + 1
        
print(res)


# #### 39. Split String of list on K character

# In[100]:


l1 = ['Gfg is best', 'for Geeks', 'Preparing']

k = ' '
res = []
for i in l1:
    sub = i.split(k)
    res.extend(sub)
    
print(res)


# In[101]:


k = ' '
res = []
for i in l1:
    sub = i.split(k)
    res.extend(sub)
    
print(res)


# In[102]:


ress = k.join(l1).split(k)
print(ress)


# In[103]:


result = k.join(l1).split(k)
print(result)


# #### 40 . Split Strings on Prefix Occurrence

# In[110]:


l1 = ["geeksforgeeks", "best", "geeks", "and", "geeks", "love", "CS"]

pre = 'geek'
res = []
for i in l1:
    if i.startswith(pre):
        res.append(i)
        
print(res)


# #### 41. Replace all Characters of a List Except the given character

# In[120]:


l1 = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']

repl_chr = '$'
ret_chr = 'G'

res = [i if i == ret_chr else repl_chr for i in l1]
print(res)


# #### 42. Ways to remove multiple empty spaces from string List

# In[124]:


l1 = ['gfg', '   ', ' ', 'is', '            ', 'best']

res = []

for i in l1:
    if i.strip():
        res.append(i)
    
print(res)


# In[126]:


res = []
for i in l1:
    if i.strip():
        res.append(i)
        
print(res)


# #### 43. Convert Character Matrix to single String

# In[132]:


l1 = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]

res = "".join(j for i in l1 for j in i)
print(res)


# In[133]:


res = "".join(j for i in l1 for j in i)
print(res)


# #### 44. Count Strings with substring String List

# In[135]:


l1 = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

sub = "Geek"
res = len([i for i in l1 if sub in i])
print(res)


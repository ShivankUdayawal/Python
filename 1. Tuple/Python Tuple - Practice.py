#!/usr/bin/env python
# coding: utf-8

# ### Tuple Exercie
# 
# * https://pynative.com/python-tuple-exercise-with-solutions/
# 
# * https://www.geeksforgeeks.org/python-tuple-exercise/

# #### 1. Reverse the tuple

# In[1]:


tuple1 = (10, 20, 30, 40, 50)

print(tuple1[::-1])


# #### 2. Access value 20 from the tuple

# In[2]:


tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

tuple1[1][1]


# #### 3. Create a tuple with single item 50

# In[3]:


tuple1 = (50,)
print(tuple1)
print(type(tuple1))


# #### 4. Unpack the tuple into 4 variables

# In[4]:


tuple1 = (10, 20, 30, 40)

a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)


# #### 5. Swap two tuples in Python

# In[5]:


tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)


# #### 6. Copy specific elements from one tuple to a new tuple

# In[6]:


tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[3:5]
print(tuple2)


# #### 7. Modify the tuple

# In[7]:


tuple1 = (11, [22, 33], 44, 55)

tuple1[1][0] = 222
print(tuple1)


# #### 8. Sort a tuple of tuples by 2nd item

# In[8]:


tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

tuple1 = tuple(sorted(list(tuple1), key = lambda i : i[1]))
print(tuple1)


# In[9]:


tuple1 = tuple(sorted(list(tuple1), key = lambda i : i[1]))
print(tuple1)


# #### 9. Counts the number of occurrences of item 50 from a tuple

# In[10]:


tuple1 = (50, 10, 60, 70, 50)

count = 0
for i in tuple1:
    if i == 50:
        count = count + 1
        
print(count)


# In[11]:


print(tuple1.count(50))


# #### 10. Check if all items in the tuple are the same

# In[12]:


tuple1 = (45, 45, 45, 45)

def chck(t):
    return all(i == t[0] for i in t)

print(chck(tuple1))


# In[13]:


def chck(t):
    return all(i == t[0] for i in t)

print(chck(tuple1))

for i in t:
    return all(i == t[0])
# #### 11. size of a Tuple in Python

# In[14]:


Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))


import sys

print("Size of tuple 1", str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of tuple 2", str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of tuple 3", str(sys.getsizeof(Tuple3)) + "bytes")


# In[15]:


print(str(sys.getsizeof(Tuple1)) + "bytes")


# In[16]:


print(str(Tuple1.__sizeof__()) + "bytes")


# * an inbuilt __sizeof__() method to determine the space allocation of an object without any additional garbage value.

# #### 12. Maximum and Minimum K elements in Tuple

# In[17]:


t1 = (5, 20, 3, 7, 6, 8)

t2 = list(sorted(t1))
t2 = tuple(t2)
print(t2[0])
print(t2[-1])


# #### 13. create a list of tuples from given list having number and its cube in each tuple

# In[18]:


l1 = [1, 2, 3, 4, 5]

l2 = []
for i in l1:
    i = i * i * i
    l2.append(i)
    
print(l2)


# In[19]:


l2 = [(i, pow(i, 3)) for i in l1]
print(l2)


# In[20]:


l2 = [(i, pow(i, 3)) for i in l1]
print(l2)


# #### 14. Adding Tuple to List and vice – versa

# In[21]:


l1 = [1, 2, 3]

t1 = (4, 5)

l1 += t1
print(l1)


# In[22]:


t2 = tuple(list(t1) + l1)
print(t2)


# In[23]:


t2 = tuple(list(t1) + l1)
print(t2)


# #### 15. Sum of tuple elements

# In[24]:


t1 = (7, 8, 9, 1, 10, 7) 

s = sum(list(t1))
print(s)


# In[25]:


t1 = ([7, 8], [9, 1], [10, 7]) 

res = sum(list(map(sum, list(t1))))
print(res)


# In[26]:


res = sum(list(map(sum, list(t1))))
print(res)


# #### 16. Modulo of tuple elements

# In[27]:


t1 = (10, 4, 5, 6)
t2 = (5, 6, 7, 5)

res = [i % j for i, j in zip(t1, t2)]
print(res)


# #### 17. Row-wise element Addition in Tuple Matrix

# In[28]:


t1 = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]

j = [6, 7, 8]

res = [[(idx, val) for idx in key] for key,  val in zip(t1, j)]
print(res)


# In[29]:


res = [[(a, b) for a in i] for i, b in zip(t1, j)]
print(res)


# In[30]:


for a, b in zip(t1, j):
    for c in a:
        print((c, b))
        


# In[31]:


for a, b in zip(t1,j):
    for c in a:
        print((c, b))


# #### 18. Update each element in tuple list

# In[32]:


t1 = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]

a = 4

for i in t1:
    for j in i:
        print((j + 4))


# In[33]:


res = [tuple((j + 4) for j in i) for i in t1]
print(res)


# In[34]:


res = [tuple(map(lambda i: i + a, j)) for j in t1]
print(res)


# #### 19. Multiply Adjacent elements

# In[35]:


t1 = (1, 5, 7, 8, 10)

res = tuple(i * j for i, j in zip(t1, t1[1:])) 
print(res)


# In[36]:


for i, j in zip(t1, t1[1:]):
    print((i * j))


# In[37]:


res = tuple(map(lambda i,j : i * j, t1[1:], t1[:-1]))
print(res)


# #### 20. Join Tuples if similar initial element

# In[38]:


l1 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

res = []
for sub in l1:                                           
    if res and res[-1][0] == sub[0]:              
        res[-1].extend(sub[1:])                        
    else:
        res.append([ele for ele in sub])   
            
res = list(map(tuple, res))
print(res)


# In[39]:


res = []
for sub in l1:                                           
    if res and res[-1][0] == sub[0]:              
        res[-1].extend(sub[1:])                        
    else:
        res.append([ele for ele in sub]) 
        
res = list(map(tuple, res))
print(res)


# #### 21. All pair combinations of 2 tuples

# In[40]:


test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

res = [(a, b) for a in test_tuple1 for b in test_tuple2]
res = res + [(b, a) for a in test_tuple1 for b in test_tuple2]

print(res)


# In[41]:


res = [(a, b) for a in test_tuple1 for b in test_tuple2]
res = res + [(b, a) for a in test_tuple1 for b in test_tuple2]

print(res)


# #### 22. Remove Tuples of Length K

# In[42]:


t1 = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

#Remove Tuples of Length K
k = 1

res = [i for i in t1 if len(i) != k]
print(res)


# In[43]:


res = [i for i in t1 if len(i) != k]
print(res)


# In[44]:


res = list(filter(lambda i : len(i) != k, t1))
print(res)


# #### 23. Remove Tuples from the List having every element as None

# In[45]:


t1 = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]

res = [i for i in t1 if  not all(j == None for j in i)]
print(res)


# In[46]:


res = [i for i in t1 if not all(j == None for j in i)]
print(res)


# In[47]:


res = [i for i in t1 if not all(j == None for j in i)]
print(res)


# #### 24. sort a list of tuples by second

# In[48]:


tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]

def sort_tupl(tup):
    tup.sort(key = lambda x : x[1])
    return tup

print(sort_tupl(tup))


# In[49]:


def sort_tup(tup):
    tup.sort(key = lambda x : x[1])
    return tup

print(sort_tup(tup))


# In[50]:


def sort_tup(tup):
    return sorted(tup, key = lambda x: x[1])

print(sort_tup(tup))


# #### 25. Sort Tuples by Total digits

# In[51]:


l1 = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]

res = sorted(l1, key = lambda tup : sum([len(str(ele)) for ele in tup ]))
print(res)


# In[52]:


res = sorted(l1, key = lambda i : sum([len(str(j)) for j in i]))
print(res)


# In[53]:


res = sorted(l1, key = lambda i : sum([len(str(j)) for j in i]))
print(res)


# #### 26. Elements frequency in Tuple

# In[54]:


t1 = (4, 5, 4, 5, 6, 6, 5, 5, 4)

from collections import defaultdict
res = defaultdict(int)
for i in t1:
    res[i] = res[i] + 1
    
print(dict(res))


# In[55]:


from collections import Counter
res = dict(Counter(t1))
print(res)


# In[56]:


from collections import Counter
res = dict(Counter(t1))
print(res)


# #### 27. Filter Range Length Tuples

# In[57]:


l1 = [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]

i , j = 2, 3

res = [a for a in l1 if len(a) >= i and len(a) <= j]
print(res)


# In[58]:


res = [a for a in l1 if len(a) >= i and len(a) <= j]
print(res)


# In[59]:


res = list(filter(lambda a : len(a) >= i and len(a) <= j, l1))
print(res)


# #### 28. Assign Frequency to Tuples

# In[60]:


l1 = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]

from collections import Counter

rea = [(* kay, val) for kay, val in Counter(l1).items()]
print(rea)


# In[61]:


res = [(*key, val) for key, val in Counter(l1).items()]
print(res)


# In[62]:


res = [(*key, val) for key, val in Counter(l1).most_common()]
print(res)


# In[63]:


res = [(*key, val) for key, val in Counter(l1).most_common()]
print(res)


# #### 29. Records with Value at K index

# In[64]:


l1 = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]

ele = 3
k = 1

res = []
for x, y, z in l1:
    if y == ele:
        res.append((x, y, z))
        
print(res)


# In[65]:


res = [b for a, b in enumerate(l1) if b[k] == ele]
print(res)


# In[66]:


res = [b for a, b in enumerate(l1) if b[k] == ele]
print(res)


# #### 30. Test if tuple is distinct

# In[67]:


test_tup = (1, 4, 5, 6, 1, 4)

res = True
temp = set()
for i in test_tup:
    if i in temp:
        res = False
        break
    temp.add(i)
    
print(res)


# In[68]:


res = len(set(test_tup)) == len(test_tup)
print(res)


# In[69]:


res = len(set(test_tup)) == len(test_tup)
print(res)


# #### 31. find tuples which have all elements divisible by K from a list of tuples

# In[70]:


l1 = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]

K = 6

res = [i for i in l1 if all(j % K == 0 for j in i)]
print(str(res))


# In[71]:


res = [i for i in l1 if all(j % K == 0  for j in i)]
print(res)


# In[72]:


res = list(filter(lambda i : all(j % K == 0 for j in i), l1))
print(res)


# #### 32. find Tuples with positive elements in List of tuples

# In[73]:


l1 = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]

res = [i for i in l1 if all(j > 0 for j in i)]
print(res)


# In[74]:


res = list(filter(lambda i : all(j > 0 for j in i), l1))
print(res)


# #### 33. Count tuples occurrence in list of tuples

# In[75]:


Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')], [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]

import collections

output = collections.defaultdict(int)

for i in Input:
    output[i[0]] += 1
    
print(output)


# In[76]:


from collections import Counter
from itertools import chain

output = Counter(chain(*Input))
print(output)


# In[77]:


from collections import Counter
from itertools import chain

print(Counter(chain(*Input)))


# #### 34. Removing duplicates from tuple

# In[78]:


t1 = (1, 3, 5, 2, 3, 5, 1, 1, 3)

print(tuple(set(t1)))


# In[79]:


from collections import OrderedDict
res = tuple(OrderedDict.fromkeys(t1).keys())
print(res)


# In[80]:


from collections import OrderedDict
res = tuple(OrderedDict.fromkeys(t1).keys())
print(res)


# #### 35. Remove duplicate lists in tuples (Preserving Order)
t1 = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])

temp = set()
res = [i for i in t1 if not tuple((i) in temp or temp.add(tuple(i)))]
print(res)
# In[81]:


t1 = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])

from collections import OrderedDict
res = list(OrderedDict((tuple(x), x) for x in t1).values())
print(res)


# In[82]:


from collections import OrderedDict
res = list(OrderedDict((tuple(x), x) for x in t1).values())
print(res)


# In[83]:


from collections import OrderedDict
res = list(OrderedDict((tuple(i), i) for i in t1).values())
print(res)


# #### 36. Extract digits from Tuple list

# In[84]:


l1 = [(15, 3), (3, 9), (1, 10), (99, 2)]

from itertools import chain
temp = map(lambda x: str(x), chain.from_iterable(l1))
res = set()
for i in temp:
    for x in i:
        res.add(x)
        
print(res)


# In[85]:


import re
temp = re.sub(r'[\[\]\(\), ]', '', str(l1))
res = [int(i) for i in set(temp)]
print(res)


# #### 37. Cross Pairing in Tuple List

# In[86]:


test_list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

res = [(i[1], j[1]) for i in test_list1 for j in test_list2 if i[0] == j[0]]
print(res)


# In[87]:


res = [(i[1], j[1]) for i, j in zip(test_list1, test_list2) if i[0] == j[0]]
print(res)


# #### 38. Consecutive Kth column Difference in Tuple List

# In[88]:


l1 = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]

k = 1
res = []

for i in range(0, len(l1) - 1):
    res.append(abs(l1[i][k] - l1[i + 1][k]))
    
print(res)


# In[89]:


res = [abs(i[k] - j[k]) for i, j in zip(l1, l1[1:])]
print(res)


# In[90]:


k = 2
res = [abs(i[k] - j[k]) for i,j in zip(l1, l1[1:])]
print(res)


# #### 39. Kth Column Product in Tuple List

# In[91]:


l1 = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]

k = 1
res = [(i[k] * j[k]) for i, j in zip(l1, l1[1:])]
print(res)


# In[92]:


l1 = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]

def prod(j):
    res = 1
    for i in j:
        res *= i
    return res

k = 2

res = prod([a[k] for a in l1])
print(res)


# In[93]:


k = 1
res = [(i[k] * j[k]) for i, j in zip(l1, l1[1:])]
print(res)


# In[94]:


def prod(j):
    res = 1
    for i in j:
        res *= i
    return res

k = 1
res = prod([a[k] for a in l1])
print(res)


# #### 40. Flatten tuple of List to tuple

# In[95]:


t1 = ([5, 6], [6, 7, 8, 9], [3])

res = tuple(sum(t1, []))
print(res)


# In[96]:


from itertools import chain
res = tuple(chain.from_iterable(t1))
print(res)


# In[97]:


res = tuple(sum(t1, []))
print(res)


# #### 41. Flatten Tuples List to String

# In[98]:


l1 = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]

res = ' '.join([j for i in l1 for j in i])
print(res)


# In[99]:


res = ' '.join([j for i in l1 for j in i])
print(res)


# In[100]:


from itertools import chain
res = ' '.join(chain(*l1))
print(res)


# In[101]:


from itertools import chain
res = ' '.join(chain(*l1))
print(res)


# #### 42. Sort a list of tuples alphabetically

# In[102]:


tup = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]

def sorttup(tup):
    tup.sort(key = lambda x: x[0])
    return tup

print(sorttup(tup))


# In[103]:


def sorttup(tup):
    tup.sort(key = lambda x: x[0])
    return tup

print(sorttup(tup))


# In[104]:


def sortedtup(tup):
    return sorted(tup, key = lambda x: x[0])

print(sortedtup(tup))


# #### 43. Combinations of sum with tuples in tuple list

# In[105]:


l1 = [(2, 4), (6, 7), (5, 1), (6, 10)]

res = [(i[0] + j[0], i[1] + j[1]) for i, j in zip(l1, l1[1:])]
print(res)


# In[106]:


from itertools import combinations
res = [(a1 + b1, a2 + b1) for (a1, a2), (b1, b2) in combinations(l1, 2)]
print(res)


# In[107]:


from itertools import combinations
res = [(a1 + b1, a2 + b2) for (a1, a2), (b1, b2) in combinations(l1, 2)]
print(res)


# #### 44. Custom sorting in list of tuples

# In[108]:


l1 = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]

res = sorted(l1, key = lambda x: (-x[0], x[1]))
print(res)


# In[109]:


l1 = [(7, (8, 4)), (5, (6, 1)), (7, (5, 3)), (10, (5, 4)), (10, (1, 3))]
res = sorted(l1, key = lambda x: (-x[0], x[1]))
print(res)


# #### 45. Convert tuple into list by adding the given string after every element

# In[110]:


t1 = (5, 6, 7, 4, 9)

k = 'abc'

res = [j for i in t1 for j in (i, k)]
print(res)


# In[111]:


res = [j for i in t1 for j in (i, k)]
print(res)


# #### 46. Convert Tuple Matrix to Tuple List

# In[112]:


l1 = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]

res = [j for i in l1 for j in i]
res = list(zip(*res))
print(res)


# In[113]:


res = [j for i in l1 for j in i]
res = list(zip(*res))
print(res)


# #### 47. Convert Tuple to Tuple Pair

# In[114]:


t1 = ('G', 'F', 'G')

from itertools import product

t1 = iter(t1)
res = list(product(next(t1), t1))
print(res)


# In[115]:


t1 = ('G', 'F', 'G')
from itertools import product
t1 = iter(t1)
res = list(product(next(t1), t1))
print(res)


# In[116]:


t1 = ('G', 'F', 'G', 'H', 'K', 'l')
from itertools import product
t1 = iter(t1)
res = list(product(next(t1), t1))
print(res)


# #### 48. Convert List of Lists to Tuple of Tuples

# In[117]:


l1 = [['Gfg', 'is', 'Best'], ['Gfg', 'is', 'love'], ['Gfg', 'is', 'for', 'Geeks']]

res = tuple(j for i in l1 for j in i)
print(res)


# In[118]:


l1 = [['Gfg', 'is', 'Best'], ['Gfg', 'is', 'love'], ['Gfg', 'is', 'for', 'Geeks']]

res = tuple(tuple(i) for i in l1)
print(res)


# In[119]:


res = tuple(tuple(i) for i in l1)
print(res)


# In[120]:


res = tuple(map(tuple, l1))
print(res)


# #### 49. Convert Matrix to Custom Tuple Matrix

# In[121]:


l1 = [[4, 5, 6], [6, 7, 3], [1, 3, 4]]

l2 = ['abc', 'is', 'best']

res = [(i,a) for i, j in zip(l2, l1) for a in j]
print(res)


# In[122]:


res = [(i, a) for i, j in zip(l2, l1) for a in i]
print(res)


# #### 50. Convert Nested Tuple to Custom Key Dictionary

# In[123]:


t1 = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]} 
                               for sub in t1]

print(res)


# #### 51. Convert tuple to float value

# In[124]:


test_tup = (4, 56)

res = float('.'.join(str(i) for i in test_tup))
print(res)


# In[125]:


res = float('.'.join(str(i) for i in test_tup))
print(res)


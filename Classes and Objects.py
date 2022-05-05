#!/usr/bin/env python
# coding: utf-8

# * Python is an object oriented programming language.
# 
# * Almost everything in Python is an object, with its properties and methods.
# 
# * A Class is like an object constructor, or a "blueprint" for creating objects.

# In[1]:


class MyClass:
    x = 5


# In[2]:


MyClass


# In[3]:


f1 = MyClass()
print(f1.x)


# ### __init__() Function
# 
# *  built-in __init__() function.
# 
# * All classes have a function called __init__(), which is always executed when the class is being initiated.
# 
# * Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# In[4]:


# Create a class named Person, use the __init__() function to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("John", 24)
print(p1.name)
print(p1.age)


# In[5]:


class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
p2 = Student("jonny", "sam")
print(p2.firstname)
print(p2.lastname)


# #### Object Methods
# 
# * Objects can also contain methods. Methods in objects are functions that belong to the object.

# In[6]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfun(self):
        print("Hello my name is " + self.name)
        

p1 = Person("John", 24)
p1.myfun()


# In[7]:


class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def myfun(self):
        print("Student's First Name is " + self.firstname)
        print("Student's Last Name is  " + self.lastname)
        
p2 = Student("jonny", "sam")
print(p2.firstname)
print(p2.lastname)
p2.myfun()


# #### The self Parameter
# 
# * The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# 
# * It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# In[8]:


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


# In[9]:


class Student:
    def __init__(record, firstname, lastname):
        record.firstname = firstname
        record.lastname = lastname
        
    def myfun(abc):
        print("Student's First Name is " + abc.firstname)
        print("Student's Last Name is  " + abc.lastname)
        
p2 = Student("jonny", "sam")
print(p2.firstname)
print(p2.lastname)
p2.myfun()


# In[10]:


# Set the age of p1 to 40:

p1.age = 40


# In[11]:


print(p1.age)


# In[12]:


#delete properties on objects 

del p1.age


# In[13]:


# delete object

del p1


# In[14]:


class Person:
    pass


# ### Python Inheritance
# 
# * Inheritance allows us to define a class that inherits all the methods and properties from another class.
# 
# * Parent class is the class being inherited from, also called base class.
# 
# * Child class is the class that inherits from another class, also called derived class.

# #### Parent Class
# 
# * Any class can be a parent class, so the syntax is the same as creating any other class:

# In[15]:


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def myfun(self):
        print(self.fname, self.lname)
        
x = Person("Sam", "Billy")
x.myfun()        


# #### Create a Child Class
# 
# * To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# In[16]:


#Create a class named Students, which will inherit the properties and methods from the Person class:

class Students(Person):
    pass


# In[17]:


#Use the Students class to create an object, and then execute the myfun method:

x = Students("jonny", "Roon")
x.myfun()


# In[18]:


y = Students("Samm", "Curen")
y.myfun()


# #### __init__() Function
# 
# * So far we have created a child class that inherits the properties and methods from its parent.
# 
# * We want to add the __init__() function to the child class (instead of the pass keyword).
# 
# 
# * The __init__() function is called automatically every time the class is being used to create a new object.

# In[19]:


class Students(Person):
    __init__(self, fname, lname):
        


# * When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# 
# 
# 
# * Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# 
# 
# 
# * To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# In[20]:


class Students(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        
x = Students("Jon", "Ripp")
x.myfun()


# #### super() Function
# 
# * Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# In[21]:


class Students(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        
x = Students("Shi", "Ham")
x.myfun()


# In[22]:


class Students(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2015
        
x = Students("Shi", "Ham")
x.myfun()
print(x.graduationyear)


# In[23]:


class Students(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2015
        self.totalpercentage = 80.00
        
x = Students("Shi", "Ham")
x.myfun()
print(x.graduationyear)
print(x.totalpercentage)


# In[24]:


class Students(Person):
    def __init__(self, fname, lname, year, perc):
        super().__init__(fname, lname)
        self.graduationyear = year
        self.totalpercentage = perc
        
x = Students("Shi", "Ham", 2020, 90)
print(x.graduationyear)
print(x.totalpercentage)


# In[25]:


class Students(Person):
    def __init__(self, fname, lname, year, perc):
        super().__init__(fname, lname)
        self.graduationyear = year
        self.totalpercentage = perc
        
    def welcome(self):
        print("Welcome", self.fname, self.lname, " to the class of ", self.graduationyear, " who having total percenatge ", 
              self.totalpercentage)
        
z = Students("Ron", "Jin", 2021, 95)
z.welcome()


# In[26]:


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def myfun(self):
        print(self.fname, self.lname)
        
class Students(Person):
    def __init__(self, fname, lname, year, perc):
        super().__init__(fname, lname)
        self.graduationyear = year
        self.totalpercentage = perc
        
    def welcome(self):
        print("Welcome", self.fname, self.lname, " to the class of ", self.graduationyear, " who having total percenatge ", 
              self.totalpercentage)
        
z = Students("Ron", "Jin", 2021, 95)
z.welcome()


# In[27]:


#  If you add a method in the child class with the same name as a function in the parent class, 
# the inheritance of the parent method will be overridden.


# ### Python Iterators
# 
# * An iterator is an object that contains a countable number of values.
# 
# * An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# 
# * Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# 
# 
# 
# * Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# In[28]:


mytuple = ("apple", "banana", "kiwi")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# * Even strings are iterable objects, and can return an iterator:
# 
# 

# In[29]:


mystr = "ASDFGQWERTYUIPLO"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


# In[30]:


for i in mytuple:
    print(i)


# In[31]:


for i in mystr:
    print(i)


# In[32]:


# The for loop actually creates an iterator object and executes the next() method for each loop.


# #### Create an Iterator
# 
# * To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# 
# * all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# 
# * The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# 
# * The __next__() method also allows you to do operations, and must return the next item in the sequence.

# In[33]:


# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# In[34]:


class MyNumbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# In[35]:


class mynumber():
    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        x = self.a
        self.a = self.a + 3
        return x
    
myclass = mynumber()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# #### StopIteration
# 
# * The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# 
# * To prevent the iteration to go on forever, we can use the StopIteration statement.
# 
# * In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

# In[36]:


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


# In[37]:


class mynumber():
    def __iter__(self):
        self.a = 0
        return self
    
    def __next__(self):
        if self.a <= 16:
            x = self.a
            self.a = self.a + 2
            return x
        else:
            raise StopIteration
    
myclass = mynumber()
myiter = iter(myclass)

for i in myiter:
    print(i)


# ### Python Scope
# 
# * A variable is only available from inside the region it is created. This is called scope.
# 
# 
# #### Local Scope
# 
# * A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# In[38]:


def myfun():
    x = 100
    return x * 2

myfun()


# In[39]:


def myfun():
    x = 100
    print(x)
    
myfun()


# In[40]:


# Function Inside Function

def myfun():
    x = 100
    def innerfun():
        print(x)
    innerfun()
    
myfun()


# ### Global Scope
# 
# 
# * A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# 
# * Global variables are available from within any scope, global and local.

# In[41]:


x = 150

def myfun():
    print(x)
    
myfun()
print(x)


# #### Naming Variables
# 
# * If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

# In[42]:


x = 150

def myfun():
    x = 200
    print(x)
    
myfun()
print(x)


# #### Global Keyword
# 
# * If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# 
# * The global keyword makes the variable global.

# In[43]:


def myfun():
    global x
    x = 1000
    
myfun()
print(x)


# In[44]:


# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = 100

def myfun():
    global x
    x = 180
    
myfun()
print(x)


# ### Exception Handling
# 
# * When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# 
# 
#  **The try block lets you test a block of code for errors.**
# 
# **The except block lets you handle the error.**
# 
# **The else block lets you execute code when there is no error.**
# 
# **The finally block lets you execute code, regardless of the result of the try- and except blocks.**

# In[45]:


try:
    print(g)
except:
    print("An exception occured")


# In[46]:


# The try block will generate an exception, because g is not defined


# In[47]:


try:
    print(g)
except NameError:
    print("g is not defined")
except:
    print("An exception occured")


# In[48]:


try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# In[49]:


try:
    print(g)
except:
    print("Something went wrong")
finally:
    print("The try - except is finished")


# In[50]:


#The try block will raise an error when trying to write to a read-only file:

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
              f.close()
except:
    print("Something went wrong when opening the file")  


# #### Raise an exception
# 
# * choose to throw an exception if a condition occurs.
# 
# * To throw (or raise) an exception, use the raise keyword.

# In[51]:


j = -1

if j < 0:
    raise Exception("Sorry number should be more than 0")


# In[52]:


v = "Hello"

if not type(v) is int:
    raise TypeError("only intergers are allowed")


# In[ ]:





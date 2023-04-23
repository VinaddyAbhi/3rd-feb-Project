#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q.1 Which keyword is used to create a function? create a function to return a list of odd numbers in the range of 1 to 25.

#Ans = def function is used to create a function.

#Example to create a list of odd numbers in the range 1 t0 25


def get_odd_num():
    a = range(1,25)
    odd_num = []
     
    for i in a :
        if i % 2 != 0:
            odd_num.append(i)
    return odd_num
get_odd_num()


# Q.2 Why *args and *kwargs is used in some functions? Create a function each for *args and *kwargs to demonstrate their use. Ans.We use this when we are unsure about the numbers of arguments to pass in the functions.
# 
# 

# In[2]:


def fn(*args):
    return args
fn(5,[i for i in range(6)])


# kwargs are used to oass key value pairs to functions that return data as a dictionary format
# 
# 

# In[3]:


def total_team(**kwargs):
    print(kwargs , type(kwargs))

    
total_team(team1="GT",team2="DC",team3="RCB")


# 3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2,4,6,8,10,12,14,16,18,20].
# It's an object that allows us to iterate over collections of data, such as lists,tuples, dictionaries, and sets.

# In[4]:


my_list = [2,4,6,8,10,12,14,16,18,20]
myit = iter(my_list)


# In[5]:


print(next(myit))


# In[6]:


print(next(myit))


# In[7]:


print(next(myit))


# In[8]:


print(next(myit))


# In[9]:


print(next(myit))


# Q.4. What is generator function in python? Why yield keyword is used? Give an example of a generator function.
# 
# 
# Ans.Generator is a function that returns an iterator that produces a sequence of values when iterated over.

# In[10]:


def test_gen(n):
    x,y = 0,1
    for i in range(n):
        yield x
        x,y = y , x+y


# In[11]:


for i in  test_gen(10):
    print(i)


# Q.5 Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

# In[12]:


#Here's a generator functions in python that generates prime numbers less than 1000

def primes():
    for num in range(2,1000):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            yield num


# In[13]:


prime_genrator =primes()

for i in range(20):
    print(next(prime_genrator))


# Q5.Write a python program to print the first 10 Fibonacci numbers using a while loop.

# In[14]:


a= 0
b=1
count =0
while count <10:
    print(a,end=" ")
    c = a+b
    a=b
    b=c
    count +=1


# Q.6 Write a List Comprehension to iterate through the given string: ‘pwskills’.

# In[15]:


#Here is the Example

string = 'pwskills'
char_list =[char for char in string]
print(char_list)


# Q.7 Write a List Comprehension to iterate through the given string: ‘pwskills’.

# In[17]:


num = int(input("enter your number"))
temp=num
reverse=0
while temp >0:
    digit = temp % 10
    reverse = reverse *10 +digit
    temp = temp // 10
    
if num==reverse:
    print(num, "is a palindrome")
else:
          print(num,"is not a palindrome")


# Q.8 Write a code to print odd numbers from 1 to 100 using list comprehension.
# 
# first creating a list from 1-100 by using list comprehension

# In[18]:


#Note Use a list comprehension to create a list from 1 to 100

numbers = [num for num in range(1,101)]
print(numbers)


# In[19]:


odd_numbers = [num for num in range(1,101) if num %2 !=0]
print(odd_numbers)


# In[ ]:





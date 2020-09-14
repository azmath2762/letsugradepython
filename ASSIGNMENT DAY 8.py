#!/usr/bin/env python
# coding: utf-8

# In[4]:


file = open("assignment day 8.txt", "r")
file.write("hi letsupgrade")
file.close()


# In[6]:


def getinput(calculate_arg_fun):
    def wrap_function():
        print ("entered numbers are :")
        x=int(input("enter num1 value"))
        y=int(input("enter num1 value"))
        calculate_arg_fun(x,y)
    return wrap_function


# In[13]:


@getinput
def evenorodd(x,y):
    for x in range(x,y):
        if x == 237:
            print(x)
            break;
        elif x % 2 == 0:
            print(x)


# In[14]:


evenorodd()


# In[ ]:





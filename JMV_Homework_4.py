#!/usr/bin/env python
# coding: utf-8

# ### Functions

# starts with: def

# In[14]:


def myfunction(age): 
    new_age = age + 10
    return new_age


# In[15]:


myfunction(30)


# In[20]:


def myfunction():
    age = float(input("Enter your age:  "))
    new_age = age + 10
    return new_age


# In[21]:


myfunction()


# ### Homework #4

# Assignment: Convert degree, minutes, seconds, direction to 

# latdirection * (latdegree + (latminute + latsecond/60.)/60.)

# In[23]:


def convert_degrees_to_decimal(degrees, minutes, seconds, direction):
    degrees = float(degrees)
    minutes = float(minutes)
    seconds = float(seconds)

    decimal = degrees + (minutes + seconds/60) / 60

    if direction in ['S', 'W']:
        decimal *= -1

    return decimal


# In[60]:


degrees = 42
minutes = 12
seconds = 43.44
direction = 'N'

lat_decimal = convert_degrees_to_decimal(degrees, minutes, seconds, direction)
lat_decimal


# In[61]:


degrees = 71
minutes = 6
seconds = 58.18
direction = 'W'

lon_decimal = convert_degrees_to_decimal(degrees,minutes,seconds,direction)
lon_decimal


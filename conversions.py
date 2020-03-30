#!/usr/bin/env python
# coding: utf-8

# In[12]:


def fahr_to_celsius(fahr):
    a = float(fahr) - 32.0
    b = 5.0 / 9
    return a * b


def fahr_to_kelvin(fahr):
    a = float(fahr)
    b = 459.67
    c = 5.0 / 9
    return (a + b) * c


def celsius_to_fahr(celsius):
    a = float(celsius)
    b = 9.0 / 5
    c = 32.0
    return (a * b) + c


def celsius_to_kelvin(celsius):
    a = float(celsius)
    b = 273.15
    return a + b


def kelvin_to_fahr(kelvin):
    a = float(kelvin)
    b = 9.0 / 5
    c = 459.67
    return a * b - c


def kelvin_to_celsius(kelvin):
    a = float(kelvin)
    b = 273.15
    return a - b


if __name__ == '__main__':
    val = 0
    print 'F to C: ', fahr_to_celsius(val)
    print 'F to K: ', fahr_to_kelvin(val)
    print 'C to F: ', celsius_to_fahr(val)
    print 'C to K: ', celsius_to_kelvin(val)
    print 'K to C: ', kelvin_to_celsius(val)
    print 'K to F: ', kelvin_to_fahr(val)


# In[ ]:





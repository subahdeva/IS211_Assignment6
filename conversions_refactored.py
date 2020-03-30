#!/usr/bin/env python
# coding: utf-8

# In[6]:


def convert(from_unit, to_unit, value):
    value = float(value)
    distance = ('mile', 'yard', 'meter')
    temp = ('fahrenheit', 'celsius', 'kelvin')
    metric = str(from_unit).lower()
    span = str(to_unit).lower()
    if metric in distance and span in distance:
        units = {
            'mile': {'mile': value * 1.0,
                     'yard': value * 1760.0,
                     'meter': value * 1609.344},
            'yard': {'mile': value * 1.0 / 1760.0,
                     'yard': value * 1.0,
                     'meter': value * 1609.344 / 1760.0},
            'meter': {'mile': value * 1.0 / 1609.344,
                      'yard': value * 1760 / 1609.344,
                      'meter': value * 1.0}
        }

    elif metric in temp and span in temp:
        units = {
            'fahrenheit': {'fahrenheit': value * 1.0,
                           'celsius': (value - 32.0) * 5.0 / 9,
                           'kelvin': (value + 459.67) * 5.0 / 9},
            'celsius': {'fahrenheit': value * 9.0 / 5.0 + 32.0,
                        'celsius': value * 1.0,
                        'kelvin': value + 273.15},
            'kelvin': {'fahrenheit': value * 9.0 / 5 - 459.67,
                       'celsius': value - 273.15,
                       'kelvin': value * 1.0}
        }
    else:
        msg = 'Conversion from {} to {} is not valid.'             .format(from_unit.title(), to_unit.title())
        raise InvalidConversion(msg)
    return units[metric][span]


class InvalidConversion(Exception):
    pass


if __name__ == '__main__':
    print convert('mile', 'meter', 70)
    print convert('meter', 'celsius', 100)


# In[ ]:





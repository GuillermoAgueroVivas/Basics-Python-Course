#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# When it comes to a list, when using () instead of [], it will turn this list into a tuple which means the values cannot be changed. It is a good practice to use the tuple
# mainly unless you are aware of the fact that later on you will have to change some value in the list.
x = ( 1, 2, 3, 4, 5 )
for i in x:
    print('i is {}'.format(i))

y = [1, 2, 3, 4, 5]
for i in y:
    print('i is {}'.format(i))

# The word range can also be utilized to create a list implying that any number before that number (not including the one inside the brackets in the middle) are part of that list.
# The number before the coma can mark what you would like the beginning number to be.
# The number after the coma can mark how many numbers you want the list to skip by.
# A range is not mutable. To change a range you would have to use the list() contractor. Ex. z = list(range(1, 50, 5))
z = range(1, 50, 5)
for i in z:
    print('i is {}'.format(i))

# This is a dictionary
# Consists of a key and a value
a = {'one': 1, 'two': 2, 'three': 3}
# Using ---> for x, i in a.items(): would return every key together with its value inside the 'for' loop.
a['three'] = 42
for key, value in a.items():
    print(f'Key is {key} and value is {value}')

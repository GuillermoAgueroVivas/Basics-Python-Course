#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# This is a tuple
x = (1, 'two', 3.0, [4, 'four'], 5)
y = [1, 'two', 3.0, [4, 'four'], 5]
print('x is {}'.format(x))
print(type(x[1]))
print(id(y[0]))
print(id(x[0]))

# This checks to see if they are exactly the same object. In this case the value placed in spot [0] fot 'x' has the exact same ID as spot [0] in 'y'
if x[0] is y[0]:
    print('Si')
else:
    print('Nope')

# 'x' and 'y' as a whole are not equal objects
if x is y:
    print('Si')
else:
    print('Nope')

# With this 'isinstance' command we can check if an object is a certain type of object. Ex. a Tuple
if isinstance(y, tuple):
    print('tuple')
elif isinstance(y, list):
    print('list')
else:
    print('Nope')

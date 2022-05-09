#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Number zero, an empty space or a 'None' value in a variable will return False
x = None
print('x is {}'.format(x))
print(type(x))

if x:
    print('True')
else:
    print('False')

#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a =4
b=16
# The .capitalize() will make the string start with a capital. The :>9 or :<9 will allocate that many spaces for the variable inside the {} in the 'f' string. Adding a '0'
# in front of the :> like so :>09 will fill up the spaces with zeros.
x = f'seven {a:<9} {b:>9}'.capitalize()
print('x is {}'.format(x))
print(type(x))

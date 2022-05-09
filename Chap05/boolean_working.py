#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression 1 is true')
else:
    print('expression 1 is false')

if a or b:
    print('expression 2 is true')
else:
    print('expression 2 is false')

if not a:
    print('expression 3 is true')
else:
    print('expression 3 is false')

if not b:
    print('expression 4 is true')
else:
    print('expression 4 is false')

if y in x:
    print('expression 5 is true')
else:
    print('expression 5 is false')

if y not in x:
    print('expression 6 is true')
else:
    print('expression 6 is false')

# Could do the following without the []. This compares if they are the same object.

if y is x[0]:
    print('expression 7 is true')
else:
    print('expression 7 is false')

if y is not x[0]:
    print('expression 8 is true')
else:
    print('expression 8 is false')
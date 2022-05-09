#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

# It is possible to do 'integer division' (meaning it will show without the remainder or decimals) by using double divide sign like so: 7 // 3 = 2. On the other hand,
# it is possible to get this remainder by using the % sign like so: 7 % 3 = 1
x = 7 / 3
print('x is {}'.format(x))
print(type(x))

# With the above import of the 'decimal' library a calculation like the one below (imagining we are dealing with money and those are cents) will properly equal the correct value
# of 0.00
a = Decimal('.10')
b = Decimal('.30')
c = a + a + a - b
print(f'The value of c is {c}')
#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Putting the 1 after the variable requested by the function will make it so if no value is given when the function is called it will default to 1.
def function(n = 1):
    print(n)
    return n * 2

# Without the return statement inside the function, the result cannot be assigned to a variable because it is in fact not 'returning' any value.
x = function(45)
print(x)
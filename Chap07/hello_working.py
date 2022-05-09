#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1(f):
    # print('This is F1')
    # Cannot call F2 directly because its scope is located inside the function.
    def f2():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f2

# This is the same as doing this 'f3 = f1(f3)' (Creating a DECORATOR). This will take the function below and pass it as an argument to 'f1' and then assigned it back to the
# value of 'f3'.
@f1
def f3():
    print('this is F3')

# x = f1()
# The function 'f1' can be called using 'x' because in Python everything is an object so by assigning 'f1' to 'x' above, 'x' then contains the object of 'f1'
# x()

# f3() in its original form is no longer available. Only the rapper is available.
# The assignment could be done like this below, but instead we use the '@' above f3() as a shortcut to do the same.
# f3 = f1(f3)
f3()



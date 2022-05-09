#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = kitten()
    print(type(x), x)

def kitten():
    print('Meow.')
    # Without the return statement the function would go back to the variable 'x' above as a 'None' type due to the fact that nothing is being sent back to it from this function.
    return dict(x = 42, y =43, z = 44)

if __name__ == '__main__': main()

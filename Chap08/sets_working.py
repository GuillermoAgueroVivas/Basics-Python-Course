#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# A set is like a list that does not allow duplicate elements

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    # Could also be sorted
    print_set(sorted(b))
    # Can check to see what members or values that are in Set 'a' are not in Set 'b'
    print(a - b)
    # Can see which ones are in one of both sets
    print(a | b)
    # Can see which members are in 'a' or 'b' but not both
    print(a ^ b)
    # Can see which members are in both
    print(a & b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()

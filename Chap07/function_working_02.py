#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    #kitten(5, 6 ,7)
    x = [5]
    # y = x
    # y[0] = 3
    # print(id(x))
    # print(id(y))
    # print(x)
    # print(y)
    kitten(x)
    print(f'In main X is {x}')

# def kitten(a, b, c):
def kitten(a):
    # You may notice that the value of a[0] (which is the same as x[0]) changing below actually changes the value of both a[0] and x[0] in main, this is because this list in kitten()
    # is a direct reference to the list in main() and these are mutable.
    # If we were talking about an integer, which is not mutable, then changing the value of 'a' in kitten() would not change the value of 'x' in main().
    # Knowing this, it is worth noting that it is really important to BE CAREFUL WHEN DEALING WITH LISTS (OR ANY MUTABLE OBJECT) ACROSS FUNCTIONS.
    a[0] = 3
    print('Meow.')
    print(a)

if __name__ == '__main__': main()

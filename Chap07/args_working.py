#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = ('meow', 'grrr', 'purr')
    # The '*' has to be included
    kitten(*x)
    # Can also be done directly like this ---> kitten('meow', 'grrr', 'purr')
# Utilizing the word 'args' is traditional in python, so it is recommended to use the word when using this method. This allows for the function to take in all given variables
# without having to write them all down again below.
def kitten(*args):
    # If the length of args is higher than 0 then this will run
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()

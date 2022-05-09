#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # Can choose to pass a certain value into the 'function call' below to be carried forward into the function itself as an available value
    kitten(5)
    # x = kitten()
    # print(x)

# We have to specify the function is taking a variable. In this case the variable is identified as 'n'
def kitten(n):
    print(f'{n} Meow.')
    # Return 'Meow'

if __name__ == '__main__': main()

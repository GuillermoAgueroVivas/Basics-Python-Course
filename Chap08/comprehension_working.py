#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    # Every value of 'seq' is multiplied by two
    seq2 = [x * 2 for x in seq]
    # Every value of 'seq' that is not divisible by 3
    seq3 = [x for x in seq if x % 3 != 0]
    # This creates a list with a tuple inside it which shows the original value of the variable in 'seq' and every value of 'seq' multiplied by itself (square root)
    seq4 = [(x, x**2) for x in seq]
    # Imports the value of Pi
    from math import pi
    # Creates a list which shows the value of Pi with decimal places according to the number from each element in 'seq'. Ex. Pi * 2 = 3.14
    seq5 = [round(pi, i) for i in seq]
    # Creates a dictionary where it shows the original value of 'x' with a key equal to 'x' squared.
    seq6 = {x: x**2 for x in seq}
    # Creates a set which displays all letters that are not part of the second string
    seq7 = {x for x in 'BigPotato' if x not in 'og'}

    print_list(seq)
    print_list(seq2)
    print_list(seq3)
    print_list(seq4)
    print_list(seq5)
    print(seq6)
    print_list(seq7)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

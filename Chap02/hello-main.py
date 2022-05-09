#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import platform

def main():
    message()

def message():
    print('This is python version {}'.format(platform.python_version()))

# Very common pattern in Python. By having this conditional line at the end of the code, it forces the interpreter to read the entire script before it executes any of the code
if __name__ == '__main__': main()

# An expression is any combinations of literals, identifiers and operators. Generally that mean that anything that returns a value is an expression.
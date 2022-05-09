#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    kitten(**x)

# In this case we require '**' to be able to pass all arguments above with their specific value
# Kwargs stands for 'Key Word Arguments'
def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()

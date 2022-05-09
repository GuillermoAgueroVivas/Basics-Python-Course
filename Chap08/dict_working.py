#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr',
        giraffe = 'I am a giraffe!', dragon = 'rawr')

    #for k , v in animals.items():
        #print(f'{k}: {v}')

    # This method below will print only the keys
    for k in animals.keys(): print(k)
    # Or just the values
    for h in animals.values(): print(h)
    # It is originally written the way it is shown below
    # animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
    #   'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)
    # How to print using the key.
    print(animals['lion'])
    # Changing the value of the key or add new value
    animals['lion'] ='I am a lion'
    animals['crocodile'] = 'Gotcha bih'
    print_dict(animals)
    # Search by key
    print('lion' in animals)
    # Print if found
    print('found!' if 'lion' in animals else 'not found!')

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()

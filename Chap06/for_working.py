#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    if pet == 'dog': continue
    # If the break function below is executed then the 'else' statement will not be printed.
    # if pet == 'velociraptor': break
    print(pet)
else:
    print('That is all the animals in this list :)')


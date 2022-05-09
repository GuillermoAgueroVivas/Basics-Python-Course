#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    # Item number 1 below is actually the second item in the list 'games' due to the facts that lists start at zero. The number after the ':' indicates to also print item number
    # 2 because while we are writing '3', it does not include itself.
    print(game[1:3])
    # With the built-in function below we can search for an item in a list and assign it to a variable and then call it directly using that variable
    i = game.index('Paper')
    print(game[i])
    # While adding a variable to the list, the number before can indicate where in the list is this variable going to be added by using 'insert'
    game.insert(0, 'Geoff')
    # We can also remove items from the list
    game.remove('Rock')
    # Using the function 'pop', we can also remove an item from the end of the list (in this process it is not only removing the last item, it is also returning its value, so we can
    # assign it)
    game.pop()
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()

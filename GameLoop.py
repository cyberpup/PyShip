'''
Created on Oct 17, 2014

@author: Ray "Cyberpup" Tong
'''
from GameLogic import GameLogic
from GameGrid import GameGrid
import sys




def isValidGuess(guess): 
    row = "abcdefghij"
    col = "0123456789"
    
    if not len(guess)==2:
        return False
    elif guess[0] in row and guess[1] in col:
        return True
    else:
        return False


print ("""\

Welcome to PYSHIP!

A battleship game written in Python

version 1.0
By Raymond Tong

""")

'''
Initialize Game Logic

Takes the user input 
calculates hits/misses 
Keeps score
'''
logic = GameLogic()

'''
Initialize Game View

Displays Game Grid
'''
grid = GameGrid()

# Game Loop
while True:
    grid.display()
    guess = raw_input("Your guess: ")
    print""
    
    while not isValidGuess(guess):
        guess = raw_input("Please guess again: ")
        print""
        
    if logic.fire(guess):
        grid.update(guess)
        grid.display()
    
    

'''
Created on Oct 17, 2014

@author: Ray "Cyberpup" Tong
'''
from GameLogic import GameLogic
from GameGrid import GameGrid
from HumanView import HumanView
from AI_View import AI_View

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
game = GameLogic()

'''
Initialize Game View

Displays Game Grid
'''
grid = GameGrid()

'''
Initialize Human View

Helps Player place ships
'''
player = HumanView(game, grid)

'''
Initialize AI View

'''
ai = AI_View(game)

# Game Loop
while True:
    
    # Begin Game
    
    grid.displayDual()
    
    
    # Player goes first
    guess = player.guess()
    
    # Check if guess is valid
    while not isValidGuess(guess):
        guess = raw_input("Please guess again: ")
        print""
        
    
    '''
    result, label, shipKey = game.fire(guess)

    if result:
        if label == "X":
            grid.updateAI(guess, label)
            print("hit!")
        else:
            # Find a way to update all labels in grid
            for ship in game.ships[shipKey]:
                grid.updateAI(ship, label)
            print("Ship sunk!")
    else:
        print("Miss!")
        
    print""
    
    '''

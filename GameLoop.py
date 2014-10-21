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

def update(guess, opponent):
    
    result, label, shipKey = game.fire(guess)
    if result:
        if label == "X":
            grid.update(guess, label, opponent)
            print("hit!")
        else:
            for ship in game.ships[shipKey]:
                grid.update(ship, label, opponent)
            print("Ship sunk!")
    else:
        print("Miss!")  
    print""


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

# Begin Game
while True:
    
    # Display Game Grid
    grid.displayDual()  

    # Player's Turn
    guess = player.guess()
    
    # Check if guess is valid
    while not isValidGuess(guess):
        guess = raw_input("Please guess again: ")
        print""

    update(guess, "ai")
    
    # AI's Turn
    guess = ai.guess()
    update(guess, "player")



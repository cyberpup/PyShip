'''
Created on Oct 17, 2014

@author: Ray "Cyberpup" Tong
'''
from GameLogic import GameLogic
from GameGrid import GameGrid
from HumanView import HumanView
from AI_View import AI_View

def isValidGuess(guess): 
    row = "ABCDEFGHIJ"
    col = "0123456789"
    
    if not len(guess)==2:
        return False
    elif guess[0] in row and guess[1] in col:
        return True
    else:
        return False


# Updates the display for either player type
def update(guess, opponent):
    
    result, label, shipKey = game.fire(guess, opponent)
    
    # opponent = AI
    if opponent == 'AI':
        print "Results:"
        if result:
            if label == "X":
                grid.update(guess, label, opponent)
                print("You hit one of the AI's ship!"),
            else:
                for cell in game.aiShips[shipKey]:
                    grid.update(cell, label, opponent)
                print("You sunk an AI ship!"),
        else:
            print("You missed!"),
    # opponent = player
    else:
        if result:
            
            if label == "X":
                grid.update(guess, label, opponent)
                print("AI hit one of your ships!")
            else:
                label = "O" # return to ocean label
                grid.update(guess, label, opponent)
                
                for cell in game.playerShips[shipKey]:
                    grid.update(cell, label, opponent)
                print("AI sunk your ship!")
        else:
            print("AI missed!")
        
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
# DEBUGprint grid.playerGrid  
# DEBUGprint game.playerShips 

'''
Initialize AI View

'''
ai = AI_View(game, grid)
# DEBUGprint grid.aiGrid  
# DEBUGprint game.aiShips 

# Begin Game
print ""
print "Begin!"

while True:
    
    # Display Game Grid
    grid.displayDual()  

    # Player's Turn
    guess = player.guess()
    update(guess, "AI")
    
    # Gave Over?
    #DEBUGprint "ai ships:",game.getNumOfShips('AI') 
    if game.getNumOfShips('AI') == 0:
        print("Game over. You win!")
        break
    
    # AI's Turn
    guess = ai.guess()
    update(guess, "player")
    
    # Gave Over?
    #DEBUGprint "player ships:",game.getNumOfShips('player') 
    if game.getNumOfShips('player') == 0:
        print("Game over. You lose!")
        break

# Display Final Grids
grid.displayDual()

'''
PyShip game loop

Created on Oct 17, 2014

@author: Ray "Cyberpup" Tong
'''
from GameLogic import GameLogic
from GameGrid import GameGrid
from HumanView import HumanView
from AI_View import AI_View

<<<<<<< HEAD
# Determines if guess is valid
# Returns True if point is on the grid
def isValidGuess(guess): 
    row = "ABCDEFGHIJ"
    col = "0123456789"
    
    if not len(guess)==2:
        return False
    elif guess[0] in row and guess[1] in col:
        return True
    else:
        return False

# GameLogic returns results of the guess
# result = hit/miss
# label = 
# Updates the display for either player type
def update(guess, opponent):
=======
'''
Evaluates player's guess against opponent fired upon:
1. If the opponent's ship is hit, opponent's display grid is updated
2. Prints results of the shot

'''
def shootAt(guess, opponent):
>>>>>>> debug
    
    result, label, shipKey = game.fire(guess, opponent) # Retrieve results of the guess
    
    if opponent == 'AI':                                # Opponent = AI
        print "Results:"
        if result:                                      # Hit 
            if label == "X":                            # Ship did not sink
                grid.update(guess, label, opponent)     # update display with a "X"
                print("You hit one of the AI's ship!"),          
            else:      
                for cell in game.aiShips[shipKey]:      # Sunk ship
                    grid.update(cell, label, opponent)  # reveal ship type on game grid for human player
                print("You sunk an AI ship!"),         
        else:                                           # Miss     
            print("You missed!"),      
                                                        
    else:                                               # Opponent = Human
        if result:                                      # Hit   
            if label == "X":                            # Ship did not sink
                grid.update(guess, label, opponent)     # update display with a "X"
                print("AI hit one of your ships!")        
            else:    
                label = "O"                             # Sunk ship             
                for cell in game.humanShips[shipKey]:   # removes ship from the display grid
                    grid.update(cell, label, opponent)
<<<<<<< HEAD
                print("You sunk an AI ship!"),
        else:
            print("You missed!"),
    # opponent = human
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
=======
                print("AI sunk your ship!")          
        else:                                           # Miss
>>>>>>> debug
            print("AI missed!")
    print""

def showTitle():                                        # Title & Credits
    
    print ("""\
    
    Welcome to PYSHIP V1.0
    
    A battleship game written in Python
    
    By Ray "Cyberpup" Tong
    
    """)


showTitle()
'''
Initialize Key objects
'''
game = GameLogic()
grid = GameGrid()
human = HumanView(game, grid)
ai = AI_View(game, grid)

'''
Begin game
'''
print ""
print "Begin!"

while True:                                             # Main loop
    grid.displayDual()                                  # Display game grid 
    guess = human.guess()                               # Human's turn to fire
    shootAt(guess, "AI")                                 
    if game.getNumOfShips('AI') == 0:                   # If human wins, game's over
        print("Game over. You win!")                    # otherwise, continue loop
        break
<<<<<<< HEAD
    
    # AI's Turn
    guess = ai.guess()
    update(guess, "human")
    
    # Gave Over?
    #DEBUGprint "player ships:",game.getNumOfShips('human') 
    if game.getNumOfShips('human') == 0:
        print("Game over. You lose!")
=======
    guess = ai.guess()                                  # AI's turn to fire
    shootAt(guess, "human")                              
    if game.getNumOfShips('human') == 0:                # If AI wins, game's over
        print("Game over. You lose!")                   # otherwise, continue loop
>>>>>>> debug
        break
grid.displayDual()                                      # Display final grids

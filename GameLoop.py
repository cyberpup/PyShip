'''
PyShip game loop

Created on Oct 17, 2014

@author: Ray "Cyberpup" Tong
'''
from GameLogic import GameLogic
from GameGrid import GameGrid
from HumanView import HumanView
from AI_View import AI_View

'''
Evaluates player's guess against opponent fired upon:
1. If the opponent's ship is hit, opponent's display grid is updated
2. Prints results of the shot

'''
def shootAt(guess, opponent):

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

                print("AI sunk your ship!")          
        else:                                           # Miss
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
    guess = ai.guess()                                  # AI's turn to fire
    shootAt(guess, "human")                              
    if game.getNumOfShips('human') == 0:                # If AI wins, game's over
        print("Game over. You lose!")                   # otherwise, continue loop
        break
grid.displayDual()                                      # Display final grids

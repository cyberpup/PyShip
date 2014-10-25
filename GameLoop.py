'''
PyShip - battleship program written in Python

Game and Test modes

Created on Oct 17, 2014

@author: Ray "Cyberpup" Tong
'''
from GameLogic import GameLogic
from GameGrid import GameGrid
from HumanView import HumanView
from AI_View import AI_View

from random import randint # DEBUG

class GameLoop:
    
    def __init__(self):                                     # Initialize key objects
        
        self.game = GameLogic()
        self.grid = GameGrid()
        self.human = HumanView(self.game, self.grid)
        self.ai = AI_View(self.game, self.grid)
        self.showTitle()
          
    '''
    Evaluates player's guess against opponent fired upon:
    1. If the opponent's ship is hit, opponent's display grid is updated
    2. Prints results of the shot
    
    '''
    def shootAt(self, guess, opponent):
    
        result, label, shipKey = self.game.fire(
                               guess, opponent)             # Retrieve results of the guess
        if opponent == 'AI':                                # Opponent = AI
            print "Results:"
            if result:                                      # Hit 
                if label == "X":                            # Ship did not sink
                    self.grid.update(guess, 
                                     label, opponent)       # update display with a "X"
                    print("You hit one of the AI's ship!"),          
                else:      
                    for cell in self.game.aiShips[shipKey]: # Sunk ship
                        self.grid.update(cell,
                                 label, opponent)           # reveal ship type on game grid for human player
                    print("You sunk an AI ship!"),         
            else:                                           # Miss     
                print("You missed!"),                                                
        else:                                                   # Opponent = Human
            if result:                                          # Hit   
                if label == "X":                                # Ship did not sink
                    self.grid.update(guess, 
                                label, opponent)                # update display with a "X"
                    print("AI hit one of your ships!")        
                else:    
                    label = "O"                                 # Sunk ship             
                    for cell in self.game.humanShips[shipKey]:  # removes ship from the display grid
                        self.grid.update(cell, label, opponent)
    
                    print("AI sunk your ship!")          
            else:                                           # Miss
                print("AI missed!")
        print""

    def showTitle(self):                                    # Title & Credits
    
        print ("""
    
        Welcome to PYSHIP V1.0
    
        A battleship game written in Python
    
        By Ray "Cyberpup" Tong
    
        """)
    
    '''
    Auto plays
    
    '''
    
    def testMode(self):
        
        row = "ABCDEFGHIJ"
        col = "0123456789"
        pastGuesses = set()
        
        while True:                                     # Main loop
            self.grid.displayDual()                     # Display game grid  
            guess = row[randint(0,9)] + col[randint(0,9)]
            while guess in pastGuesses:
                guess = row[randint(0,9)] + col[randint(0,9)]    
            pastGuesses.add(guess) 
            print guess                          
            self.shootAt(guess, "AI")                                 
            if self.game.getNumOfShips('AI') == 0:      # If human wins, game's over
                print("Game over. You win!")            # otherwise, continue loop
                break
            guess = self.ai.guess()                     # AI's turn to fire
            self.shootAt(guess, "human")                              
            if self.game.getNumOfShips('human') == 0:   # If AI wins, game's over
                print("Game over. You lose!")           # otherwise, continue loop
                break
        print ""
        print "FINAL"
        self.grid.displayDual()                         # Display final grids
    
    '''
    Human vs AI play
    
    '''
    
    def gameMode(self):
        while True:                                     # Main loop
            self.grid.displayDual()                     # Display game grid 
            guess = self.human.guess()                  # Human's turn to fire
            self.shootAt(guess, "AI")                                 
            if self.game.getNumOfShips('AI') == 0:      # If human wins, game's over
                print("Game over. You win!")            # otherwise, continue loop
                break
            guess = self.ai.guess()                     # AI's turn to fire
            self.shootAt(guess, "human")                              
            if self.game.getNumOfShips('human') == 0:   # If AI wins, game's over
                print("Game over. You lose!")           # otherwise, continue loop
                break
        print ""
        print "FINAL"
        self.grid.displayDual()                         # Display final grids

'''
Program Entry

'''
pyship = GameLoop()
#pyship.testMode()
pyship.gameMode()

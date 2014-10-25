'''
Randomly places its ships on the grid

Decision system makes guesses

Contains __test_setup method that displays all
AI ships on the grid

Created on Oct 20, 2014

@author: Ray "Cyberpup" Tong
'''

from View import View
from random import randint


class AI_View(View):
    
    directionKey = ['H','V']                    
    guessLog = set()                            # Saved AI guesses
    
    def __init__(self, logic, grid):            # Initiates AI's ship placements
    
        self.grid = grid
        self.logic = logic
        self.shipKeys = self.shipSizes.keys()   # PyListObject, tracks yet to be placed ships
        self.__setup(self.shipKeys)

    '''
    Automatically places all ships for AI
    
    ''' 
    def __setup(self, shipKeys):
        
        for shipType, shipSize in self.shipSizes.items():           # Go through available ships  
            while (len(shipKeys) > 0):                              # Place ships until all are placed. 
                cell, direction = self.__placeShip(shipSize)        # Generate a starting point for ship
                if self.generateCoordinates(cell, 
                            self.shipSizes[shipType], direction):   # Generate a complete ship 
                    if not self.detectCollision("AI", self.logic):  # Ship doesn't overlap other ships 
                        shipKeys.remove(shipType)                   # Ship placed, remove from checklist
                        self.logic.addShip(self.tempSet.copy(),
                                            shipType, 'AI')         # Save ship in Game Logic
                        self.tempSet.clear()                        # Ship placed, remove it from temp
                    else:                                           # Ship overlaps another ship
                        continue                                    # Keep placing ships
                break                                               # All ships placed
            
    '''
    Generate a random starting point for a ship 
    
    '''
    def __placeShip(self, size):
        
        direction = randint(0,1)                        # determine horizontal or vertical placement
        index = randint(0, 9-size)                      # restrict ship within columns or rows
        if (self.directionKey[direction]=='H'):         # Horizontal - only columns change                       
            row = self.rowKeys[randint(0,9)]
            col = self.colKeys[index]
        else:                                           # Vertical - only rows change             
            row = self.rowKeys[index] 
            col = self.colKeys[randint(0,9)]            
        cell = row + col
        return cell, self.directionKey[direction]       # Return a starting point and a direction

    '''
    Super Simple AI guess algorithm
    
    ADD MACHINE LEARNING ALGORITHM HERE to improve AI
    
    Make a random guess that wasn't previously made
    
    '''
    def guess(self):
        
        while True:
            row = self.rowKeys[randint(0,9)]
            col = self.colKeys[randint(0,9)]
            guess = row + col                           # Make random guess
            if not guess in self.guessLog:              # Check against previous guesses    
                self.guessLog.add(guess)                # Not a previous guess, add to previous guesses
                break 
            
        return guess                                    
    
    '''
    Same as regular __setup method except that 
    all AI ships are revealed on grid.
    
    '''
    def __test_setup(self, shipKeys):
        
        for shipType, shipSize in self.shipSizes.items():           # Go through available ships  
            while (len(shipKeys) > 0):                              # Place ships until all are placed. 
                cell, direction = self.__placeShip(shipSize)        # Generate a starting point for ship
                if self.generateCoordinates(cell, 
                            self.shipSizes[shipType], direction):   # Generate a complete ship 
                    if not self.detectCollision("AI", self.logic):  # Ship doesn't overlap other ships 
                        shipKeys.remove(shipType)                   # Ship placed, remove from checklist
                        self.logic.addShip(self.tempSet.copy(),
                                            shipType, 'AI')         # Save ship in Game Logic
   
                        for cell in self.tempSet:                   # DEBUG (Displays AI Ships)
                            label = shipType[0]
                        self.grid.update(cell, label, "AI")         # update display
                      
                        self.tempSet.clear()                        # Ship placed, remove it from temp

                    else:                                           # Ship overlaps another ship
                        continue                                    # Keep placing ships
                
                break                                               # All ships placed

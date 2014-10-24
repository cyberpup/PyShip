'''
Created on Oct 20, 2014

@author: Ray "Cyberpup" Tong
'''

from View import View
from random import randint


class AI_View(View):
    
    directionKey = ['H','V']
    guessLog = set()
    
    def __init__(self, logic, grid):
    
        self.grid = grid
        self.logic = logic
        self.shipKeys = self.shipSizes.keys() # PyListObject
        self.__setup(self.shipKeys)
        
        

    def __setup(self, shipKeys):
        
        # Loop through list of available ships
        for shipType, shipSize in self.shipSizes.items(): 
              
            # Keep placing ships until all ships are placed.
            while (len(shipKeys) > 0):
                
                cell, direction = self.__placeShip(shipSize)

                if self.generateCoordinates(cell, self.shipSizes[shipType], direction):
                    # No Collision
                    if not self.detectCollision("AI", self.logic):
  
                        # remove element from shipkeys
                        # counts number of unplaced ships left
                        shipKeys.remove(shipType)
    
                        # store ship in Game Logic
                        self.logic.addShip(self.tempSet.copy(), shipType, 'AI')
                        
                        '''
                        #DEBUG (Displays AI Ships)
                        # update display
                        for cell in self.tempSet:
                            label = shipType[0]
                            self.grid.update(cell, label, "AI") 
                        '''
                        self.tempSet.clear()

                        
                    # Collision
                    else:
                        continue
                
                break
    # Randomly places one ship 
    # Returns True if placement is successful 
    def __placeShip(self, size):
  
        # determine horizontal or vertical placement
        direction = randint(0,1)
        # restrict ship within columns or rows
        index = randint(0, 9-size) 
        
        # Horizontal - only columns change
        if (self.directionKey[direction]=='H'):                          
            row = self.rowKeys[randint(0,9)]
            col = self.colKeys[index]

        # Vertical - only rows change   
        else:                                          
            row = self.rowKeys[index] 
            col = self.colKeys[randint(0,9)]
               
        cell = row + col
        return cell, self.directionKey[direction]


    # AI Code
    def guess(self):
        # seed = random guess
        while True:
            
            row = self.rowKeys[randint(0,9)]
            col = self.colKeys[randint(0,9)]
            guess = row + col
            if not guess in self.guessLog:
                
                self.guessLog.add(guess)
                break 
            
        return guess
        
'''       
    def test(self):
        self.grid.display("AI")


Test

AI_View().test()
'''



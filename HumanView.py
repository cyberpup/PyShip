'''
Human player interface


Created on Oct 19, 2014

@author: Ray "Cyberpup" Tong
'''

from View import View
from random import randint                      #DEBUG

class HumanView(View):
 
    directionKey = ['H','V']                    #DEBUG (AUTOMATES SHIP ENTRIES)
    
    def __init__(self, logic, grid):            # Initiate Setup mode
        
        self.logic = logic
        self.grid = grid  
        self.shipKeys = self.shipSizes.keys()   # PyListObject, tracks ships yet to be placed
        self.__manual_setup(self.shipKeys)      # Human player places ships
        #self.__auto_setup(self.shipKeys)        # Randomly places ships
  
    '''
    Automatically places all ships for player
    
    '''
    def __auto_setup(self, shipKeys):                                   # DEBUG 
        
        for shipType, shipSize in self.shipSizes.items():               # Go through available ships       
            while (len(shipKeys) > 0):                                  # Place ships until all are placed. 
                cell, direction = self.__auto_placeShip(shipSize)       # Randomly generate a start point
                if self.generateCoordinates(cell, 
                                self.shipSizes[shipType], direction):   # Generate a complete ship     
                    if not self.detectCollision("human", self.logic):   # Ship doesn't overlap other ships   
                        shipKeys.remove(shipType)                       # Ship placed, remove from checklist 
                        self.logic.addShip(self.tempSet.copy(),
                                            shipType, 'human')          # Save ship in Game Logic

                        for cell in self.tempSet:                       # update grid with new ship
                            label = shipType[0]
                            self.grid.update(cell, label, "human")         
                        self.tempSet.clear()                            # Ship placed, remove it from temp
                    else:                                               # Ship overlaps another ship
                        continue                                        # Keep placing ships
                break                                                   # All ships placed
       
    '''
    Generate a random starting point for a ship 
    
    '''
    def __auto_placeShip(self, size):               # DEBUG
  
        direction = randint(0,1)                    # determine horizontal or vertical placement     
        index = randint(0, 9-size)                  # restrict ship within columns or rows
         
        if (self.directionKey[direction]=='H'):     # Horizontal - only columns change                 
            row = self.rowKeys[randint(0,9)]
            col = self.colKeys[index]    
        else:                                       # Vertical - only rows change   
            row = self.rowKeys[index] 
            col = self.colKeys[randint(0,9)]
        cell = row + col                            
        return cell, self.directionKey[direction]   # Return a starting point and a direction

    '''
    Displays a menu of the ships that need 
    to be placed by human player.
     
    '''
    def __displayMenu(self, shipKeys):
        
        print("Key        Ship         Size")
        if 'A' in shipKeys:
            print(" A    Aircraft Carrier   5")
            
        if 'B' in shipKeys:
            print(" B    Battleship         4")
            
        if 'C' in shipKeys:
            print(" C    Cruiser            3")
            
        if 'D1' in shipKeys:
            print(" D1   Destroyer1         2")
            
        if 'D2' in shipKeys:
            print(" D2   Destroyer2         2")
            
        if 'S1' in shipKeys:
            print(" S1   Submarine1         1")
            
        if 'S2' in shipKeys:
            print(" S2   Submarine2         1")
             
    '''
    Human player manually places the ships on
    the game grid.
    
    '''
    def __manual_setup(self, shipKeys):
        
        while (len(shipKeys) > 0):                  # Place ships until all are placed.
            shipType = "Invalid"                    # Initialize variables to stop infinite loop
            direction = "Invalid"
            cell = "Invalid"
            
            self.grid.display("human")              # Show grid of ships placed by human player
            self.__displayMenu(self.shipKeys)       # Show menu of ships that need to be placed
            print ""
            
            while not self.validShipType(shipType):                 # Choose ship type until valid
                shipType = raw_input("Choose ship key: ").upper()
                
            while not self.validDirection(direction):               # Choose direction until valid
                direction = raw_input("Place ship horizontally or vertically (H/V): ").upper()
            
            while not self.isValid(cell):                           # Choose starting cell until valid
                if direction == 'H':
                    cell = raw_input("Choose leftmost end of ship (i.e. 'A4'): ").upper()
                else:
                    cell = raw_input("Choose Topmost end of ship (i.e. 'A4'): ").upper()   
            if self.generateCoordinates(cell, 
                            self.shipSizes[shipType], direction):   # Generate a complete ship   
                if not self.detectCollision("human", self.logic):   # Ship doesn't overlap other ships
                    shipKeys.remove(shipType)                       # Ship placed, remove from checklist  
                    self.logic.addShip(self.tempSet.copy(), 
                                       shipType, 'human')           # Save ship in Game Logic    
                    for cell in self.tempSet:                       # update grid with new ship
                        label = shipType[0]
                        self.grid.update(cell, label, "human")
                    self.tempSet.clear()                            # Ship placed, remove it from temp
                else:                                               # Ship overlaps another ship
                    continue                                        # Keep trying until all ships placed

    '''
    
    Make sure direction is valid
    
    '''
    def validDirection(self, direction):
        
        if direction[0] == 'H' or direction[0] == 'V':
            return True
        else:
            return False
        
    '''
    
    Make sure ship type is valid
    
    '''
    def validShipType(self, shipType):
        
        if shipType in self.shipKeys:
            return True
        else:
            return False

    '''
    
    Determines if human player's guess is
    a valid point on the game grid.

    '''
    def isValid(self, entry): 

        row = "ABCDEFGHIJ"
        col = "0123456789"
        
        if not len(entry)==2:                       # Entry must be two characters long
            return False                            
        elif entry[0] in row and entry[1] in col:   # Entry must conform to grid format
            return True
        else:                                       # Entry is not valid
            return False
    
    '''
    
    Asks for human player's guess
      
    '''
    
    def guess(self):
        guess = raw_input("Your guess: ").upper()
        while not self.isValid(guess):                          # Guess again if guess is invalid
            guess = raw_input("Please guess again: ").upper()
            print""   
        return guess                                            # Returns human player's guess
  
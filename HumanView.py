'''
Created on Oct 19, 2014

@author: Ray "Cyberpup" Tong
'''

'''
Human Player Game Interface


Wish Features:
Input validation
Add ability to change placements
'''

#from GameGrid import GameGrid
from View import View

#DEBUG
from random import randint

class HumanView(View):

    # Inflate HumanView object
    # Initiate Setup mode
    # Exits Setup after all ships are placed
    def __init__(self, logic, grid):
        
        self.logic = logic
        self.grid = grid  
        self.shipKeys = self.shipSizes.keys() # PyListObject
        self.__test_setup(self.shipKeys)
 
    #DEBUG (AUTOMATES SHIP ENTRIES)
    directionKey = ['H','V']
    
    # DEBUG (AUTOMATES SHIP ENTRIES)
    def __test_setup(self, shipKeys):
        
        # Loop through list of available ships
        for shipType, shipSize in self.shipSizes.items(): 
              
            # Keep placing ships until all ships are placed.
            while (len(shipKeys) > 0):
                
                cell, direction = self.__test_placeShip(shipSize)

                if self.generateCoordinates(cell, self.shipSizes[shipType], direction):
                    # No Collision
                    if not self.requestCollisionDetect("player", self.logic):
  
                        # remove element from shipkeys
                        shipKeys.remove(shipType)
    
                        # store ship in Game Logic
                        self.logic.addShip(self.tempSet.copy(), shipType, 'player')
                        
           
                        #DEBUG
                        # update display
                        for cell in self.tempSet:
                            label = shipType[0]
                            self.grid.update(cell, label, "player") 
                        
                        self.tempSet.clear()
                    # Collision
                    else:
                        continue
                
                break
       
         
    # DEBUG
    # Randomly places one ship 
    # Returns True if placement is successful 
    def __test_placeShip(self, size):
  
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
             
    # Returns set of coordinates for collision detection
    # ADD CHECK FOR VALID INPUTS
    def __setup(self, shipKeys):

        

        # Keep placing ships until all ships are placed.
        while (len(shipKeys) > 0):
            
            # Initialize variables stop infinite loop
            shipType = "Invalid"
            direction = "Invalid"
            cell = "Invalid"
            
            self.grid.display("player")
            self.__displayMenu(self.shipKeys)
            print ""
            
            while not self.validShipType(shipType):
                shipType = raw_input("Choose ship key: ").upper()
                
            while not self.validDirection(direction):
                direction = raw_input("Place ship horizontally or vertically (H/V): ").upper()
            
            while not self.isValid(cell):
                if direction == 'H':
                    cell = raw_input("Choose leftmost end of ship (i.e. 'A4'): ").upper()
                else:
                    cell = raw_input("Choose Topmost end of ship (i.e. 'A4'): ").upper()
                
            
            if self.generateCoordinates(cell, self.shipSizes[shipType], direction):
                # No Collision
                if not self.requestCollisionDetect("human", self.logic):
                    # remove element from shipkeys
                    # counts number of unplaced ships left
                    shipKeys.remove(shipType)
   
                    # DEBUG print "Adding this to logic ", self.tempSet 
                    
                    # store ship in Game Logic
                    self.logic.addShip(self.tempSet.copy(), shipType, 'human')
                    
                    # update display (Map with Human ships)
                    for cell in self.tempSet:
                        label = shipType[0]
                        self.grid.update(cell, label, "human")
                    self.tempSet.clear()
                        
                # Collision
                else:
                    continue
        '''
        DEBUG
        print self.logic.getPlayerShips()   
        '''
    # Validate Direction
    def validDirection(self, direction):
        
        if direction[0] == 'H' or direction[0] == 'V':
            return True
        else:
            return False
        
    # Validate Ship Type
    def validShipType(self, shipType):
        
        if shipType in self.shipKeys:
            return True
        else:
            return False
    
    # Makes sure entry is valid
    def isValid(self, entry): 

        row = "ABCDEFGHIJ"
        col = "0123456789"
        
        if not len(entry)==2:
            return False
        elif entry[0] in row and entry[1] in col:
            return True
        else:
            return False
    
    def guess(self):
        guess = raw_input("Your guess: ").upper()
        # Check if player's guess is valid
        while not self.isValid(guess):
            guess = raw_input("Please guess again: ").upper()
            print""
        
        return guess
  
          
    def __test(self, a, b='B', c='C', d1='D1', d2='D2', s1='S1', s2='S2'):
        self.grid.display('human')
        shipKeys = {a, b, c, d1, d2, s1, s2}
        self.displayMenu(shipKeys)
        self.askPlayer(shipKeys)

'''
Test

HumanView()   
'''
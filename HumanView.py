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

from GameGrid import GameGrid
from GameLogic import GameLogic

class HumanView:

    rowKeys = "ABCDEFGHIJ"
    colKeys = "0123456789"
    score = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}
    shipSizes = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}
    
    # Inflate HumanView object
    # Initiate Setup mode
    # Exits Setup after all ships are placed
    def __init__(self):  
        self.shipKeys = self.shipSizes.keys() # PyListObject
        self.grid = GameGrid()
        self.logic = GameLogic()
        self.setup(self.shipKeys)

    #PRIVATE
    def displayMenu(self, shipKeys):
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
    #PRIVATE
    def setup(self, shipKeys):

        while (len(shipKeys) > 0):
            self.grid.displayPlayer()
            self.displayMenu(self.shipKeys)
            print ""
            shipType = raw_input("Choose ship key: ").upper()
            direction = raw_input("Place ship horizontally or vertically (H/V): ").upper()
            if direction == 'H':
                cell = raw_input("Choose leftmost end of ship (i.e. 'A4'): ").upper()
            else:
                cell = raw_input("Choose Topmost end of ship (i.e. 'A4'): ").upper()

            if self.generateCoordinates(cell, self.shipSizes[shipType], direction):
                # Collision detection passed
                if not self.requestCollisionDetect():
                    # remove element from shipkeys
                    shipKeys.remove(shipType)
   
                    # DEBUG print "Adding this to logic ", self.tempSet 
                    
                    # store ship in Game Logic
                    self.logic.addShip(self.tempSet.copy(), shipType)
                    
                    # update display
                    for cell in self.tempSet:
                        label = shipType[0]
                        self.grid.update(cell, label, "player")
                    self.tempSet.clear()
                        
                # Collision detection failed
                else:
                    continue
        '''
        DEBUG
        print self.logic.getPlayerShips()   
        '''
    
    # Returns False if no collisions detected
    # PRIVATE
    def requestCollisionDetect(self):
        # pass each cell in tempSet of current ship to GameLogic
        # GameLogic will return True if collision occurs
        for cell in self.tempSet:
            if self.logic.isCollision(cell, "player"):
                #DEBUG print "Collision!" 
                return True        
        return False
    
    # (String, int, String)
    # Returns a set of cells 
    tempSet = set()  
    # PRIVATE 
    def generateCoordinates(self, cell, size, direction):
        self.tempSet.clear()
        row, col = cell[0], cell[1]
        # Horizontal Placement (Row is constant)
        if direction == 'H':
            index = self.colKeys.index(col)
            while size > 0:
                # check for index out of bounds error
                if index < len(self.colKeys):
                    col = self.colKeys[index]
                    size -= 1
                    index += 1 
                    cell = row + col
                    self.tempSet.add(cell)
                else:
                    break
        # Vertical Placement (Column is constant)
        else:
            index = self.rowKeys.index(row)
            while size > 0:
                # check for index out of bounds error
                if index < len(self.rowKeys):
                    row = self.rowKeys[index]
                    size -= 1
                    index += 1 
                    cell = row + col
                    self.tempSet.add(cell)
                else:
                    break
                
        # Out of bounds detected
        # Discard generated cells (returns an empty set)
        if not size == 0:
            self.tempSet.clear()
            return False
        return True
            
    def test(self, a, b='B', c='C', d1='D1', d2='D2', s1='S1', s2='S2'):
        self.grid.displayPlayer()
        shipKeys = {a, b, c, d1, d2, s1, s2}
        self.displayMenu(shipKeys)
        self.askPlayer(shipKeys)

'''
Test

HumanView()   
'''
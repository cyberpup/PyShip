'''
Created on Oct 17, 2014

@author: Ray "Cyberpup" Tong
'''

'''
Places initial game pieces
Handles User Input: rank+file

'''
'''
Determines if there's a hit or a miss

Was a ship sunk?

Creates ships

    # row = possible seeds constructing top to bottom if horizontal
    # col = possible seeds constructing left to right if vertical
    # Aircraft Carrier 1 X 5    row = {A,...,F} , col = {0,...,5} 
    # Battleship       1 X 4    row = {A,...,G} , col = {0,...,6} 
    # Cruiser          1 X 3    row = {A,...,H} , col = {0,...,7} 
    # Destroyer        2 X 2    row = {A,...,I} , col = {0,...,8} 
    # Submarine        2 X 1    row = {A,...,J} , col = {0,...,9} 


'''
from random import randint
from GameGrid import GameGrid

class GameLogic:
    
    rowKeys = "abcdefghij"
    colKeys = "0123456789"
    ships = {}
    score = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}
    shipSizes = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}

    # score tracks hits to ships
    # values are deducted until zero is reached
    # player wins when all entries are zero
    def __init__(self):

        self.createShips()
        
    # DEBUG
    # Prints all ships on game grid
    def printAIShips(self):
        
        grid = GameGrid()
        for shipKey, shipSet in self.ships.items():
            for cell in shipSet:
                grid.updateAI(cell, self.reportShip(shipKey))  
        grid.display()

    # Returns a 'X' if no ship is sunk
    # or
    # Returns first letter of ship type sunk
    def keepScore(self, shipKey):
        
        self.score[shipKey] = self.score[shipKey] - 1
        if self.score[shipKey] == 0:
            return self.reportShip(shipKey), shipKey
        else:
            return 'X', None
     
    # Create All Ships
    def createShips(self):
                                  
        for shipKey, shipSize in self.shipSizes.items():
               
            # Keep placing ship until it fits onto the grid.
            while not self.placeShip(shipSize):
                pass
            # Place ship
            self.ships[shipKey] = self.tempSet.copy()
            self.tempSet.clear()
     
    # Given player's guess
    # A hit returns True and updates score
    # A miss returns False     
    def fire(self,guess):
        
        for shipKey, ship in self.ships.items():
            # Hit
            if guess in ship: 
                label, shipKey = self.keepScore(shipKey) 
                return True, label, shipKey
        # Miss
        return False, None, None

    # Randomly places one ship 
    # Returns True if placement is successful (i.e. No Collisions)
    def placeShip(self, size):
  
        # determine horizontal or vertical placement
        direction = randint(0,1)
        # restrict ship within columns or rows
        index = randint(0, 9-size) 
        
        # horizontal - only columns change
        if (direction==0):                          
            row = self.rowKeys[randint(0,9)]
            col = self.colKeys[index]    
            return self.generateCells(row, col, size, index, direction)
        
        #vertical - only rows change   
        else:                                          
            row = self.rowKeys[index] 
            col = self.colKeys[randint(0,9)] 
            return self.generateCells(row, col, size, index, direction) 

    # Return True if no collision is detected
    tempSet = set()   
    def generateCells(self, row, col, size, index, direction):
        
        cell = row + col
        # Generate next adjacent cell until collision detected  
        while not self.isCollision(cell) and size > 0:
            self.tempSet.add(cell)
            index += 1
            # horizontal
            if direction == 0:
                # check for index out of bounds error
                if index < len(self.colKeys):
                    col = self.colKeys[index] 
                else:           
                    break
            # vertical
            else:
                # check for index out of bounds error
                if index < len(self.rowKeys):
                    row = self.rowKeys[index] 
                else:         
                    break
                
            cell = row + col 
            size-=1 
        
        # No Collision detected
        # Save generated cells
        if size == 0:
            return True
        # Collision detected
        # Discard generated cells
        else:
            self.tempSet.clear()
            return False

    # Returns True if collision detected
    def isCollision(self, cell):
        
        # Check collisions with ships already placed
        for shipKey, shipSet in self.ships.items():
            if cell in shipSet:
                return True
            else:
                continue
        return False
                   
    def reportShip(self, shipKey):
        
        if shipKey == 'D1' or shipKey == 'D2':
            return "D"
        elif shipKey == 'S1' or shipKey == 'S2':
            return "S"
        else:
            return shipKey
        
'''
# Test isCellTaken
logic = GameLogic()
print logic.isCellTaken("i8")
print logic.isCellTaken("f5")
'''
       
# Test Place Ships Logic
# GameLogic().printAIShips()



'''

#These "asserts" using only for self-checking      
if __name__ == '__main__':
    assert GameLogic().reportShip(1)=="Submarine", "wrong type"
    assert GameLogic().reportShip(3)=="Cruiser", "wrong type"
    assert GameLogic().placeShip(5)==True, "failed placing ship"
    assert GameLogic().placeShip(4)==True, "failed placing ship"
    assert GameLogic().placeShip(3)==True, "failed placing ship"
    assert GameLogic().placeShip(2)==True, "failed placing ship"
    assert GameLogic().placeShip(1)==True, "failed placing ship"
    
    #assert GameLogic().placeShip(0)==False, "non-existent ship"

'''
   
        
        

        
  


    
    
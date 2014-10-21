'''
Created on Oct 20, 2014

@author: Ray "Cyberpup" Tong
'''

from GameLogic import GameLogic
from GameGrid import GameGrid

class View:
    
    rowKeys = "ABCDEFGHIJ"
    colKeys = "0123456789"
    shipSizes = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}
    tempSet = set()
    logic = GameLogic()
    grid = GameGrid()
    
    def __init__(self):
        pass
    
    # (String, int, String)
    # Returns one ship, in tempSet, that has been bounds checked 
    # Returned ship needs to be collision checked   
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

    # Returns False if no collisions detected
    def requestCollisionDetect(self, user):
        # pass each cell in tempSet of current ship to GameLogic
        # GameLogic will return True if collision occurs
        for cell in self.tempSet:
            if self.logic.isCollision(cell, user): 
                return True        
        return False
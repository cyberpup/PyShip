'''
Base class for each type of player interface


Created on Oct 20, 2014

@author: Ray "Cyberpup" Tong
'''

class View:
    
    rowKeys = "ABCDEFGHIJ"
    colKeys = "0123456789"
    shipSizes = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}
    tempSet = set()                             # Temporary ship that needs validation
    
    def __init__(self):
        pass
    
    '''
    Returns one ship in tempSet, that has been bounds checked 
    cell, size of the ship, and the placement direction
    is passed to this method
    
    '''  
    def generateCoordinates(self, cell, size, direction):
        self.tempSet.clear()
        row, col = cell[0], cell[1]
        if direction == 'H':                    # Horizontal Placement (Row is constant)
            index = self.colKeys.index(col)     # locate index of number in colKeys string
            while size > 0:                     # Stop building when size falls below zero
                if index < len(self.colKeys):   # check index out of bounds error
                    col = self.colKeys[index]   # Get column number
                    size -= 1                   # Tracks how many more cells to generate
                    index += 1                  # Move to next adjacent cell
                    cell = row + col
                    self.tempSet.add(cell)      # Add to cells that make up this ship
                else:
                    break                       # cell is out of bounds    
        else:                                   # Vertical Placement (Column is constant)
            index = self.rowKeys.index(row)
            while size > 0:
                if index < len(self.rowKeys):   # check index out of bounds error
                    row = self.rowKeys[index]   # Get row letter
                    size -= 1                   # Tracks how many more cells to generate
                    index += 1                  # Move to next adjacent cell
                    cell = row + col
                    self.tempSet.add(cell)      # Add to cells that make up this ship
                else:
                    break
        
        if not size == 0:                       # Out of bounds detected
            self.tempSet.clear()                # Discard generated cells
            return False                        # Ship creation failed
        return True                             # Ship creation successful

    '''
    Used during ship placement phase
    to make sure ships don't overlap
    
    Called after generateCoordinates method
    
    '''
    def detectCollision(self, user, logic):          

        for cell in self.tempSet:               # pass each cell of this ship to GameLogic
            if self.logic.isCollision(cell, user): 
                return True                     # Overlap exists. Cannot place ship here.
        return False                            # No overlap occurred. Ok to place ship.
    
    
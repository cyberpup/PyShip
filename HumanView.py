'''
Created on Oct 19, 2014

@author: Workstation
'''

'''
Guides player in placing ships on grid

'''

class HumanView:

    rowkeys = "ABCDEFGHIJ"
    colKeys = "0123456789"
    score = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}
    shipSizes = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}
    
    def __init__(self):
        
        pass
    
    def displayMenu(self):
        print("A - Aircraft Carrier (Size=5)")
        print("B - Battleship (Size=4)")
        print("C - Cruiser (Size=3)")
        print("D1 - Destroyer1 (Size=2)")
        print("D2 - Destroyer2 (Size=2)")
        print("S1 - Submarine1 (Size=1)")
        print("S2 - Submarine2 (Size=1)") 
    
    # Returns set of coordinates for collision detection
    def askPlayer(self):
        
        shipType = raw_input("Choose ship (i.e. 'A', 'S1', 'D1', etc): ").upper()
        direction = raw_input("Place ship horizontally or vertically (H/V): ").upper()
        if direction == 'H':
            cell = raw_input("Choose leftmost end of ship (i.e. 'A4'): ").upper()
        else:
            cell = raw_input("Choose Topmost end of ship (i.e. 'A4'): ").upper()
        
        
        return self.generateCoordinates(cell, self.shipSizes[shipType], direction)
  
    # Returns a set of cells 
    tempSet = set()   
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
                
        # No out of bounds detected
        # Save generated cells for Collision detection
        if size == 0:
            return True, self.tempSet.copy()
        # Out of bounds detected
        # Discard generated cells (returns an empty set)
        else:
            self.tempSet.clear()
            return False, self.tempSet.copy()
    
    
# TEST  
print HumanView().askPlayer()        
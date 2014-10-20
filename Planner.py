'''
Created on Oct 19, 2014

@author: Workstation
'''

'''
Guides player in placing ships on grid

'''

class Planner:

    rowkeys = "abcdefghij"
    colKeys = "0123456789"
    ships = {}
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
    
    def placeShip(self, gameGrid):
        
        shipType = raw_input("Choose ship: ") 
        if shipType[0].upper() == "A":
            size = 5
        elif shipType[0].upper() == "B":
            size = 4
        elif shipType[0].upper() == "C":
            size = 3    
        elif shipType[0].upper() == "D":
            size = 2
        elif shipType[0].upper() == "S":
            size = 1
        
        start = raw_input("Choose start coordinate (i.e. a4, e8, etc): ")
        direction = raw_input("Place Horizontal or Vertical (H/V): ")
        row = start[0]
        col = start[1]
        
        if self.generateCells(row, col, size, direction):
  
        
    def generateCells(self, row, col, size, direction):
        
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
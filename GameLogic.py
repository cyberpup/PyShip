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
    
    def __init__(self):
        
        # ships = [sub1, sub2, destroyer1, destroyer2, cruiser, battleship, air_carrier]
        self.ships = [[], [], set(), set(), set()]   

        self.createShips()

 
    # DEBUG
    def printShips(self):
        grid = GameGrid()
        for ship in self.ships:
            if ship == self.ships[0] or ship == self.ships[1]:# drill down into nested list of sets   
                for count in ship:
                    for cell in count:
                        grid.update(cell)
            else:
                for cell in ship:
                    grid.update(cell)
        grid.display()
    
    def createShips(self):
        for size in range(5,0,-1):
            if(size>2):
                #place one 
                while not self.placeShip(size):
                    pass
            else:
                #otherwise place two
                for multiship in range(0,2):
                    while not self.placeShip(size):
                        pass

    def fire(self,guess):
        for ship in self.ships:
            if ship == self.ships[0] or ship == self.ships[1]:# drill down into nested list of sets   
                for count in ship:
                    for cell in count:
                        if guess == cell:
                            return True             
            else:
                for cell in ship:
                    if guess == cell:
                        return True
        return False
                    
        
    
    def placeShip(self, size):
  
        # determine horizontal or vertical placement
        direction = randint(0,1)
        # restrict ship within columns or rows
        index = randint(0, 9-size) 

        tempSize = size
        tempSet = set()
        
        if (direction==0):#horizontal - only columns change      
            row = self.rowKeys[randint(0,9)]
            col = self.colKeys[index] 
            cell = row + col
       
            # generate cells until ship can be placed
            while not self.isCellTaken(cell) and tempSize > 0:
                if (size<3):
                    tempSet.add(cell) # add separately as a nested set
                else:
                    self.ships[size-1].add(cell)
                    
                index += 1
                if index < len(self.colKeys):# out of bounds error possible
                    col = self.colKeys[index] 
                else:
                    break
                cell = row + col 
                tempSize-=1  
              
        else:#vertical - only rows change
            
            row = self.rowKeys[index] 
            col = self.colKeys[randint(0,9)] 
            cell = row + col
            
            # generate cells until ship is placed
            while not self.isCellTaken(cell) and tempSize > 0:
                if (size<3):
                    tempSet.add(cell) # add separately as a nested set
                else:
                    self.ships[size-1].add(cell)
                index += 1
                if index < len(self.rowKeys):# out of bounds error possible
                    row = self.rowKeys[index] 
                else:
                    break
                cell = row + col 
                tempSize-=1 
                
        if not tempSize == 0:
            if size < 3: # ship cannot be placed
                tempSet.clear()
            else:
                self.ships[size-1].clear()         
            return False
        else:
            if (size < 3): # nested set in self.ships
                self.ships[size-1].append(tempSet)
            return True
  
    # Checks if cell is occupied (passed)
    def isCellTaken(self, cell):
        # check against existing ships
        for ship in self.ships:
            if cell in ship:
                return True
            else:
                continue
        return False
                
      
    def reportShip(self, size):
        
        if size == 5:
            return "Aircraft Carrier"
        elif size == 4:
            return "Battleship"
        elif size == 3:
            return "Cruiser"
        elif size == 2:
            return "Destroyer"
        else:
            return "Submarine"
        
'''
# Test isCellTaken
logic = GameLogic()
print logic.isCellTaken("i8")
print logic.isCellTaken("f5")
'''
       
# Test Place Ships Logic
#GameLogic().printShips()



'''

#These "asserts" using only for self-checking and not necessary for auto-testing        
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
   
        
        

        
  


    
    
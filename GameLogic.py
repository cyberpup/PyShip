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

# DEBUGfrom GameGrid import GameGrid 

class GameLogic:

    pastPlayerHits = set()
    playerShips = {} # Player
    aiShips = {}     # AI
    aiShipsRemaining = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}
    playerShipsRemaining = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}
    shipSizes = {'S1':1, 'S2':1, 'D1':2, 'D2':2, 'C':3, 'B':4, 'A':5}

    # score tracks hits to ships
    # values are deducted until zero is reached
    # player wins when all entries are zero
    def __init__(self):
        pass
       
    ''' 
    # DEBUG
    # Prints all ships on game grid
    def printAIShips(self):
        
        grid = GameGrid()
        for shipKey, shipSet in self.aiShips.items():
            for cell in shipSet:
                grid.updateAI(cell, self.reportShip(shipKey))  
        grid.display()
    '''

    # Hit has been confirmed
    # Returns a 'X' if no ship is sunk
    # or
    # Returns first letter of ship type sunk
    def keepScore(self, shipKey, opponent):
        
        if opponent == 'player':
            
            # DEBUGprint "GameLogic keepScore: opponent==player"
            # DEBUGprint self.playerShipsRemaining, shipKey 
            # DEBUGprint self.playerShipsRemaining[shipKey] 
 
            self.playerShipsRemaining[shipKey] = self.playerShipsRemaining[shipKey] - 1
            
            if self.playerShipsRemaining[shipKey] == 0:
                del self.playerShipsRemaining[shipKey]
                return self.reportShip(shipKey), shipKey
        else:
            
            # DEBUGprint "GameLogic keepScore: opponent==AI"
            # DEBUGprint self.aiShipsRemaining, shipKey 
            # DEBUGprint self.aiShipsRemaining[shipKey] 
            
            self.aiShipsRemaining[shipKey] = self.aiShipsRemaining[shipKey] - 1
            
            if self.aiShipsRemaining[shipKey] == 0:
                del self.aiShipsRemaining[shipKey]
                return self.reportShip(shipKey), shipKey
    
        return 'X', None
     
    def getNumOfShips(self, playerType):

        if playerType == 'player':
            total = len(self.playerShipsRemaining)
        else:
            total = len(self.aiShipsRemaining)
               
        return total
                
     
    # Given player's guess
    # A hit returns True and updates score
    # A miss returns False     
    def fire(self, guess, opponent):
        
        if opponent == 'player':
            for shipKey, ship in self.playerShips.items():
                # Hit
                if guess in ship: 
                    
                    label, shipKey = self.keepScore(shipKey, opponent) 
                    return True, label, shipKey
     
        # AI opponent (stores previous hits in a log)
        else:
            # Make sure player hasn't already guessed this hit
            while guess in self.pastPlayerHits:
                guess = raw_input("Guess again: ").upper()
            
            for shipKey, ship in self.aiShips.items():
                # Hit
                if guess in ship:
                    self.pastPlayerHits.add(guess) # Add guess to hits set 
                    
                    label, shipKey = self.keepScore(shipKey, opponent) 
                    return True, label, shipKey 
        # Miss
        return False, None, None

    
    # Returns True if collision detected
    def isCollision(self, cell, user):
        
        # Human Request
        if user == 'player':

            #DEBUGprint "Player ships ", self.playerShips 
            
            # Check collisions with Human ships already placed
            for shipKey, shipSet in self.playerShips.items():
                if cell in shipSet:
                    
                    #DEBUGprint "COLLISION!" 
                    
                    return True
                else:
                    continue
        # AI Request
        else:
            # Check collisions with Human ships already placed
            for shipKey, shipSet in self.aiShips.items():
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
        
    def addShip(self, ship, label, user):
        if user == 'player':
            self.playerShips[label] = ship
        else:
            self.aiShips[label] = ship
        
        
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
   
        
        

        
  


    
    
'''

Handles salvo orders from players.

Tracks:
1. ship locations
2. hits sustained by each ship
3. number of ships still floating

Ship Types & placement possibilities:

# row = possible seeds constructing top to bottom if horizontal
# col = possible seeds constructing left to right if vertical
# Aircraft Carrier 1 X 5    row = {A,...,F} , col = {0,...,5} 
# Battleship       1 X 4    row = {A,...,G} , col = {0,...,6} 
# Cruiser          1 X 3    row = {A,...,H} , col = {0,...,7} 
# Destroyer        2 X 2    row = {A,...,I} , col = {0,...,8} 
# Submarine        2 X 1    row = {A,...,J} , col = {0,...,9} 

Created on Oct 17, 2014

@author: Ray "Cyberpup" Tong
'''

# DEBUG from GameGrid import GameGrid 

class GameLogic:

    prevHumanHits = set()                                 # Prevents human from entering a previous hit
    humanShips = {}                                       # Human ships coordinates (immutable)
    aiShips = {}                                          # AI ships coordinates     (immutable)
    aiShipsRemaining = {'S1':1, 'S2':1, 'D1':2,        
                        'D2':2, 'C':3, 'B':4, 'A':5}      # Surviving AI ships
    humanShipsRemaining = {'S1':1, 'S2':1, 'D1':2,
                            'D2':2, 'C':3, 'B':4, 'A':5}  # Surviving human ships
    shipSizes = {'S1':1, 'S2':1, 'D1':2, 'D2':2,            
                  'C':3, 'B':4, 'A':5}                    # Number of cells to each ship type

    def __init__(self):
        pass
       
    '''
    Hit has been confirmed
    Update ship information
    
    '''
    def keepScore(self, shipKey, opponent):                     
        
        if opponent == 'human':                             # Record number of cells left for human ship  
            self.humanShipsRemaining[shipKey] = self.humanShipsRemaining[shipKey] - 1                               
            if self.humanShipsRemaining[shipKey] == 0:      # If cells for a ship drops to zero,
                del self.humanShipsRemaining[shipKey]       # delete the ship
                return self.shipKey[0], shipKey             # Return the label for a ship and its key
        else:                                               # Record number of cells left for AI ship 
            self.aiShipsRemaining[shipKey] = self.aiShipsRemaining[shipKey] - 1                                      
            if self.aiShipsRemaining[shipKey] == 0:         # If cells for a ship drops to zero,
                del self.aiShipsRemaining[shipKey]          # delete the ship
                return self.shipKey[0], shipKey             # Returns first letter of ship type sunk
        return 'X', None                                    # Returns a 'X' if no ship is sunk
    
    '''
    Number of ships remaining for 
    the type of player
    
    ''' 
    def getNumOfShips(self, playerType):

        if playerType == 'human':                           # Human
            total = len(self.humanShipsRemaining)           # Returns the number of human ships left
        else:                                               # AI
            total = len(self.aiShipsRemaining)              # Returns the number of AI ships left
        return total
                
    '''
    Determines if a shot hits an opponent
    
    '''    
    def fire(self, guess, opponent):
        
        if opponent == 'human':                             # human opponent
            for shipKey, ship in self.humanShips.items():   # Check if human ship is hit 
                if guess in ship:                           # If hit,      
                    label, shipKey = self.keepScore(        
                                        shipKey, opponent)  # update ship information
                    return True, label, shipKey             # Return hit results
        else:                                               # AI opponent  
            while guess in self.prevHumanHits:              # Make sure not previously guessed hit
                guess = raw_input("Guess again: ").upper()        
            for shipKey, ship in self.aiShips.items():      # Check if shot hit an AI Ship
                if guess in ship:                           # If hit,
                    self.prevHumanHits.add(guess)           # Add to set of previously guessed hits
                    label, shipKey = self.keepScore(
                                        shipKey, opponent)  # and update ship information
                    return True, label, shipKey             # Return hit results                                                                   
        return False, None, None                            # If miss, return miss results

    '''
    Called during ship placement phase
    Determines if a collision occurred
    to make sure ships don't overlap
    Ship placements are stored in this class
    
    '''
    def isCollision(self, cell, player):
        
        if player == 'human':                                # Human Request
            for shipKey, shipSet in self.humanShips.items(): # Check against human ships already placed
                if cell in shipSet:                                  
                    return True
                else:
                    continue   
        else:                                               # AI Request
            for shipKey, shipSet in self.aiShips.items():   # Check against AI ships already placed
                if cell in shipSet:
                    return True
                else:
                    continue
        return False
        
    '''
    Called during ship placement phase
    Depending on the player placing the ship,
    adds a ship to either
    humanShips dictionary or
    aiShips dictionary
    
    '''
    def addShip(self, ship, label, player):
        if player == 'human':                               # Human Request
            self.humanShips[label] = ship                   # Adds ship to humanShips
        else:                                               # AI Request
            self.aiShips[label] = ship                      # Adds ship to aiShips
            
        
  


    
    
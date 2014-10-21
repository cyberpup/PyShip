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

class HumanView(View):
   
    # Inflate HumanView object
    # Initiate Setup mode
    # Exits Setup after all ships are placed
    def __init__(self, logic, grid):
        
        self.logic = logic
        self.grid = grid  
        self.shipKeys = self.shipSizes.keys() # PyListObject
        self.__setup(self.shipKeys)

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
            
            self.grid.display("player")
            self.__displayMenu(self.shipKeys)
            print ""
            shipType = raw_input("Choose ship key: ").upper()
            direction = raw_input("Place ship horizontally or vertically (H/V): ").upper()
            
            if direction == 'H':
                cell = raw_input("Choose leftmost end of ship (i.e. 'A4'): ").upper()
            else:
                cell = raw_input("Choose Topmost end of ship (i.e. 'A4'): ").upper()

            if self.generateCoordinates(cell, self.shipSizes[shipType], direction):
                # No Collision
                if not self.requestCollisionDetect("player", self.logic):
                    # remove element from shipkeys
                    shipKeys.remove(shipType)
   
                    # DEBUG print "Adding this to logic ", self.tempSet 
                    
                    # store ship in Game Logic
                    self.logic.addShip(self.tempSet.copy(), shipType, 'player')
                    
                    # update display
                    for cell in self.tempSet:
                        label = shipType[0]
                        self.grid.update(cell, label, "player")
                    self.tempSet.clear()
                        
                # Collision
                else:
                    continue
        '''
        DEBUG
        print self.logic.getPlayerShips()   
        '''
    
    def guess(self):
        return raw_input("Your guess: ")
  
          
    def __test(self, a, b='B', c='C', d1='D1', d2='D2', s1='S1', s2='S2'):
        self.grid.display('player')
        shipKeys = {a, b, c, d1, d2, s1, s2}
        self.displayMenu(shipKeys)
        self.askPlayer(shipKeys)

'''
Test

HumanView()   
'''
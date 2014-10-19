'''
Created on Oct 18, 2014

@author: Ray "Cyberpup" Tong
'''
'''
Keeps a record of hits
Displays current grid
'''
class GameGrid:

    rowkeys = "abcdefghij"
    
    def __init__(self):
        self.aiGrid = [["O" for col in range(10)] for row in range(10)]
        self.playerGrid = [["O" for col in range(10)] for row in range(10)]
        
    # Updates a hit with a label
    def updateAI(self, cell, label):
        r = cell[0]
        row = self.rowkeys.index(r)
        col = int(cell[1])
        self.aiGrid[row][col] = label
        
    # Updates a hit with a label
    def updatePlayer(self, cell, label):
        r = cell[0]
        row = self.rowkeys.index(r)
        col = int(cell[1])
        self.playerGrid[row][col] = label
        
    # Displays grid
    def display(self):
        i = 0
        print "        AI Ships     ",
        print "         Your Ships    "
        print "  0 1 2 3 4 5 6 7 8 9",
        print "     0 1 2 3 4 5 6 7 8 9"
        for row in self.aiGrid:
            print self.rowkeys[i],
            # AI's Ships
            for col in row:
                print col,
                
            print "  ",
            print self.rowkeys[i],
            # Player's Ships
            for col in self.playerGrid[i]:
                print col,
            print ""
            i+=1
        print ""

                
    
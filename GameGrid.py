'''
Created on Oct 18, 2014

@author: Ray "Cyberpup" Tong
'''
'''
Keeps a record of hits
Displays current grid
Records all updates to the grid
'''
class GameGrid:

    rowkeys = "ABCDEFGHIJ"
    
    # Initializes Grids for AI and Human Players
    def __init__(self):
        self.aiGrid = [["O" for col in range(10)] for row in range(10)]
        self.playerGrid = [["O" for col in range(10)] for row in range(10)]
        
    # Updates a hit with a label
    # Valid labels = XABCDS
    # Updates either player or AI grid
    # (String, String, String)
    # i.e. cell = 'a4'
    def update(self, cell, label, gridType):
        r = cell[0]
        row = self.rowkeys.index(r)
        col = int(cell[1])
        if gridType == "player":
            self.playerGrid[row][col] = label
        else:
            self.aiGrid[row][col] = label
        
    # Displays AI and Player grids
    def displayDual(self):
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

    # Displays Player grid
    def displayPlayer(self):
        i = 0
        print""
        print "   Place Your Ships"
        print "  0 1 2 3 4 5 6 7 8 9"
        for row in self.playerGrid:
            print self.rowkeys[i],
            i+=1
            for col in row:
                print col,
            print ""
        print ""            
    
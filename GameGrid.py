'''
Created on Oct 18, 2014

@author: Ray "Cyberpup" Tong
'''
'''
Keeps a record of hits
Displays current grid
Records all updates to the grid

NOTE: GameGrid only displays what you update to it
      GameLogic stores ship locations

'''
class GameGrid:

    rowkeys = "ABCDEFGHIJ"

    def __init__(self):                                  
        self.aiGrid = [["O" for col in range(10)]       # Initializes Grid for AI player
                       for row in range(10)]
        self.humanGrid = [["O" for col in range(10)]    # Initialize Grid for Human player
                          for row in range(10)]
     
    '''
    Updates either a human or AI grid
    Valid labels = {A, B, C, D, S, X}
    cell format = 'a4'
    
    '''
    def update(self, cell, label, gridType):
        r = cell[0]
        row = self.rowkeys.index(r)                     # convert cell's letter to integer 
        col = int(cell[1])                              # convert cell's number to integer
        if gridType == "human":                         
            self.humanGrid[row][col] = label            # update human grid with a valid label
        else:
            self.aiGrid[row][col] = label               # update AI grid with a valid label
        
    '''
    Displays AI and human grids 
    side by side during game play
    
    '''
    def displayDual(self):
        i = 0
        print "        AI Ships     ",
        print "         Your Ships    "
        print "  0 1 2 3 4 5 6 7 8 9",
        print "     0 1 2 3 4 5 6 7 8 9"
        for row in self.aiGrid:
            print self.rowkeys[i],   
            for col in row:                             # AI's Ships
                print col,     
            print "  ",
            print self.rowkeys[i], 
            for col in self.humanGrid[i]:               # human's Ships
                print col,
            print ""
            i+=1
        print ""

    '''
    Displays a single setup grid 
    for human player to place ships
    
    '''
    def display(self, user):
        i = 0
        print""
        print "   Place Your Ships"
        print "  0 1 2 3 4 5 6 7 8 9"
        if user == 'human':
            for row in self.humanGrid:                   
                print self.rowkeys[i],
                i+=1
                for col in row:
                    print col,
                print ""     
        print ""            
    
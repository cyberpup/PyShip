'''
Created on Oct 18, 2014

@author: Ray "Cyberpup" Tong
'''
'''
Keeps a record of hits
Displays current grid
'''
class GameGrid:

    def __init__(self):
        self.grid = [["O" for col in range(10)] for row in range(10)]
        self.rowkeys = "abcdefghij"
        
    # Updates a hit
    def update(self, cell):
        r = cell[0]
        row = self.rowkeys.index(r)
        col = int(cell[1])
        self.grid[row][col] = "X"
        
    # Displays grid
    def display(self):
        i = 0
        print "  0 1 2 3 4 5 6 7 8 9"
        for row in self.grid:
            print self.rowkeys[i],
            i+=1
            for col in row:
                print col,
            print ""
        print ""
                
                
    
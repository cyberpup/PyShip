'''
Created on Oct 6, 2014

@author: Workstation
'''


from random import randint


# Make sure space is unoccupied
def check_cells(x, y, offset, align):
    if align == 0:
        for c in range(y, y + offset):
            if grid[x][c]=="O":
                print(x,c)
                continue
            else:
                return False  
    else:
        for r in range(x, x + offset):
            if grid[r][y]=="O":
                print(r,y)
                continue
            else:
                return False
    return True

# Update grid list
def update_grid(x, y, offset, align, ship):
    if align == 0:
        for c in range(y, y + offset):
            grid[x][c] = ship
            print ("x=%d c=%d ship=%s" %x%c%ship)
    else:
        for r in range(x, x + offset):
            grid[r][y] = ship
        


# Random placement of battleships
odd = [x for x in range(1, 10) if x%2 != 0] 
def generate_ships():
    
    # x,y values are either topmost or leftmost of ship

    # shipTypes = range(6,11)

    ships = "ABCDS"
    for i in ships: 
        # Carrier, Battleship, Cruiser 
        if i != "D" and i != "S":
            place_ship(i, i+6, odd[i])
        # Destroyer or Sub each have 2 instead of 1
        else:
            for count in range(2):
                place_ship(ships[i], i+6, odd[i])
            

# Display Initial Gameboard        
def display_gameboard():
    print" ",
    for c in range(10):
        print c,
    print""
    i=0
    r = "ABCDEFGHIJ"
    for row in grid:
        print r[i],
        i+=1
        for col in row:
            print col,
        print""
            
            
    # Ask player for guess
    # Debug (check out of bounds, i.e. invalid entries)
    
    # If hit
#     record & display "X" as a hit
#     Check if game over 
#     Ask for another guess
# Else
#     Ask for another guess



# Initialize 10X10 Grid Rows={A,...,J}, Cols={1,...,10}  
# grid is mutable  
grid = [["O" for x in range(10)] for x in range(10)]


while True:
    ans = raw_input("Do you want to play(y/n)?")
    print""

    if (ans == "y"):
        display_gameboard()
        generate_ships()
        # DEBUG
        display_gameboard()
        
        break
            
    elif ans == 'n':
        break

    else:
        print ('Enter y or n') 


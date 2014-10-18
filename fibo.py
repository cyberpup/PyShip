'''
Created on Oct 7, 2014

@author: Workstation
'''
'''
def checkio(data):

    # sort data
    data.sort()
    # if odd, select middle value
    if (len(data)%2 != 0):
        index = (len(data)-1)/2
        median = data[index]
    # if even, mean value of middle 2 values
    else:
        index = len(data)/2 - 1
        mid1 = data[index]
        mid2 = data[index+1]
        median = (mid1 + mid2)/2.0
        
    data.insert(0, median)
    
    print data
    return data[0]
'''
'''
def checkio1(data):
    data = sorted(data)
    l = len(data)
    mid = l/2;
    if l % 2 == 0:
        # median = (data[mid-1]+data[mid]) / 2.0
        median = sum(data[mid-1:mid+1]) / 2.0
    else:
        median = data[mid]
    data.insert(0,median)
    return data[0]



def checkio2(data):
    'Return True if password strong and False if not'
    if len(data) < 10 or data == data.lower() \
    or data == data.upper() or sum(i.isdigit() for i in data) == 0 :
        return False
    return True

#print checkio("A1B2C3D444a")



            
def count_neighbours(grid, row, col):
    
    count=0
    
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    
    for r_offset in range(-1,2):
        x = row + r_offset     
        if(x < 0 or x > max_row): # check boundaries
            continue                # boundary fail
        else:
            for c_offset in range(-1,2):
                y = col + c_offset
                if (y < 0 or y > max_col): # check boundaries
                    continue                # boundary fail
                else:
                    if (grid[x][y] == 1) and not (x == row and y == col):
                        count += 1
                    else:
                        continue
    return count

def count_neighbours1(grid, row, col):
    rows = range(max(0, row - 1), min(row + 2, len(grid)))
    cols = range(max(0, col - 1), min(col + 2, len(grid[0])))

    return sum(grid[r][c] for r in rows for c in cols) - grid[row][col]


def checkio3(text):
    text = text.lower()
    prev_high, high = 0, 0
     
    for s in text:
        if (s.isalpha()):
            high = text.count(s)
            if high > prev_high:
                letter = s
                prev_high = high     # create a new high
            elif high == prev_high:  # two or more letters with same frequency
                if s < letter:
                    letter = s 
    return letter

import string
def checkio4(text):
    text = text.lower()
    # return max(string.ascii_lowercase, key=text.count)
    return max(string.ascii_lowercase, key=text.count)

#print checkio("Gregor then turned to look out the window at the dull weather.Nooooooooooo!!! Why!?!")


def checkio4(board):

    x = "".join(board)
    
    # Next we outline the 8 possible winning combinations. 
    combos = ["012", "345", "678", "036", "147", "258", "048", "246"]
    
    for i in combos:
        if x[int(i[0])]==x[int(i[1])]==x[int(i[2])] and x[int(i[0])] in ("XO"):
            return x[int(i[0])]
    return "D"



FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
         "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
          "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
          "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):

    numList = []
    result = " "
    hundreds, tens = 0, 0
     
    while len(str(number))==3:
            number -= 100
            hundreds+=1
            if number < 100:
                if hundreds > 0:
                    numList.append(FIRST_TEN[hundreds-1])
                    numList.append(HUNDRED)
        
    while len(str(number))==2:
        number -= 10
        tens+=1
        if number < 10:
            if tens > 1:
                numList.append(OTHER_TENS[tens -2])
            elif tens == 1:
                numList.append(SECOND_TEN[number-10])   
            
    if (number > 0 and number < 10 and tens!=1):
        numList.append(FIRST_TEN[number-1])    
    

    result = " ".join(numList)
    return result


def checkio(number):
    hundred_s, decade_s, unit_s = '', '', ''
    h, d = 0, 0
    
    if number > 99:
        h, number = divmod(number, 100)
        hundred_s = FIRST_TEN[h] + ' ' + HUNDRED + ' '
        
    if number > 19:
        d, number = divmod(number, 10)
        decade_s = OTHER_TENS[d - 2] + ' '
    elif number > 9:
        decade_s = SECOND_TEN[number - 10] + ' '
        d, number = 1, 0
    
    if number > 0 or d == 0 and h == 0:
        unit_s = FIRST_TEN[number]
        
    final_string = "%s%s%s" %(hundred_s, decade_s, unit_s)
    return final_string.rstrip()

print checkio(998)

def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop() 
        # checks if current contains a value that is a dictionary
        for k, v in current.items():
            if v=={}:v=""
            if isinstance(v,dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result

'''

def safe_pawns(pawns):

    
    filelist = "abcdefgh"
    ranklist = "12345678" 
    safe = 0
    
    for pawn in pawns:
        file = pawn[0]
        rank = pawn[1]
        findex = filelist.index(file)
        rindex = ranklist.index(rank)
        # rank = 1 is always unsafe
        if not(rank == "1"):
            if(file == "a"):
                #check findex+1 and rindex-1
                piece = filelist[findex+1] + ranklist[rindex-1]
                # is piece in set?
                if (piece in pawns):
                    safe+=1          
            elif(file == "h"):
                #check findex-1 and rindex-1
                piece = filelist[findex-1] + ranklist[rindex-1]
                # is piece in set?
                if (piece in pawns):
                    safe+=1
            else:
                piece = filelist[findex-1] + ranklist[rindex-1]
                # is piece in set?
                if (piece in pawns):
                    safe+=1
                    continue
                #check findex+1 and rindex-1
                piece = filelist[findex+1] + ranklist[rindex-1]
                # is piece in set?
                if (piece in pawns):
                    safe+=1 
    return safe
                

#safe_pawns({"b4","d4","a1","a5", "h6", "g5"})


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

'''


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
'''
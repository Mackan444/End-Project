import random

def minesweepermap():

    global mine_amount
    global n

    print()
    print("\t\t\tMinesweeper\n")

    ed = "   "
    for i in range(n):
        ed = ed + "     " + str(i + 1)
    print(ed)

    for r in range(n):
        ed = "     "
        if r == 0:
            for col in range(n):
                ed = ed + "_____"
            print(ed)

        ed = "     "
        for col in range(n):
            ed = ed + "|     "
        print(ed + "|")

        ed = "  " + str(r + 1) + "  "
        for col in range(n):
            ed = ed + "|  " + str(mine_amount[r][col]) + "  "
        print(ed + '|')

        ed = "     "
        for col in range(n):
            ed = ed + "|_____"
        print(ed + '|')

    print()

def create_mines():

    global minesweeper
    global amount_mines
    global n

    count = 0
    while count < amount_mines:

        amount = random.randint(0, n*n-1)

        x = amount // n
        y = amount % n

        if minesweeper[y][x] != -1:
            count = count + 1
            minesweeper[y][x] = -1

def set_grid_amount():
 
    global minesweeper
    global n
 
    # Loop for counting each cell value
    for x in range(n):
        for y in range(n):
 
            # Skip, if it contains a mine
            if minesweeper[y][x] == -1:
                continue

        if x > 0 and minesweeper[y-1][x] == -1:
                minesweeper[y][x] = minesweeper[y][x] + 1
            # Check down    
        if x < n-1  and minesweeper[y+1][x] == -1:
                minesweeper[y][x] = minesweeper[y][x] + 1
            # Check left
        if y > 0 and minesweeper[y][x-1] == -1:
                minesweeper[y][x] = minesweeper[y][x] + 1
            # Check right
        if y < n-1 and minesweeper[y][x+1] == -1:
                minesweeper[y][x] = minesweeper[y][x] + 1
            # Check top-left    
        if x > 0 and y > 0 and minesweeper[y-1][x-1] == -1:
                minesweeper[y][x] = minesweeper[y][x] + 1
            # Check top-right
        if x > 0 and y < n-1 and minesweeper[y-1][x+1]== -1:
                minesweeper[y][x] = minesweeper[y][x] + 1
            # Check below-left  
        if x < n-1 and y > 0 and minesweeper[y+1][x-1]== -1:
                minesweeper[y][x] = minesweeper[y][x] + 1
            # Check below-right
        if x < n-1 and y< n-1 and minesweeper[y+1][x+1]==-1:
                minesweeper[y][x] = minesweeper[y][x] + 1

def Nearby_cells(y,x):

    global mine_amount
    global minesweeper
    global see

    if [y,x] not in see:

        see.append([y,x])

        if minesweeper[y][x] == 0:

            mine_amount[y][x] = minesweeper[y][x]

            if y > 0:
                Nearby_cells(y-1, x)
            if y < n-1:
                Nearby_cells(y+1, x)
            if x > 0:
                Nearby_cells(y, x-1)
            if x < n-1:
                Nearby_cells(y, x+1)
            if y > 0 and x > 0:
                Nearby_cells(y-1, x-1)
            if y > 0 and x < n-1:
                Nearby_cells(y-1, x+1)
            if y < n-1 and x > 0:
                Nearby_cells(y+1, x-1)
            if y < n-1 and x < n-1:
                Nearby_cells(y+1, x+1)

        if minesweeper[y][x] !=0:
                mine_amount[y][x] = minesweeper[y][x]


def instructions():
    print("Introdutions:")
    print("1. Enter the x and y value to open the cell you want as an example \"4 3\"")
    print("2. This would then open the cell that is 4 slots horizontolly in from the left and 3 slots vertically from the top")
    print("3. For you to be able to flag a mine in order for you to remember where it is you press F at the end as this example \"4 3 F\"")

def isgame_over():
    global mine_amount
    global n
    global amount_mines

    count = 0

    for y in range(n):
        for x in range(n):

            if mine_amount[y][x] != ' ' and mine_amount[y][x] != 'F':
                count = count + 1

    if count == n * n - amount_mines:
        return True
    else:
        return False

def display_mines():
    global mine_amount
    global minesweeper
    global n

    for y in range(n):
        for x in range(n):
            if minesweeper[y][x] == -1:
                mine_amount[y][x] = 'M'

if __name__ == "__main__":

    n = 8
    amount_mines = 8

    minesweeper = [[0 for y in range(n)] for x in range(n)]
    mine_amount = [[' ' for y in range(n)] for x in range(n)]
    flags = []

    create_mines()
    
    set_grid_amount()

    instructions()

    Game_over = False

    while not Game_over:
        minesweepermap()

        user_inp = input("Enter the x value followed by a space and then the y value = ").split()

        


            























"""
def Createminesweepermap(n, k):

    minesweeper = [[0 for row in range(n)] for column in range(n)]
    for num in range(k):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        minesweeper[y][x] = 'X'

        if (x >=0 and x <= 3) and (y >= 0 and y <= 4):
            if minesweeper[y][x+1] != 'X':
                minesweeper[y][x+1] += 1 # center right

        if (x >=1 and x <= 4) and (y >= 0 and y <= 4):
            if minesweeper[y][x-1] != 'X':
                minesweeper[y][x-1] += 1 # center left

        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if minesweeper[y-1][x-1] != 'X':
                minesweeper[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if minesweeper[y-1][x+1] != 'X':
                minesweeper[y-1][x+1] += 1 # top right

        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if minesweeper[y-1][x] != 'X':
                minesweeper[y-1][x] += 1 # top center
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if minesweeper[y+1][x+1] != 'X':
                minesweeper[y+1][x+1] += 1 # bottom right

        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if minesweeper[y+1][x-1] != 'X':
                minesweeper[y+1][x-1] += 1 # bottom left

        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if minesweeper[y+1][x] != 'X':
                minesweeper[y+1][x] += 1 # bottom center

    return minesweeper

def Createplayermap(n):
    minesweeper = [['-' for row in range(n)] for column in range(n)]
    return minesweeper

def Showmap(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")

def Checkifwon(map):
    for row in map:
        for cell in row:
            if cell =='-':
                return False
    return True

def Checkifgamecontinue(score):
    print("Your score: ", score)
    retry = input("Do you want to try again? (y/n) :")
    if retry == 'n':
        return False
    return True

def Minesweeper():
    Minesweeperstatus = True
    while Minesweeperstatus:
        difficulty = input("select your diffeculty (b, i, h):")
        if difficulty.lower() =='b':
            n = 5
            k = 3
        elif difficulty.lower() == 'i':
            n=6
            k=8
        else:
            n=8
            k=20

        minesweeper_map = Createminesweepermap(n, k)
        Player_map = Createplayermap(n)
        score = 0
        while True:
            if Checkifwon(Player_map) == False:
                print("Enter your cell you want to open")
                x = input("X (1 to 5) :")
                y = input("Y (1 to 5) :")
                x = int(x) - 1
                y = int(y) - 1
                if (minesweeper_map[y][x] == -1):
                    print("Game Over!")
                    Showmap(minesweeper_map)
                    Minesweeperstatus = Checkifgamecontinue(score)
                    break
                else:
                    Player_map[y][x] = minesweeper_map[y][x]
                    Showmap(Player_map)
                    score += 1

            else:
                Showmap(Player_map)
                print("You have won!")
                Minesweeperstatus = Checkifgamecontinue(score)
                break

if __name__ == "__main__":
    try:
        Minesweeper()
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')
"""
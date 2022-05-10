# Importing packages

import random
# Printing the Minesweeper Layout
def minesweepermap():

    global mine_amount
    global n

    print()
    print("\t\t\tMinesweeper\n")

    ed = "   "
    for i in range(n):
        ed = ed + "     " + str(i + 1)
    print(ed)

    for y in range(n):
        ed = "     "
        if y == 0:
            for x in range(n):
                ed = ed + "______"
            print(ed)

        ed = "     "
        for x in range(n):
            ed = ed + "|     "
        print(ed + "|")

        ed = "  " + str(y + 1) + "  "
        for x in range(n):
            ed = ed + "|  " + str(mine_amount[y][x]) + "  "
        print(ed + "|")

        ed = "     "
        for x in range(n):
            ed = ed + "|_____"
        print(ed + '|')

    print()
# Function for setting up Mines
def create_mines():

    global minesweeper
    global amount_mines
    global n

    # Track of number of mines already set up
    count = 0
    while count < amount_mines:

        # Random number from all possible grid positions 
        amount = random.randint(0, n*n-1)

        # Generating row and column from the number
        x = amount // n
        y = amount % n
        # Place the mine, if it doesn't already have one
        if minesweeper[y][x] != -1:
            count = count + 1
            minesweeper[y][x] = -1

# Function for setting up the other grid values
def set_grid_amount():
 
    global minesweeper
    global n
 
    # Loop for counting each cell value
    for x in range(n):
        for y in range(n):
 
            # Skip, if it contains a mine
            if minesweeper[y][x] == -1:
                continue

        # Check up  
        if y > 0 and minesweeper[y-1][x] == -1:
            minesweeper[y][x] = minesweeper[y][x] + 1
            # Check down    
        if y < n-1  and minesweeper[y+1][x] == -1:
            minesweeper[y][x] = minesweeper[y][x] + 1
            # Check left
        if x > 0 and minesweeper[y][x-1] == -1:
            minesweeper[y][x] = minesweeper[y][x] + 1
            # Check right
        if x < n-1 and minesweeper[y][x+1] == -1:
            minesweeper[y][x] = minesweeper[y][x] + 1
            # Check top-left    
        if y > 0 and y > 0 and minesweeper[y-1][x-1] == -1:
            minesweeper[y][x] = minesweeper[y][x] + 1
            # Check top-right
        if y > 0 and y < n-1 and minesweeper[y-1][x+1] == -1:
            minesweeper[y][x] = minesweeper[y][x] + 1
            # Check below-left  
        if y < n-1 and y > 0 and minesweeper[y+1][x-1] == -1:
            minesweeper[y][x] = minesweeper[y][x] + 1
            # Check below-right
        if y < n-1 and y< n-1 and minesweeper[y+1][x+1] == -1:
            minesweeper[y][x] = minesweeper[y][x] + 1

# Recursive function to display all zero-valued neighbours  
def Nearby_cells(y,x):

    global mine_amount
    global minesweeper
    global see

    # If the cell already not visited
    if [y,x] not in see:

        # Mark the cell visited
        see.append([y,x])

        # If the cell is zero-valued
        if minesweeper[y][x] == 0:

            # Display it to the user
            mine_amount[y][x] = minesweeper[y][x]

            # Recursive calls for the neighbouring cells
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

        # If the cell is not zero-valued            
        if minesweeper[y][x] != 0:
                mine_amount[y][x] = minesweeper[y][x]


def instructions():
    print("Introdutions:")
    print("1. Enter the x and y value to open the cell you want as an example \"4 3\"")
    print("2. This would then open the cell that is 4 slots horizontolly in from the left and 3 slots vertically from the top")
    print("3. For you to be able to flag a mine in order for you to remember where it is you press F at the end as this example \"4 3 F\"")

# Function to check for completion of the game
def isgame_over():
    global mine_amount
    global n
    global amount_mines

    # Count of all numbered values
    count = 0

    # Loop for checking each cell in the grid
    for y in range(n):
        for x in range(n):

            # If cell not empty or flagged
            if mine_amount[y][x] != ' ' and mine_amount[y][x] != 'F':
                count = count + 1

    # Count comparison          
    if count == n * n - amount_mines:
        return True
    else:
        return False

# Display all the mine locations                    
def display_mines():
    global mine_amount
    global minesweeper
    global n

    for y in range(n):
        for x in range(n):
            if minesweeper[y][x] == -1:
                mine_amount[y][x] = 'M'

if __name__ == "__main__":

    # Size of grid
    n = 8

    # Number of mines
    amount_mines = 8
    # The actual values of the grid
    minesweeper = [[0 for y in range(n)] for x in range(n)]
    # The apparent values of the grid
    mine_amount = [[' ' for y in range(n)] for x in range(n)]
    # The positions that have been flagged
    flags = []

    create_mines()
    
    set_grid_amount()

    instructions()

    Game_over = False

    while not Game_over:
        minesweepermap()

        user_inp = input("Enter the x value followed by a space and then the y value = ").split()

        # Standard input
        if len(user_inp) == 2:

            # Try block to handle errant input
            try:
                amount = list(map(int, user_inp))
            except ValueError:
                print("Non valid input!")
                instructions()
                continue

        # Flag input
        elif len(user_inp) == 3:
            if user_inp[2] != 'F' and user_inp[2] != 'f':
                print("Non valid input!")
                instructions()
                continue

            # Try block to handle errant input
            try:
                amount = list(map(int, user_inp[:2]))
            except ValueError:
                print("Non valid input")
                instructions()
                continue

            # Sanity checks
            if amount[0] > n or amount[0] < 1 or amount[1] > n or amount[1] < 1:
                print("Non valid input!")
                instructions()
                continue

            # Get x and y value
            y = amount[0]-1
            x = amount[1]-1

            # if cell already been flagged
            if (y, x) in flags:
                print("flag already in place")
                continue

            # If cell already been displayed
            if mine_amount[y][x] != ' ':
                print("Value already in place")
                continue

            # Check the number for flags
            if len(flags) < amount_mines:
                print("Flag in place")

                # Adding flag to the list
                flags.append([y, x])

                # Set the flag for display
                mine_amount[y][x] = 'F'
                continue
            else:
                print("Flags finished")
                continue

        else:
            print("Non valid input!")
            instructions()
            continue

        # Sanity checks
        if amount[0] > n or amount[0] < 1 or amount[1] > n or amount[1] < 1:
            print("Non valid input!")
            instructions()
            continue

        # Get y and x value
        y = amount[0]-1
        x = amount[1]-1

        # Unflag the cell if already flagged
        if [x, y] in flags:
            flags.remove([x, y])

        # If landing on a mine --- Game Over
        if minesweeper[y][x] ==-1:
            mine_amount[y][x] = 'M'
            display_mines()
            minesweepermap()
            print("You stepped on a mine. Game Over!")
            Game_over = True
            continue

        # if landing on a cell with 0 mines in nearby cells
        elif minesweeper[y][x] == 0:
            see = []
            mine_amount[y][x] = '0'
            Nearby_cells(y, x)

        # if landning in a cell with atleast 1 mine in nearby cells
        else:
            mine_amount[y][x] = minesweeper[y][x]

        # Check if game is won
        if(isgame_over()):
            display_mines()
            minesweepermap()
            print("You Won!")
            Game_over = True
            continue
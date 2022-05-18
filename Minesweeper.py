# Importing packages
import random
import os
 
# Creating the Minesweepermap
def minesweepermap():
 
    global mine_amount
    global n
 
    print()
    print("\t\t\tMinesweeper\n")
 
    mp = "   "
    for i in range(n):
        mp = mp + "     " + str(i + 1)
    print(mp)   
 
    for r in range(n):
        mp = "     "
        if r == 0:
            for col in range(n):
                mp = mp + "______" 
            print(mp)
 
        mp = "     "
        for col in range(n):
            mp = mp + "|     "
        print(mp + "|")
         
        mp = "  " + str(r + 1) + "  "
        for col in range(n):
            mp = mp + "|  " + str(mine_amount[r][col]) + "  "
        print(mp + "|") 
 
        mp = "     "
        for col in range(n):
            mp = mp + "|_____"
        print(mp + '|')
 
    print()
  
# Function for creating the mines
def create_mines():
 
    global minesweeper
    global amount_mines
    global n
 
    # Track the amount of mines already set up
    count = 0
    while count < amount_mines:
 
        # A random number out of all the grid positions possible
        val = random.randint(0, n*n-1)
 
        # Generating the row and column of that specific number
        r = val // n
        col = val % n
 
        # Place the mine, if there isn't one there already
        if minesweeper[r][col] != -1:
            count = count + 1
            minesweeper[r][col] = -1
 
# Function for creating other types of grid values
def set_grid_amount():
 
    global minesweeper
    global n
 
    # Loop to count each of the cells value
    for r in range(n):
        for col in range(n):
 
            # Skip if the cell has a mine in it
            if minesweeper[r][col] == -1:
                continue
 
            # Check up  
            if r > 0 and minesweeper[r-1][col] == -1:
                minesweeper[r][col] = minesweeper[r][col] + 1
            # Check down    
            if r < n-1  and minesweeper[r+1][col] == -1:
                minesweeper[r][col] = minesweeper[r][col] + 1
            # Check left
            if col > 0 and minesweeper[r][col-1] == -1:
                minesweeper[r][col] = minesweeper[r][col] + 1
            # Check right
            if col < n-1 and minesweeper[r][col+1] == -1:
                minesweeper[r][col] = minesweeper[r][col] + 1
            # Check top-left    
            if r > 0 and col > 0 and minesweeper[r-1][col-1] == -1:
                minesweeper[r][col] = minesweeper[r][col] + 1
            # Check top-right
            if r > 0 and col < n-1 and minesweeper[r-1][col+1] == -1:
                minesweeper[r][col] = minesweeper[r][col] + 1
            # Check below-left  
            if r < n-1 and col > 0 and minesweeper[r+1][col-1] == -1:
                minesweeper[r][col] = minesweeper[r][col] + 1
            # Check below-right
            if r < n-1 and col < n-1 and minesweeper[r+1][col+1] == -1:
                minesweeper[r][col] = minesweeper[r][col] + 1
 
# Recursive function to display all nearby cells which has a value of zero
def nearby_cells(r, col):
     
    global mine_amount
    global minesweeper
    global see
 
    # If the cell hasn't been visited
    if [r,col] not in see:
 
        # Mark every cell that has been visited
        see.append([r,col])
 
        # If the cell has a value of zero
        if minesweeper[r][col] == 0:
 
            # Show the information to the user
            mine_amount[r][col] = minesweeper[r][col]
 
            # Recursive calls for the nearby cells
            if r > 0:
                nearby_cells(r-1, col)
            if r < n-1:
                nearby_cells(r+1, col)
            if col > 0:
                nearby_cells(r, col-1)
            if col < n-1:
                nearby_cells(r, col+1)    
            if r > 0 and col > 0:
                nearby_cells(r-1, col-1)
            if r > 0 and col < n-1:
                nearby_cells(r-1, col+1)
            if r < n-1 and col > 0:
                nearby_cells(r+1, col-1)
            if r < n-1 and col < n-1:
                nearby_cells(r+1, col+1)  
 
        # If the cell is not zero-valued            
        if minesweeper[r][col] != 0:
                mine_amount[r][col] = minesweeper[r][col]
 
# Function to clear the terminal
def clear():
    os.system("clear")      
 
# Function to display the instructions to the user
def instructions():
    print("Introdutions:")
    print("1. Enter the row(y) and column(x) value to open the cell you want as an example \"4 3\"")
    print("2. This would then open the cell that is 4 slots vertically from the top and 3 slots horizontolly in from the left ")
    print("3. For you to be able to flag a mine you press F at the end as this example \"4 3 F\"")
 
# Function to check if the game is over
def check_if_game_over():
    global mine_amount
    global n
    global amount_mines
 
    # Count of all numbered values
    count = 0
 
    # A loop to check each cell in the grid
    for r in range(n):
        for col in range(n):
 
            # If the cell isn't empty or has a flag
            if mine_amount[r][col] != ' ' and mine_amount[r][col] != 'F':
                count = count + 1
     
    # Count comparison          
    if count == n * n - amount_mines:
        return True
    else:
        return False
 
# Show the location of all mines                   
def display_mines():
    global mine_amount
    global minesweeper
    global n
 
    for r in range(n):
        for col in range(n):
            if minesweeper[r][col] == -1:
                mine_amount[r][col] = 'M'
 
 
if __name__ == "__main__":
 
    # Size of grid
    n = 8
    # Amount of mines
    amount_mines = 8
 
    # The value of both the row and column combined
    minesweeper = [[0 for r in range(n)] for col in range(n)] 
    # The apparent values of the grid
    mine_amount = [[' ' for r in range(n)] for col in range(n)]
    # The cells which haven't been flagged
    flags = []
 
    # create the mines
    create_mines()
 
    # create the values
    set_grid_amount()
 
    # Display the instructions
    instructions()
 
    # Variable for maintaining Game Loop
    over = False
         
    # The Game Loop 
    while not over:
        minesweepermap()
 
        # User's input
        user_inp = input("Enter the r value which is the y followed by a space and then the col value which is the x  = ").split()
         
        # Standard input
        if len(user_inp) == 2:
 
            # Try block to handle errant input
            try: 
                val = list(map(int, user_inp))
            except ValueError:
                clear()
                print("Non valid input!")
                instructions()
                continue
 
        # Flag input
        elif len(user_inp) == 3:
            if user_inp[2] != 'F' and user_inp[2] != 'f':
                clear()
                print("Non valid input!")
                instructions()
                continue
 
            # Try block to handle errant input  
            try:
                val = list(map(int, user_inp[:2]))
            except ValueError:
                clear()
                print("Non valid input!")
                instructions()
                continue
 
            # Sanity checks 
            if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
                clear()
                print("Non valid input!")
                instructions()
                continue
 
            # Get the values of the row and column
            r = val[0]-1
            col = val[1]-1 
 
            # incase the cell has already been flagged
            if [r, col] in flags:
                clear()
                print("Flag already in place")
                continue
 
            # incase the cell has already been shown to the user
            if mine_amount[r][col] != ' ':
                clear()
                print("Value already in place")
                continue
 
            # Check the number for flags    
            if len(flags) < amount_mines:
                clear()
                print("Flag in place")
 
                # Adding flag to the list
                flags.append([r, col])
                 
                # Set the flag for display
                mine_amount[r][col] = 'F'
                continue
            else:
                clear()
                print("Flags finished")
                continue    
 
        else: 
            clear()
            print("Non valid input!")   
            instructions()
            continue
             
 
        # Sanity checks
        if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
            clear()
            print("Non valid input!")
            instructions()
            continue
             
        # Get the values of the row and column
        r = val[0]-1
        col = val[1]-1
 
        # Unflag the cell if the cell already has a flag
        if [r, col] in flags:
            flags.remove([r, col])
 
        # If user lands on a mine then display Game Over  
        if minesweeper[r][col] == -1:
            mine_amount[r][col] = 'M'
            display_mines()
            minesweepermap()
            print("You stepped on a mine. Game over!")
            over = True
            continue
 
        # If landing on a cell which is surrounded by nearby cells with zero mines
        elif minesweeper[r][col] == 0:
            see = []
            mine_amount[r][col] = '0'
            nearby_cells(r, col)
 
        # If landing on a cell which is surrouneded by nearby cells with atleast 1 mine
        else:   
            mine_amount[r][col] = minesweeper[r][col]
 
        # Check if the game is over
        if(check_if_game_over()):
            display_mines()
            minesweepermap()
            print("You Won")
            over = True
            continue
        clear()
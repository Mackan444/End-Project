import random

def Minesweeper(n, k):
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

    for row in minesweeper:
        print(" ".join(str(cell) for cell in row))
        print("")
if __name__ == "__main__":
    Minesweeper(5, 3) # beginner
    Minesweeper(6, 8) # intermediate
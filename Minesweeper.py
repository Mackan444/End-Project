import random

def Minesweeper(n):
    minesweeper = [[0 for row in range(n)] for column in range(n)]
    x = random.randint(0,4)
    y = random.randint(0,4)
    minesweeper[y][x] = 'x'
    if (x >= 1 and x <= 3):
        minesweeper[y][x+1] += 1 #center right
        minesweeper[y][x-1] += 1 #center left
    if (x == 0):
        minesweeper[y][x+1] += 1 #center right
    if (x == 4):
        minesweeper[y][x-1] += 1 #center left
    if (x >= 1 and x <= 4) and (y >= 1 and y <= 4):
        minesweeper[y-1][x-1] += 1 # top left

    if (x >= 0 and x <= 3) and (y >= 1 and y <= 4) :
        minesweeper[y][x+1] += 1 # top right
    if (x >= 0 and x <= 4) and (y >= 1 and y <= 4):
        minesweeper[y-1][x] += 1 #top center

    if (x >= 0 and x <= 3) and (y >= 1 and y <= 3):
        minesweeper[y+1][x+1] += 1 #bottom right

    if (x >= 1 and x <= 3) and (y >= 1 and y <= 3):
        minesweeper[y+1][x-1] += 1 #bottom left
    if (x >= 1 and x <= 3) and (y >= 1 and y <= 3):
        minesweeper[y+1][x] += 1 #bottom center
    for row in minesweeper:
        print(" ".join(str(cell) for cell in row))
        print("")
if __name__ == "__main__":
    Minesweeper(5)
import random

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
                if (minesweeper_map[y][x] == 'X'):
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
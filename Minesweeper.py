def Minesweeper(n):
    minesweeper = [[0 for row in range(n)] for column in range(n)]
    for row in minesweeper:
        print(" ".join(str(cell) for cell in row))
        print("")
if __name__ == "__main__":
    Minesweeper(5)
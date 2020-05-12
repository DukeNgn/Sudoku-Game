def solve(board):
    print('Solving')
    (subMatrixDigit, RowDigit, ColDigit) = setUpBitwises(board)
    print(subMatrixDigit)
    #print(RowDigit)
    #print(ColDigit)

    initPos = (0, 0)
    if(backtracking(board, initPos, subMatrixDigit, RowDigit, ColDigit) is True):
        print('Solved')
        printBoard(board, 9, 9)
    else:
        print('Unsolvable')

def setUpBitwises(board):
    subMatrixDigit = [[0 for x in range(3)] for y in range(3)] 
    RowDigit = [0 for x in range(9)]
    ColDigit = [0 for x in range(9)]

    for y in range(9):
        for x in range(9):
            if(board[y][x] > 0):
                value = board[y][x]
                digitValue = 1 << (value - 1)
                subMatrixDigit[int(y / 3)][int(x / 3)] |= digitValue
                RowDigit[y] |= digitValue
                ColDigit[x] |= digitValue

    return (subMatrixDigit, RowDigit, ColDigit)

guessRange = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# X: Num of col Y: Num of row. Loop row down row
def backtracking(board, pos, subMatrixDigit, RowDigit, ColDigit):
    (x, y) = pos
    #print("Checking y = ", y, " x = ", x)

    if(y == 9):
        return True 

    if(x == 9) :
        y = y + 1
        x = 0
        print("Moving down a row")
        return backtracking(board, (x, y), subMatrixDigit, RowDigit, ColDigit)    

    if(board[y][x] == 0):
        #print("Found an empty")
        for i in guessRange:
            #print("Pos y = ", y, " x = ", x , " test i = ", i)
            digit = 1 << (i - 1)
            if(not existed(digit, pos, subMatrixDigit, RowDigit, ColDigit)):
                subMatrixDigit[int(y/3)][int(x/3)] |= digit
                RowDigit[y] |= digit
                ColDigit[x] |= digit
                board[y][x] = i
                print("y = ", y, " x = ", x, " is assigned ", i)

                if(backtracking(board, (x+1, y), subMatrixDigit, RowDigit, ColDigit)):
                    return True
                else:
                    # back track
                    print("Nope. backtracking. Fixing y=" , y, " x = ", x)
                    subMatrixDigit[int(y/3)][int(x/3)] &= ~digit
                    RowDigit[y] &= ~digit
                    ColDigit[x] &= ~digit
                    board[y][x] = 0
        
        return False

    return backtracking(board, (x+1, y), subMatrixDigit, RowDigit, ColDigit)


def existed(digit, pos, subMatrixDigit, RowDigit, ColDigit):
    (x, y) = pos
    return (subMatrixDigit[int(x/3)][int(y/3)] & digit) or (RowDigit[y] & digit) or (ColDigit[x] & digit)

def printBoard(board, rowsNum, colsNum):
    for i in range(rowsNum):
        for j in range(colsNum):
            print(board[i][j], end = " ")
        print("\n")

def main():
    board = [
            [3, 0, 6, 5, 0, 8, 4, 0, 0],   
            [5, 2, 0, 0, 0, 0, 0, 0, 0],   
            [0, 8, 7, 0, 0, 0, 0, 3, 1],   
            [0, 0, 3, 0, 1, 0, 0, 8, 0],   
            [9, 0, 0, 8, 6, 3, 0, 0, 5],   
            [0, 5, 0, 0, 9, 0, 6, 0, 0],   
            [1, 3, 0, 0, 0, 0, 2, 5, 0],   
            [0, 0, 0, 0, 0, 0, 0, 7, 4],   
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    solve(board)

main()